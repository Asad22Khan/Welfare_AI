from tools.donation_tools import browse_donees

def donor_agent(state):

    donees = browse_donees()

    state["response"] = str(donees)

    return state