import streamlit as st
from prompt_template import PromptTemplateConfig
from llm import LLMConfig
from util.logging_config import LoggerConfig


logger = LoggerConfig.setup_logging()

st.title("Any Coding Language Assistant with GENAI")

st.write("This is a Streamlit app that uses Hugging face reasoning model to generate responses to user queries.")

lang_list = ["Python", "C", "C++", "Java", "JavaScript", "R", "Swift", "Go", "TypeScript", "Kotlin", "Rust", "PHP", "SQL"]
lang = st.selectbox('Select Language', lang_list, disabled=False)
query = st.text_area('Enter your query')
generate_button = st.button('Generate Answer')

if lang and query and generate_button:
    st.write("Generating answer...")
    logger.info("Generating answer...")
    prompt_template = PromptTemplateConfig().get_prompt_template()
    llm = LLMConfig().get_llm()
    llm_chain = prompt_template | llm
    response = llm_chain.invoke({"language": lang, "query": query})
    st.write(response)
    logger.info("Answer generated successfully.")
    


