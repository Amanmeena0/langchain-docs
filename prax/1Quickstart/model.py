from prax.config.settings import anthropic_api_key
from google import genai
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "gemini-3-flash-preview",
    temperature=0.5,
    timeout=10,
    max_token=1000
)
