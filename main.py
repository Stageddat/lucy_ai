import os
import traceback

import discord
import dotenv

from config import bot
from src.embeds.noPermEmbed import no_perm_embed
import src.commands.kill  # noqa: F401

cogs = ["cogs.ai"]

for cog in cogs:
    try:
        bot.load_extension(cog)
        print(f'Cog loaded "{cog}"')
    except Exception as e:
        print(f'Error loading cog: "{cog}": {e}')
        traceback.print_exc()

@bot.event
async def on_ready():
    print(f"{bot.user} is cool!")
    await bot.change_presence(activity=discord.Streaming(name="sigma videos!", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))


async def get_cog_names(ctx: discord.AutocompleteContext):
    name = ctx.options["name"]
    return [cog for cog in cogs if name.lower() in cog.lower()]


@bot.slash_command(name="reload_cog", description="Reload a specific cog")
async def reload_cog(
    ctx: discord.ApplicationContext,
    name: discord.Option(str, "Cog name to reload", autocomplete=get_cog_names),  # type: ignore
):
    if int(ctx.author.id) != 756509638169460837:
        if name.lower() in cogs:
            try:
                bot.reload_extension(name.lower())
                await ctx.respond(f'Cog "{name}" reloaded correctly')
            except Exception:
                await ctx.respond(f'Failed to reload cog "{name}"')
            return
        await ctx.respond(f'I can"t find "{name}" :c')
    else:
        await ctx.respond("You are not allowed to use this")

@bot.slash_command(name="version", description="View bot version")
async def version(
    ctx: discord.ApplicationContext,
):
    await ctx.defer(ephemeral=True)
    if int(ctx.author.id) != 756509638169460837:
        await ctx.respond(embed=no_perm_embed, ephemeral=True)
        return

    await ctx.respond(
        f"V.1.0.\nPing: `{round(bot.latency * 1000, 2)}`ms", ephemeral=True
    )

dotenv.load_dotenv()
token = str(os.getenv("DISCORD_TOKEN"))
bot.run(token)
