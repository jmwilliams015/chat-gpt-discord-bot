import discord
import openai
import os

discordToken = os.getenv('DISCORD_BOT_TOKEN')
openAIToken = os.getenv('OPEN_AI_API_KEY')

openai.api_key = openAIToken

try:
  openai.Completion.create(engine="text-davinci-002", prompt="Hello")
  print("API connection successful")
except Exception as e:
  print(f"Error: {e}")

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.guilds = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


async def on_message(message):
  print("Received Message!")
  if message.author == client.user:
    return

  if message.content.startswith("!chat"):
    print("Received !chat Prompt!")
    prompt = message.content[6:]
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=2048,
      n=1,
      stop=None,
      temperature=0.5,
    )
    await message.channel.send(response["choices"][0]["text"])

client.run(discordToken)