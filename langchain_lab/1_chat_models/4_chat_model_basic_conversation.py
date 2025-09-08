from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Initialise Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# --------------------------------------------------------------
# Chat Models - Message-Based Invocation
# --------------------------------------------------------------

# Create Messages
messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="Tell me about artificial intelligence in 100 words"),
]

# Invoke Model
result = model.invoke(messages)
print(f"Response: {result.content}")

# --------------------------------------------------------------
# Chat Models - Streaming Invocation
# --------------------------------------------------------------

# Initialise Model with Streaming
streaming_model = ChatOpenAI(model="gpt-4o-mini", streaming=True)

# Invoke Model
for chunk in streaming_model.stream(messages):
    if chunk.content:
        print(f"Response: {chunk.content}", end="", flush=True)
