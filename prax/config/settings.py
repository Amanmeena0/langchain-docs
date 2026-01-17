import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

anthropic_api_key: Optional[str] = os.getenv("ANTHROPIC_API_KEY")


