from langgraph.graph import StateGraph, END
from agents.router_agent import router_agent
from agents.registration_agent import registration_agent
from agents.donee_agent import donee_agent
from agents.donor_agent import donor_agent
from agents.surveyor_agent import surveyor_agent
from agents.admin_agent import admin_agent
from state.graph_state import GraphState
from persistence.checkpointer import checkpointer

builder = StateGraph(GraphState)

# ROUTER NODE
builder.add_node("router", router_agent)

# AGENT NODES
builder.add_node("registration_agent", registration_agent)
builder.add_node("donee_agent", donee_agent)
builder.add_node("donor_agent", donor_agent)
builder.add_node("surveyor_agent", surveyor_agent)
builder.add_node("admin_agent", admin_agent)

# ENTRY POINT
builder.set_entry_point("router")

# ROUTING LOGIC
builder.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "register": "registration_agent",
        "donee": "donee_agent",
        "donor": "donor_agent",
        "surveyor": "surveyor_agent",
        "admin": "admin_agent",
    }
)

# END AFTER AGENT RESPONSE
builder.add_edge("registration_agent", END)
builder.add_edge("donee_agent", END)
builder.add_edge("donor_agent", END)
builder.add_edge("surveyor_agent", END)
builder.add_edge("admin_agent", END)

app_graph = builder.compile(checkpointer=checkpointer)