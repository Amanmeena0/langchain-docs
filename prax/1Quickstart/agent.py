from langchain.agents.structured_output import ToolStrategy
from langchain.agents import create_agent
from .model import model
from .prompt import SYSTEM_PROMPT
from .format import ReponseFormat
from .tools import get_user_location, get_weather_for_location, Context
from .memory import checkpointer


agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location,get_weather_for_location],
    context_schema=Context, 
    reponse_format=ToolStrategy(ReponseFormat),
    checkpointer=checkpointer
)

config = {"configurable":{"thread_id":"1"}}

response = agent.invoke(
    {"messages": [{"role":"user", "content":"what is the weather outside?"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])

response = agent.invoke(
    {"message":[{"role":"user", "content":"thank you!"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])

