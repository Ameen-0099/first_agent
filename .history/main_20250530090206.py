from dotenv import load_dotenv     #acces throgh api and save api key
import os
from  agents import Agent,OpenAIChatCompletionsModel,RunConfig,AsyncOpenAI,Runner

load_dotenv()
gemini_api_key =os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)



agents = Agent(name="Assistant",instructions="")


res = Runner.run_sync(agents,input="who was the founder of pakistan",)
print(res)