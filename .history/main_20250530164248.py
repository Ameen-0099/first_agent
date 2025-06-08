import chainlit as cl
import os 
from agents import Agent,OpenAIChatCompletionsModel,Runner,AsyncOpenAI,RunConfig
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

modal = OpenAIChatCompletionsModel(
    modal= "gemini-20-flash",
    provider = provider
    
)

run_config = RunConfig(
    modal = modal
    modal_provider = provider
    tracing_disabled = True
)


agents = Agent(
    
) 

















def main():
    print("uv")
    
if __name__ == "__main__":
    main()    
    
    


@cl.on_message
async def handle_message(message: cl.Message):
    await cl.Message(content="Hello: " + message.content).send()
    