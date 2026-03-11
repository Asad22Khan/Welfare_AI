import random
from config import llm
from schemas.registration_schema import RegistrationInfo
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import PydanticOutputParser

REQUIRED_FIELDS = ["name", "phone", "address", "support_type"]

parser = PydanticOutputParser(pydantic_object=RegistrationInfo)


def registration_agent(state):

    user_query = state.get("user_query", "")

    # Extract structured info
    extraction_prompt = f"""
Extract the following information from the user message.

{parser.get_format_instructions()}

User Message:
{user_query}
"""

    response = llm.invoke([HumanMessage(content=extraction_prompt)])

    try:
        extracted = parser.parse(response.content)
    except:
        extracted = RegistrationInfo()

    # Update state with extracted values
    for field in REQUIRED_FIELDS:
        value = getattr(extracted, field)
        if value and not state.get(field):
            state[field] = value

    # Check missing fields
    missing_fields = [f for f in REQUIRED_FIELDS if not state.get(f)]

    if missing_fields:

        ask_prompt = f"""
You are a welfare registration assistant.

Collected information:

Name: {state.get("name")}
Phone: {state.get("phone")}
Address: {state.get("address")}
Support Type: {state.get("support_type")}

Ask the user politely for the next missing information: {missing_fields[0]}.
Only ask for one thing at a time.
"""

        ask_response = llm.invoke([HumanMessage(content=ask_prompt)])

        state["response"] = ask_response.content
        return state

    # All information collected
    ref = f"DNE-{random.randint(1000,9999)}"
    state["reference_id"] = ref

# SAVE TO DATABASE
    save_registration({
        "reference_id": ref,
        "name": state["name"],
        "phone": state["phone"],
        "address": state["address"],
        "support_type": state["support_type"]
    })

    

    final_prompt = f"""
You are a welfare registration assistant.

Generate a short confirmation message.

Rules:
- Maximum 4 lines
- Do NOT invent phone numbers
- Do NOT add extra contact information
- Do NOT add placeholders like [Organization Name]

User Details:
Name: {state['name']}
Address: {state['address']}
Support Type: {state['support_type']}

Reference ID: {ref}

Tell the user:
1. Their registration is successful
2. Their request is pending admin approval
3. Show the Reference ID
"""

    final_response = llm.invoke([HumanMessage(content=final_prompt)])

    state["response"] = final_response.content

    return state

from database.db import SessionLocal
from database.models import Registration


def save_registration(data):

    db = SessionLocal()

    new_user = Registration(
        reference_id=data["reference_id"],
        name=data["name"],
        phone=data["phone"],
        address=data["address"],
        support_type=data["support_type"],
        status="PENDING"
    )

    db.add(new_user)
    db.commit()
    db.close()