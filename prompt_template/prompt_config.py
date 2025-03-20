from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ChatMessage

prompt_template = ChatPromptTemplate([
    (SystemMessage("""You are a helpful {language} assistant.
    You need to answer the query with few {language} code examples in all possible senarios for the topic to cover the most of all senarios so the user should master in that topic.
    Please place the code in code block. to make it more readable. in website with streamlit
     """)),
    (HumanMessage("{query}"))
])

class PromptTemplateConfig:
    def __init__(self):
        self.prompt_template = prompt_template

    def get_prompt_template(self):
        return self.prompt_template