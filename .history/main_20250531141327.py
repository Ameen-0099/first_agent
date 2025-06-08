import os 
import chainlit as cl
from agents import Agent,OpenAIChatCompletionsModel,Runner,AsyncOpenAI,RunConfig
from dotenv import load_dotenv,find_dotenv
from openai.types.responses import ResponseTextDeltaEvent
import asyncio

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

#step 1
provider = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#step 2

model = OpenAIChatCompletionsModel(
    model= "gemini-1.5-flash",
    openai_client=  provider,
    
)

#step 3
run_config = RunConfig(
    model = model,
    model_provider = provider,
    tracing_disabled = True
)

#step 4

agents = Agent(
    instructions="you are helpful assistant that can answer",
    name='Assistant',
    
    )

@cl.on_chat_start
async def handle_chat_start ():
    cl.user_session.set("history",[])
    await cl.Message(content="Hello!I am panaversity support Agent").send()


@cl.on_message
async def handle_message(message: cl.Message):
    
    history = cl.user_session.get("history")
    msg = cl.Message()
    
    
    history.append({"role": "user" , "content" :message.content})
    
    result = await Runner.run(
        agents,
        input = history,
        run_config = run_config
        )
    
    history.append({"role":"assistant","content":result.final_output})
    
    cl.user_session.set("history",history)
    await cl.Message(content=result.final_output).send()















# result = Runner.run_sync(
#     input="what is the capital of france",
#     run_config = run_config,
#     starting_agent = agents
# )

# print(result.final_output)

