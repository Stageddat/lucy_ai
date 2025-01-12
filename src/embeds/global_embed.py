from config import discord

no_perm_embed = discord.Embed(
    title="",
    description="You are not allowed to use this!",
    colour=discord.Colour(int("ff0000", 16))
)

soon_embed = discord.Embed(
    title="Soon!",
    description="This command/feature is not available for now. Try again later!",
    colour=discord.Colour(int("ff0000", 16))
)

error_embed = discord.Embed(
    title="Something failed :c",
    description="Please, contact <@756509638169460837> or any moderator/administrator.",
    colour=discord.Colour(int("ff0000", 16))
)

failed_fetch_daily_channel = discord.Embed(
    title="Daily fact channel log not found!",
    description="Failed log mod action becouse daily fact log channel not found",
    colour=discord.Colour(int("ff0000", 16))
)

ticket_ban_embed = discord.Embed(
    title="You are banned!",
    description="Sorry, you are banned from ticket.",
    colour=discord.Colour(int("ff0000", 16))
)

claimed_ticket_embed = discord.Embed(
    title="This ticket is claimed!",
    description="Sorry, only people who have claimed the ticket can close.",
    colour=discord.Colour(int("ff0000", 16))
)