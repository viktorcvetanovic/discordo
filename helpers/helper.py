from service import MailService, MessageDeleter
from service.post_service import PostPictureService


def print_all_commands():
    s = ""
    for i in Helper.commands:
        s += i + "\n"
    return s


class Helper:
    commands = ['.sendmail', '.commands', '.postpicture', '.c']

    def __init__(self, message, client):
        self.message = message
        self.client = client

    async def check_message(self):
        if self.message.author == self.client.user:
            return

        if self.message.content.startswith(Helper.commands[0]):
            channel = self.message.channel
            service = MailService(self.message, self.client, channel)
            await service.send_mail()

        elif self.message.content.startswith(self.commands[1]):
            await self.message.channel.send(print_all_commands())

        elif self.message.content.startswith(self.commands[2]):
            channel = self.message.channel
            post_picture = PostPictureService(channel, self.client)
            await  post_picture.post()
        elif self.message.content.startswith(self.commands[3]):
            channel = self.message.channel
            message_deleter = MessageDeleter(self.message, channel, self.client)
            await message_deleter.delete()
