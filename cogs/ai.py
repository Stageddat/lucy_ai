import discord
from discord.ext import commands
from datetime import datetime
from src.ai.embedGenerator import generate_embedding
from src.ai.aiResponse import genAiResponse
from src.ai.saveMessage import saveMessage


class ai_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if message.channel.id != 931840054526095370:
            return
        else:
            actual_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            author = message.author.name
            parse_message = f"[{actual_time}] {author}: {message.content.strip()}"
            embedded_message = generate_embedding(parse_message)

            answer = genAiResponse(parse_message, embedded_message)
            parse_answer = f"[{actual_time}] Lucy (You): {answer.strip()}"
            saveMessage(message=parse_message)
            saveMessage(message=parse_answer)
            await message.reply(f"{answer}")

            message_count = 0
            message_count += 2
            print(message_count)

    # @discord.slash_command(name = "add_info", description = "force x info")
    # async def test_welcome(self, ctx: discord.ApplicationContext, info: Option(discord.InputText, "sigma info")):# type: ignore
    #     await ctx.respond("Soon")

def setup(bot):
    bot.add_cog(ai_cog(bot))