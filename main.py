import discord, os, keep_alive

from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)

@client.event
async def on_connect():
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="Amelia's stream 'till I'm offline."))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

client.run("TOKEN HERE", bot=False)
