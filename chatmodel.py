from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


if "OPENAI_API_KEY" in os.environ:
    print('available')
    del os.environ["OPENAI_API_KEY"] 
load_dotenv()

# Set OPENAI_API_KEY as in .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(model='gpt-4', temperature=0.3, max_completion_tokens=100)

result = model.invoke("What is the capital of germany")

print(result.content)
