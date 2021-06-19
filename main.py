import discord
from config import bot_code
from helper.helper import Helper

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    helper = Helper(message, client)
    helper.check_message()


client.run(bot_code.bot_code)
