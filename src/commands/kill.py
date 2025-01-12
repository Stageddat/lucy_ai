import discord
from config import bot
from src.embeds.noPermEmbed import no_perm_embed

@bot.slash_command(name="kill", description="ONLY USE IN URGENCY CASE")
async def kill(
    ctx: discord.ApplicationContext,
):
    await ctx.defer(ephemeral=True)
    if int(ctx.author.id) != 756509638169460837:
        await ctx.respond(embed=no_perm_embed, ephemeral=True)
        return
    await ctx.respond("Killing bot...", ephemeral=True)
    await bot.close()
