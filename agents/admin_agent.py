from tools.user_tools import get_pending_users

def admin_agent(state):

    pending = get_pending_users()

    state["response"] = str(pending)

    return state

from tools.user_tools import get_pending_users


def admin_agent(state):

    users = get_pending_users()

    if not users:
        state["response"] = "No pending registrations."
        return state

    text = "Pending Users:\n"

    for u in users:
        text += f"{u['name']} - {u['reference_id']}\n"

    state["response"] = text

    return state