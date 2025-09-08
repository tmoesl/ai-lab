"""
This script explores the basic message types in LangChain.
"""

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Initialise Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# --------------------------------------------------------------
# Single User Message
# --------------------------------------------------------------

human_message = HumanMessage(content="Hello, how are you?")

# Invoke Model
response = model.invoke([human_message])
print(f"Response: {response.content}")

# --------------------------------------------------------------
# System and User Message
# --------------------------------------------------------------

system_message = SystemMessage(content="You are a helpful assistant. You only answer in Spanish.")
human_message = HumanMessage(content="Hello, how are you?")

# Invoke Model
response = model.invoke([system_message, human_message])
print(f"Response: {response.content}")

# --------------------------------------------------------------
# Conversation Messages
# --------------------------------------------------------------

conversation = [
    SystemMessage(content="You are a coding tutor"),
    HumanMessage(content="Explain Python variables"),
    AIMessage(content="Variables store data..."),
    HumanMessage(content="Can you give an example?"),
]

# Invoke Model
response = model.invoke(conversation)
print(f"Response: {response.content}")
