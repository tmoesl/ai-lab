"""
This script explores dynamic prompt templates with placeholders and partials.
"""

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Initialise Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# --------------------------------------------------------------
# Chat Prompt Templates [Dynamic Content with MessagesPlaceholder]
# --------------------------------------------------------------

# Basic Chat Template with Placeholder
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Continue the conversation naturally."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

# Simulate Chat History
chat_history = [
    HumanMessage("What is 5+5?"),
    AIMessage("5+5=10"),
    HumanMessage("What is 10+10?"),
    AIMessage("10+10=20"),
]

# Invoke Template
prompt = prompt_template.invoke(
    {"chat_history": chat_history, "input": "Add the previous values and multiply by 2"}
)

# Invoke Model
response = model.invoke(prompt)
print(f"Response: {response.content}")

# --------------------------------------------------------------
# Chat Prompt Templates [Partial Templates (Pre-filled values)]
# --------------------------------------------------------------

# Basic Chat Template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a translator. Translate from {source_lang} to {target_lang}."),
        ("human", "Translate: {text}"),
    ]
)

# Create Partial Template
spanish_prompt_template = prompt_template.partial(source_lang="English", target_lang="Spanish")
french_prompt_template = prompt_template.partial(source_lang="English", target_lang="French")

# Invoke Template
spanish_prompt = spanish_prompt_template.invoke({"text": "Hello, how are you?"})
french_prompt = french_prompt_template.invoke({"text": "Hello, how are you?"})

# Invoke Model
spanish_response = model.invoke(spanish_prompt)
french_response = model.invoke(french_prompt)

print(f"Spanish: {spanish_response.content}")
print(f"French: {french_response.content}")
