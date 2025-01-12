import os

import discord
import dotenv
from discord.ext import commands

bot = discord.Bot()
intents = discord.Intents.all()
intents.message_content = True
intents.messages = True
intents.guild_messages = True
bot = commands.Bot(command_prefix="a!", intents=intents)

# Server ID
guild_id = 815909997186777128

# Github token
dotenv.load_dotenv()
github_token = str(os.getenv("GITHUB_TOKEN"))