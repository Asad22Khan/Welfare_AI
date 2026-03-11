from fastapi import FastAPI
from graph.welfare_graph import app_graph

app = FastAPI()


@app.post("/chat")
def chat(message: str, thread_id: str):

    response_text = None

    for event in app_graph.stream(
        {"user_query": message},
        config={"configurable": {"thread_id": thread_id}}
    ):

        for node_output in event.values():

            if isinstance(node_output, dict):
                response_text = node_output.get("response", response_text)

    return {
        "response": response_text or "No response generated"
    }