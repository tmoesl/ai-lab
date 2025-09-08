# Prompt Template Docs:
#   https://python.langchain.com/v0.2/docs/concepts/#prompt-templates

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Initialise Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# --------------------------------------------------------------
# Basic Prompt Templates
# --------------------------------------------------------------

# Initialise Template
prompt_template = PromptTemplate.from_template("Hello {name}, tell me a joke about {topic}.")

# Invoke Template
prompt = prompt_template.invoke({"name": "Alice", "topic": "cats"})
print(f"Basic Prompt Template: {prompt}")


# --------------------------------------------------------------
# Chat Prompt Templates [Tuple-Based]
# --------------------------------------------------------------

# Initialise Template [Multiple Placeholders]
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Tell me a {adjective} story about a {animal}."),
    ]
)

# Invoke Template
prompt = prompt_template.invoke({"adjective": "funny", "animal": "panda"})
print(f"Chat Prompt Template: {prompt}")


# --------------------------------------------------------------
# Chat Prompt Templates [Mixed Message Types]
# --------------------------------------------------------------
# Note: HumanMessage can't have variables - already parsed

# Initialise Template [Mixed Message Types]
messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    HumanMessage(content="Tell me 3 jokes."),
]

# Invoke Template
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic": "lawyers"})
print(f"Chat Prompt Template: {prompt}")


# --------------------------------------------------------------
# Example: Using Templates with a Chat Model
# --------------------------------------------------------------
# Note: Using the template from the previous example

# Initialise Template
prompt = prompt_template.invoke({"topic": "lawyers"})
result = model.invoke(prompt)
print(f"Response: {result.content}")
