from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# --------------------------------------------------------------
# Chain of Runnables [Under the Hood]
# --------------------------------------------------------------
# Sequence of Runnables, where the output of each is the input of the next.
# RunnableLambda converts a python callable into a Runnable.

# Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful AI assistant."), ("human", "{input}")]
)

# Create individual runnables (steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

# Create the RunnableSequence (equivalent to the LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Invoke the chain
response = chain.invoke({"input": "Tell me about artificial intelligence in one sentence"})

# Output
print(response)
