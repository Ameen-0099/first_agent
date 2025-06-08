# import os 
# import chainlit as cl
# from agents import Agent,OpenAIChatCompletionsModel,Runner,AsyncOpenAI,RunConfig
# from dotenv import load_dotenv,find_dotenv
# from openai.types.responses import ResponseTextDeltaEvent
# import asyncio

# load_dotenv(find_dotenv())

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# #step 1
# provider = AsyncOpenAI(
#     api_key= gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# #step 2

# model = OpenAIChatCompletionsModel(
#     model= "gemini-1.5-flash",
#     openai_client=  provider,
    
# )

# #step 3
# run_config = RunConfig(
#     model = model,
#     model_provider = provider,
#     tracing_disabled = True
# )

# #step 4

# agents = Agent(
#     instructions="you are helpful assistant that can answer",
#     name='Assistant',
    
#     )


# @cl.on_chat_start
# async def handle_chat_start ():
#     cl.user_session.set("history",[])
#     await cl.Message(content="Hello!I am panaversity support Agent").send()


# @cl.on_message
# async def handle_message(message: cl.Message):
    
#     history = cl.user_session.get("history")
#     history.append({"role": "user" , "content" :message.content})
    
#     result = await Runner.run(
#         agents,
#         input = history,
#         run_config = run_config
#         )
    
#     history.append({"role":"assistant","content":result.final_output})
    
#     cl.user_session.set("history",history)
#     await cl.Message(content=result.final_output).send()




import os
import chainlit as cl
from agents import Agent, OpenAIChatCompletionsModel, Runner, AsyncOpenAI, RunConfig
from dotenv import load_dotenv, find_dotenv
from openai.types.chat import ChatCompletionChunk

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Step 1: Setup provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Step 2: Setup model
model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=provider
)

# Step 3: Run configuration
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

# Step 4: Create agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant that can answer questions."
)

# Chat start event
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello! I am Panaversity support agent.").send()

# Handle incoming messages with streaming
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")
    history.append({"role": "user", "content": message.content})

    # Start streaming response
    msg = cl.Message(content="")
    await msg.send()

    result = await Runner.run_streamed(agent, input=history, run_config=run_config)

    full_response = ""

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ChatCompletionChunk):
            delta = event.data.choices[0].delta.content or ""
            full_response += delta
            await msg.stream_token(delta)

    # Save response in history
    history.append({"role": "assistant", "content": full_response})
    cl.user_session.set("history", history)

    # Finalize the message (optional)
    await msg.update()










# result = Runner.run_sync(
#     input="what is the capital of france",
#     run_config = run_config,
#     starting_agent = agents
# )

# print(result.final_output)

