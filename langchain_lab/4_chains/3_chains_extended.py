from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# --------------------------------------------------------------
# Extended Chains
# --------------------------------------------------------------

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful AI assistant."), ("human", "{input}")]
)

# Add additional processing steps [RunnableLambda]
lowercase_output = RunnableLambda(lambda x: x.lower())
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")

# Initialise chain
chain = prompt_template | model | StrOutputParser() | lowercase_output | count_words

# Invoke the chain
result = chain.invoke({"input": "Tell me about artificial intelligence in one sentence"})

# Output
print(result)
