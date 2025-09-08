from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

# --------------------------------------------------------------
# Parallel Chains
# --------------------------------------------------------------
# RunnableParallel is a dict of runnables, returning a dict of their results.

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert research analyst."),
        ("human", "List the main findings of the paper titled: {paper_title}."),
    ]
)


# Define strengths analysis
def analyse_strengths_prompt(findings):
    strengths_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert research analyst."),
            (
                "human",
                "Given these findings: {findings}, list the study's main strengths in 100 words.",
            ),
        ]
    )
    return strengths_template.format_prompt(findings=findings)


# Define limitations analysis
def analyse_limitations_prompt(findings):
    limitations_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert research analyst."),
            (
                "human",
                "Given these findings: {findings}, list the study's key limitations in 100 words.",
            ),
        ]
    )
    return limitations_template.format_prompt(findings=findings)


# Define final analysis
# Input is a dict of strengths and limitations from RunnableParallel
def final_analysis(strengths, limitations):
    return f"Strengths:\n{strengths}\n\nLimitations:\n{limitations}"


# Initialise branches [LCEL]
strengths_branch_chain = (
    RunnableLambda(lambda x: analyse_strengths_prompt(x)) | model | StrOutputParser()
)
limitations_branch_chain = (
    RunnableLambda(lambda x: analyse_limitations_prompt(x)) | model | StrOutputParser()
)

# Initialise chain [LCEL]
chain = (
    prompt_template
    | model
    | StrOutputParser()
    | RunnableParallel(strengths=strengths_branch_chain, limitations=limitations_branch_chain)
    | RunnableLambda(lambda x: final_analysis(x["strengths"], x["limitations"]))
)

# Invoke the chain
result = chain.invoke({"paper_title": "Self-supervised learning for medical image classification"})
print(result)
