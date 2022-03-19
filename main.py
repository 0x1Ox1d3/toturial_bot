import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("I'm Alive")

@client.command()
async def hi(ctx):
    await ctx.send("Hello World")

client.run("OTU0NTU2NzUwNzIyNDAwMzI2.YjU2QA.u7gPkkOYrUdeZ9Z3Q46BjxiMyQA")
