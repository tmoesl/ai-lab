from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Sample Messages
message = "Hello, how are you?"

# --------------------------------------------------------------
# Chat Models - Model Configuration & Parameters
# --------------------------------------------------------------

settings = {
    "temperature": 0.5,
    "max_tokens": 100,
    "max_retries": 3,
    "top_p": 0.9,
}

# Initialise Model
model_openai = ChatOpenAI(model="gpt-4o-mini", **settings)

# Invoke Model
result_openai = model_openai.invoke(message)

print(f"OpenAI: {result_openai.content}")
