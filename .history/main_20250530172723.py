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
    open = provider,
    
)

#step 3
run_config = RunConfig(
    model = model,
    model_provider = provider,
    tracing_disabled = True
)

#step 4
agents = Agent(
    instructions="you are the helpful Assistant that can answer question",
    name='Assistant',
) 

result = Runner.run_sync(
    input="who is founder of pakistan",
    run_config = run_config,
    starting_agent = agents
    
)
print(result)

# def main():
#     print("uv")
    
# if __name__ == "__main__":
#     main()    
    
    
@cl.on_message
async def handle_message(message: cl.Message):
    await cl.Message(content="Hello: " + message.content).send()
    