import disnake
from disnake.ext import commands
import asyncio
import os

intents = disnake.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Boosty developer: https://boosty.to/mao-mao")
    print("GitHub: https://github.com/rinnyuwu")
    print("Donation Alerts: https://www.donationalerts.com/r/rinnyuwu")

for root, dirs, files in os.walk('./cogs'):
    for file in files:
        if file.endswith('.py'):
            extension = os.path.join(root, file).replace('./', '').replace('/', '.').replace('\\', '.').removesuffix('.py')
            bot.load_extension(extension)

bot.run("INSERT-TOKEN") # To run the bot, you'll need a token which you get by creating an application in the Discord Developer Portal (https://discord.com/developers/)
                        # Replace INSERT-TOKEN with your token here
                        # Make sure the token remains confidential and is not published in public sources