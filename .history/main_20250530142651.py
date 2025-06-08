import chainlit as cl
from agents import Agent,OpenAIChatCompletionsModel,Runner
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

gemini





















def main():
    print("uv")
    
if __name__ == "__main__":
    main()    
    
    


@cl.on_message
async def handle_message(message: cl.Message):
    await cl.Message(content="Hello: " + message.content).send()
    