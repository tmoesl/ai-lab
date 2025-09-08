from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Initialise Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)


# --------------------------------------------------------------
# Basic Chain [LangChain Expression Language (LCEL)]
# --------------------------------------------------------------
# Sequence of Runnables, where the output of each is the input of the next.

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful AI assistant."), ("human", "{input}")]
)

# Initialise chain
chain = prompt_template | model | StrOutputParser()

# Equivalent (see 2_chains_mechanism.py)
chain = RunnableSequence(first=prompt_template, middle=[model], last=StrOutputParser())

# Invoke the chain
response = chain.invoke({"input": "Tell me about artificial intelligence in one sentence"})

# Output
print(response)
