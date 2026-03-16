from langchain.chat_models import ChatOpenAI

def summarize_research(text):

    llm = ChatOpenAI()

    prompt = f"Summarize this medical research: {text}"

    return llm.predict(prompt)