"""
This script explores few-shot prompt templates in LangChain.
"""

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.prompts.few_shot import FewShotChatMessagePromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Initialise Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# --------------------------------------------------------------
# Few-Shot Prompt Templates [String-Based]
# --------------------------------------------------------------

# Example Data
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "fast", "output": "slow"},
    {"input": "hot", "output": "cold"},
]

prompt_template = PromptTemplate.from_template("Input: {input}\nOutput: {output}")

# Few-Shot Template
few_shot_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_template,
    prefix="Translate the following words to their opposites:",
    suffix="Input: {input}\nOutput:",
    input_variables=["input"],
)

# Format Template
prompt = few_shot_template.format(input="big")  # -> [String]

# Invoke Model
result = model.invoke(prompt)
print(f"Few-Shot Response: {result.content}")

# --------------------------------------------------------------
# Few-Shot Chat Message Templates [Message-Based]
# --------------------------------------------------------------

# Example Data
examples = [
    {"input": "I love this product!", "output": "positive"},
    {"input": "This is terrible quality", "output": "negative"},
    {"input": "It's okay, nothing special", "output": "neutral"},
    {"input": "Amazing! Best purchase ever!", "output": "positive"},
]

prompt_template = ChatPromptTemplate.from_messages([("human", "{input}"), ("ai", "{output}")])

# Few-Shot Chat Template
few_shot_template = FewShotChatMessagePromptTemplate(
    examples=examples, example_prompt=prompt_template
)

# Full Chat Template
chat_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a sentiment classifier. Classify text as positive, negative, or neutral.",
        ),
        few_shot_template,
        ("human", "{input}"),
    ]
)

# Invoke Template
prompt = chat_template.invoke({"input": "This product exceeded my expectations!"})
print("Prompt messages:")
print(prompt.to_messages())

# Invoke Model
response = model.invoke(prompt)
print(f"Few-Shot Chat Response: {response.content}")
