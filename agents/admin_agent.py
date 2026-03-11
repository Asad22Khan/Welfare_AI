from config import llm
from database.db import SessionLocal
from database.models import Registration
from langchain_core.messages import HumanMessage
import re


def admin_agent(state):

    user_query = state.get("user_query", "").lower()

    db = SessionLocal()

    # detect reference ID
    match = re.search(r"dne-\d+", user_query)

    reference_id = match.group().upper() if match else None

    # approve
    if "approve" in user_query and reference_id:

        record = db.query(Registration).filter(
            Registration.reference_id == reference_id
        ).first()

        if record:
            record.status = "APPROVED"
            db.commit()

            state["response"] = f"✅ Registration {reference_id} has been APPROVED."

        else:
            state["response"] = "❌ Reference ID not found."

    # reject
    elif "reject" in user_query and reference_id:

        record = db.query(Registration).filter(
            Registration.reference_id == reference_id
        ).first()

        if record:
            record.status = "REJECTED"
            db.commit()

            state["response"] = f"❌ Registration {reference_id} has been REJECTED."

        else:
            state["response"] = "Reference ID not found."

    # show pending requests
    elif "pending" in user_query:

        records = db.query(Registration).filter(
            Registration.status == "PENDING"
        ).all()

        if not records:
            state["response"] = "No pending registrations."

        else:
            response = "Pending Requests:\n\n"

            for r in records:
                response += f"{r.reference_id} | {r.name} | {r.support_type}\n"

            state["response"] = response

    else:

        state["response"] = """
Admin Commands:

approve DNE-XXXX
reject DNE-XXXX
show pending requests
"""

    db.close()

    return state