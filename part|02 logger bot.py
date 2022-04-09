import discord
from discord.ext import commands


client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("started")

@client.event
async def on_message(message):
    if message == "":
        return
    else:
        id = str(message.author)
        time = str(message.created_at.strftime("%d-%m-%Y %H:%M:%S"))
        mss = str(message.content)

        data = open("data.txt","a")
        data.write(f"({time}) {id} : {mss}\n")
    
client.run("Your Token")
