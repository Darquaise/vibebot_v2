import discord
from discord.ext import bridge

intents = discord.Intents.all()
bot = bridge.Bot(command_prefix="!", help_command=None, debug_guilds=[576380164250927124], intents=intents)


with open("token", "r") as f:
    token = f.read()


bot.run(token=token)
