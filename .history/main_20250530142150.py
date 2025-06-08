def main():
    print("uv")
    
if __name__ == "__main__":
    main()    
    
    
import chainlit as cl

@cl.on_message
async def handle_message(message: cl.Message):
    await cl.Message(content="Hello! You said: " + message.content).send()
    