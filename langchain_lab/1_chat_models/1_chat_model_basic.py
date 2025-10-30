# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables from .env
load_dotenv()

# Sample Messages
message = "Hello, how are you?"

# --------------------------------------------------------------
# Chat Models - Basic Initialisation
# --------------------------------------------------------------

# Initialise Model
model_openai = init_chat_model(model="gpt-4o-mini", model_provider="openai")
model_anthropic = init_chat_model(model="claude-3-5-haiku-latest", model_provider="anthropic")
model_google = init_chat_model(model="gemini-2.5-pro", model_provider="google_genai")

# Invoke Model
print(f"GPT-4o-mini: {model_openai.invoke(message).content}")
print(f"Claude-3-5-haiku: {model_anthropic.invoke(message).content}")
print(f"Gemini-2.5-pro: {model_google.invoke(message).content}")


# --------------------------------------------------------------
# Chat Models - Configurable Initialisation
# --------------------------------------------------------------

# Initialise Model
model_configurable = init_chat_model(
    model="gpt-4o-mini", configurable_fields=("model", "model_provider")
)

# Invoke Model
result_configurable = model_configurable.invoke(
    input=message,
    config={"model": "claude-3-5-haiku-latest", "model_provider": "anthropic"},  # type: ignore
)
print(f"Claude-3-5-haiku: {result_configurable.content}")
