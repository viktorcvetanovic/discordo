import discord

client = discord.Client()

commands = ['#dajpicke', '#dajkurac', '#cao']
channel = client.get_channel(12324234183172)


def printcommands():
    s = ""
    for i in commands:
        s += i + "\n"
    return s


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# @client.event
# async def on_member_join(member):
#     await member.send(member + " se pridruzio kanalu")
#     await channel.send(member + " se pridruzio kanalu")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('#dajpicke'):
        await message.channel.send('Evo ti picke ' + message.author.name)
    if message.content.startswith('#dajkurac'):
        await message.channel.send('Evo ti kurac ' + message.author.name)
    if message.content.startswith('#cao'):
        await message.channel.send('Cao ' + message.author.name)
    if message.content.startswith('#komande'):
        await message.channel.send(printcommands())


client.run('')
