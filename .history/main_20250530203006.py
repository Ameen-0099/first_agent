import os 
import chainlit as cl
from agents import Agent,OpenAIChatCompletionsModel,Runner,AsyncOpenAI,RunConfig
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

#step 1
provider = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

#step 2

model = OpenAIChatCompletionsModel(
    model= "gemini-2.0-flash",
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
    instructions="you are helpful assistant that can answer ",
    name='Assistant ',
) 

# result = Runner.run_sync(
#     input="what is the capital of france",
#     run_config = run_config,
#     starting_agent = agents
# )

# print(result.final_output)

@cl.on_chat_start
async def handle_chat_start ():
    cl.user_session.set("history",[])
    await cl.Message(content=f"Hello!I am panaversity support Agent")

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user
   result = await Runner.run(
    agents,   
    input = message.content,
    run_config = run_config,
   )
   await cl.Message(content=result.final_output).send()
    