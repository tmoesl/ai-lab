from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Sample Messages
message = "Hello, how are you?"

# --------------------------------------------------------------
# Chat Models - Provider Specific Initialisation
# --------------------------------------------------------------

# Initialise Model
model_openai = ChatOpenAI(model="gpt-4o-mini")
model_anthropic = ChatAnthropic(model="claude-3-5-sonnet-20240620")  # type: ignore
model_google = ChatGoogleGenerativeAI(model="gemini-2.5-pro")

# Invoke Model
result_openai = model_openai.invoke(message)
result_anthropic = model_anthropic.invoke(message)
result_google = model_google.invoke(message)

print(f"OpenAI: {result_openai.content}")
print(f"Anthropic: {result_anthropic.content}")
print(f"Google: {result_google.content}")
