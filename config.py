import discord
from discord.ext import commands

bot = discord.Bot()
intents = discord.Intents.all()
intents.message_content = True
intents.messages = True
intents.guild_messages = True
bot = commands.Bot(command_prefix="a!", intents=intents)