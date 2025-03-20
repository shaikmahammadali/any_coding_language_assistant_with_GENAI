from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os


class LLMConfig:
    def __init__(self):
        load_dotenv()
        self.llm = HuggingFaceEndpoint(repo_id="Qwen/QwQ-32B",
                                        task="text-generation")

        self.model = ChatHuggingFace(llm=self.llm)

    def get_model(self):
        return self.model

    def get_llm(self):
        return self.llm

    def get_huggingfacehub_api_token(self):
        return os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
        