from service import MailService


def print_all_commands():
    s = ""
    for i in Helper.commands:
        s += i + "\n"
    return s


class Helper:
    commands = ['#sendmail', '#commands']

    def __init__(self, message, client):
        self.message = message
        self.client = client

    async def check_message(self):
        if self.message.author == self.client.user:
            return

        if self.message.content.startswith(Helper.commands[0]):
            channel = self.message.channel
            service = MailService(self.message, self.client, channel)
            service.callMail()

        elif self.message.content.startswith(self.commands[1]):
            await self.message.channel.send(print_all_commands())
