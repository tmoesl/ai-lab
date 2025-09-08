"""
This script explores a basic conversational loop using a chat model.
"""

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage, trim_messages
from langchain_openai import ChatOpenAI

# Load environment variables from .env
load_dotenv()

# Initialise Model
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# --------------------------------------------------------------
# 1. Simple Chat Session (Basic Conversational Loop)
# --------------------------------------------------------------


def simple_chat_session():
    """Practice function combining models and messages"""

    # Create a list to store the conversation history (in-memory)
    chat_history: list[BaseMessage] = []

    # Initialize conversation with system message
    system_message = SystemMessage(
        content="You are a helpful AI assistant. Keep responses concise."
    )
    chat_history.append(system_message)

    print("------------- Simple Chat Session -------------")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ("exit", "quit", "q"):
            print("------------- Exiting Chat Session ------------")
            break

        # Add user message
        chat_history.append(HumanMessage(content=user_input))  # type: ignore

        # Get AI response
        response = model.invoke(chat_history)
        print(f"User: {user_input}")
        print(f"AI: {response.content}")

        # Add AI message to conversation
        chat_history.append(response)  # type: ignore

        # Trim if getting too long
        if len(chat_history) > 10:
            chat_history = trim_messages(
                messages=chat_history,
                strategy="last",
                token_counter=len,
                max_tokens=8,
                include_system=True,
            )


# Run the practice session
simple_chat_session()
