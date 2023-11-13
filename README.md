# langflow_chatglm
这是一篇介绍langflow集成chatglm的手册

# 先看效果
![image](https://github.com/liujichengs/langflow_chatglm/assets/18487488/9d16c1d7-ed37-4ade-ab30-41b8ffb46f34)


# 操作步骤
让langflow集成chatglm非常容易，

## 首先找到src/backend/langflow/components/llms这个目录
![image](https://github.com/liujichengs/langflow_chatglm/assets/18487488/c2295de9-3d46-4934-9c22-9615a7138526)


## 其次在目录下新增chatglm即可

```

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




```
