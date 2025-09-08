"""
This script explores message utilities and management in LangChain.
"""

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, trim_messages
from langchain_core.messages.utils import convert_to_openai_messages, count_tokens_approximately
from langchain_openai import ChatOpenAI
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Initialise Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# Sample conversation
conversation = [
    SystemMessage(content="You are a coding tutor"),
    HumanMessage(content="Explain Python variables"),
    AIMessage(content="Variables store data..."),
    HumanMessage(content="Can you give an example?"),
]

# --------------------------------------------------------------
# Message Conversion to OpenAI Format
# --------------------------------------------------------------

# Convert to OpenAI Format
openai_format = convert_to_openai_messages(conversation)
print(f"OpenAI Format: {openai_format}")

# Initialise OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Invoke Model
response = client.responses.create(
    model="gpt-4o-mini",
    temperature=0.5,
    input=openai_format,  # type: ignore
)
print("OpenAI Response:", response.output_text)

# --------------------------------------------------------------
# Message Token Counting [Approximately, LLM]
# --------------------------------------------------------------

# Count Tokens Approximately
approximate_token_count = count_tokens_approximately(conversation)

# Count Tokens
token_count = model.get_num_tokens_from_messages(conversation)

print(f"Approximate Token Count: {approximate_token_count}")
print(f"Token Count: {token_count}")

# --------------------------------------------------------------
# Message Trimming [Token Count, Message Count]
# --------------------------------------------------------------

# Trim by Token Count
trimmed_token_count = trim_messages(
    messages=conversation,
    strategy="last",
    token_counter=model,
    max_tokens=100,
    start_on="human",
    end_on=["human", "tool"],
    include_system=True,
    allow_partial=False,
)

# Trim by Message Count
trimmed_message_count = trim_messages(
    messages=conversation,
    strategy="last",
    token_counter=len,
    max_tokens=5,
    start_on="human",
    end_on=["human", "tool"],
    include_system=True,
    allow_partial=False,
)

print(f"Trimmed by Token Count: {trimmed_token_count}")
print(f"Trimmed by Message Count: {trimmed_message_count}")
