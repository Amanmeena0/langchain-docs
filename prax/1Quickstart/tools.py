from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime

@tool 
def get_weather_for_location(city:str)-> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

@dataclass
class context:
    """Custom runtime context schema."""

    used_id:str

@tool 
def get_user_location(runtime: ToolRuntime[context])->str:
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "SF"
