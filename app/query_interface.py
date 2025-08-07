from app.agent import get_agent

def ask_question(question):
    agent = get_agent()
    return agent.invoke({"input": question})

