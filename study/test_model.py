import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="Qwen/Qwen3-32B:cerebras",
    messages=[
        {
            "role": "user",
            "content": "你好"
        }
    ],
)

print(completion.choices[0].message)