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
gpt_4o_mini = init_chat_model(model="gpt-4o-mini", model_provider="openai")
claude_3_5_sonnet = init_chat_model(model="claude-3-5-sonnet-20240620", model_provider="anthropic")
gemini_2_5_pro = init_chat_model(model="gemini-2.5-pro", model_provider="google_genai")

# Invoke Model
print(f"GPT-4o-mini: {gpt_4o_mini.invoke(message).content}")
print(f"Claude-3-5-sonnet: {claude_3_5_sonnet.invoke(message).content}")
print(f"Gemini-2.5-pro: {gemini_2_5_pro.invoke(message).content}")


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
    config={"model": "claude-3-5-sonnet-20240620", "model_provider": "anthropic"},  # type: ignore
)
print(f"Claude-3-5-sonnet: {result_configurable.content}")
