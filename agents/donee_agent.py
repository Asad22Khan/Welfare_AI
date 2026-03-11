from tools.user_tools import get_status

def donee_agent(state):

    status = get_status(state["user_id"])

    state["response"] = f"Your application status: {status}"

    return state

from tools.user_tools import get_status


def donee_agent(state):

    ref = state.get("reference_id", None)

    if not ref:
        state["response"] = "Please provide your reference ID."
        return state

    result = get_status(ref)

    if not result:
        state["response"] = "No record found."
        return state

    state["response"] = f"""
Reference ID: {result['reference_id']}

Status: {result['status']}
"""

    return state