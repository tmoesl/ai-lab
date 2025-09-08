"""
This script explores prompt composition and chaining in LangChain.
"""

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Initialise Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# Sample text
text_to_summarize = "Artificial intelligence is transforming the world. \
It's being used in healthcare, finance, and education to solve complex \
problems and improve efficiency."

# --------------------------------------------------------------
# Chat Prompt Templates [Prompt Composition and Chaining]
# --------------------------------------------------------------

# Initialise Templates [Summarizer]
summarizer_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert summarizer. Create concise summaries."),
        ("human", "Summarize this text in 2-3 sentences:\n\n{text}"),
    ]
)

# Initialise Templates [Translator]
translator_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a professional translator."),
        ("human", "Translate this text to {target_language}:\n\n{text}"),
    ]
)

# Step 1: Summarize [Invoke Template and Model]
summary_prompt = summarizer_prompt_template.invoke({"text": text_to_summarize})
summary_result = model.invoke(summary_prompt)
print(f"Summary: {summary_result.content}")

# Step 2: Translate [Invoke Template and Model]
translation_prompt = translator_prompt_template.invoke(
    {"text": summary_result.content, "target_language": "French"}
)
translation_result = model.invoke(translation_prompt)
print(f"Translation: {translation_result.content}")
