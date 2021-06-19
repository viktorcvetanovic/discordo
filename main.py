import discord
from discord import Message

import bot_code
from mail_sender import MailSender

client = discord.Client()

commands = ['#sendmail', '#commands']


def printcommands():
    s = ""
    for i in commands:
        s += i + "\n"
    return s


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(commands[0]):
        channel = message.channel
        await channel.send('Type your mail:')

        def check(m):
            return m.channel == channel

        your_email: Message = await client.wait_for('message', check=check)
        await channel.send('Type mail to send:')
        mail: Message = await  client.wait_for('message', check=check)
        await channel.send('Type message:')
        mess: Message = await  client.wait_for('message', check=check)
        await  channel.send(
            message.author.name + " have typed \n" + "Your email: "+your_email.content + "\n" +"To send email: "+ mail.content + "\n" + "Message content: "+mess.content)
        sender = MailSender(your_email.content, mail.content, mess.content)
        return_code = sender.send_mail()
        if return_code == 1:
            await message.channel.send('Sucessful mail send  ' + message.author.name)
        else:
            await message.channel.send('Error happend email didnt send ' + message.author.name)

    elif message.content.startswith(commands[1]):
        await message.channel.send(printcommands())


client.run(bot_code.bot_code)
