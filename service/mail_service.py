from discord import Message

from service.util import MailSender


class MailService:
    def __init__(self, message, client, channel):
        self.message = message
        self.client = client
        self.channel = channel

    async def send_mail(self):
        def check(m):
            return m.channel == self.channel

        await self.channel.send('```Type your mail:```')
        your_email: Message = await self.client.wait_for('message', check=check)
        await self.channel.send('```Type mail to send: ```')
        mail: Message = await  self.client.wait_for('message', check=check)
        await self.channel.send('```Type message: ```')
        mess: Message = await  self.client.wait_for('message', check=check)
        await self.channel.send(
            self.message.author.name + " have typed \n" + "Your email: " + your_email.content + "\n" + "To send email: " + mail.content + "\n" + "Message content: " + mess.content)
        sender = MailSender(your_email.content, mail.content, mess.content)
        return_code = sender.send()
        if return_code == 1:
            await self.message.self.channel.send('Sucessful mail send  ' + self.message.author.name)
        else:
            await self.message.self.channel.send('Error happend email didnt send ' + self.message.author.name)
