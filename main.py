import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("I'm Alive")

@client.command()
async def hi(ctx):
    await ctx.send("Hello World")

client.run("Your token")
