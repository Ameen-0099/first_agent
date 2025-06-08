def main():
    print("uv")
    
if __name__ == "__main__":
    main()    
    
    


@cl.on_message
async def handle_message(message: cl.Message):
    await cl.Message(content="Hello! You said: " + message.content).send()
    