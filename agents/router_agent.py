from config import llm
from langchain_core.messages import HumanMessage


def router_agent(state):

    message = state.get("user_query", "")

    prompt = f"""
Classify the user intent.

Return ONLY one word from this list:

register
donee
donor
surveyor
admin

Message:
{message}
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    intent = response.content.strip().lower()

    allowed = ["register", "donee", "donor", "surveyor", "admin"]

    if intent not in allowed:
        intent = "register"

    return {"route": intent}