from dataclasses import dataclass

@dataclass
class ReponseFormat:
    """Reponse schema for the agent."""
    punny_response: str

    weather_conditions: str | None = None