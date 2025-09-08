from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableBranch
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Example reviews
reviews = [
    "The product is excellent. I really enjoyed using it and found it very helpful.",
    "The product is terrible. It broke after just one use and the quality is very poor.",
    "The product is okay. It works as expected but nothing exceptional.",
    "I'm not sure about the product yet. Can you tell me more about its features and benefits?",
]

# --------------------------------------------------------------
# Branching Chains
# --------------------------------------------------------------
# RunnableBranch is a list of tuples (condition, Runnable)
# The RunnableBranch will run the first Runnable that satisfies the condition.

# Define prompt templates for different feedback types
positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a thank you note for this positive feedback: {feedback}."),
    ]
)

negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a response addressing this negative feedback: {feedback}."),
    ]
)

neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a request for more details for this neutral feedback: {feedback}."),
    ]
)

escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Generate a message to escalate this feedback to a human agent: {feedback}."),
    ]
)

# Define the feedback classification template
classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}.",
        ),
    ]
)

# Define the runnable branches for handling feedback [conditional logic]
branches = RunnableBranch(
    (
        lambda x: "positive" in x.lower(),
        positive_feedback_template | model | StrOutputParser(),  # Positive feedback chain
    ),
    (
        lambda x: "negative" in x.lower(),
        negative_feedback_template | model | StrOutputParser(),  # Negative feedback chain
    ),
    (
        lambda x: "neutral" in x.lower(),
        neutral_feedback_template | model | StrOutputParser(),  # Neutral feedback chain
    ),
    escalate_feedback_template | model | StrOutputParser(),  # default branch
)

# Initialise classification chain [LCEL]
classification_chain = classification_template | model | StrOutputParser()

# Initialise the complete chain [LCEL]
chain = classification_chain | branches

# Invoke the chain
for review in reviews:
    result = chain.invoke({"feedback": review})
    print(result)
