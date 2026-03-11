from tools.survey_tools import get_tasks


def surveyor_agent(state):

    tasks = get_tasks()

    if not tasks:
        state["response"] = "No survey tasks assigned."
        return state

    text = "Survey Tasks:\n"

    for t in tasks:
        text += f"{t['donee']} - {t['location']} - {t['reference_id']}\n"

    state["response"] = text

    return state