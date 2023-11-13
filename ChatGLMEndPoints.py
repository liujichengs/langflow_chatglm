from typing import Optional
from langflow import CustomComponent
from langchain.llms import ChatGLM
from langchain.llms.base import BaseLLM


class ChatGLMComponent(CustomComponent):
    display_name: str = "ChatGLM "
    description: str = "this is Custom ChatGLM ."

    def build_config(self):
        return {
            "endpoint_url": {
                "display_name": "endpoint_url",
                "options": [
                    "https://xxxxxxxxx/chat",
                  
                ],
            },
            "code": {"show": False},
        }

    def build(
        self,
        endpoint_url: str = "https://xxxxxxxxx/chat",
    ) -> BaseLLM:
        try:
            output = ChatGLM(
               endpoint_url=endpoint_url,
            )  # type: ignore
        except Exception as e:
            raise ValueError("Could not connect to ChatGLM URL.") from e
        return output
