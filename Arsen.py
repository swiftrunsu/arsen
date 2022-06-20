import discord
from discord.ext import commands
import jishaku
import sqlite3
import asyncio

def get_prefix(bot, message):
    return commands.when_mentioned_or(".", "plz ", "hey ")(bot, message)

arsen = commands.Bot(
    intents=discord.Intents.all(),
    command_prefix = get_prefix,
    strip_after_prefix = True
)

@arsen.event
async def on_ready():
    print("online")
    await arsen.load_extension("cogs.economy")
    await arsen.load_extension("cogs.error_handler")
    await arsen.load_extension("jishaku")

arsen.help_command = commands.MinimalHelpCommand()

arsen.run("-")