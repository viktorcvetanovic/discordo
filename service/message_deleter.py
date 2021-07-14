class MessageDeleter:

    def __init__(self, message, channel, client):
        self.message = message
        self.message_number = None
        self.channel = channel
        self.client = client

    async def get_message_number(self):
        def check(m):
            return m.channel == self.channel

        await self.channel.send('```Enter number of messages to delete```')
        self.message_number = int((await self.client.wait_for('message', check=check)).content)

    async def delete(self):
        await self.get_message_number()
        if self.message_number < 300:
            for msg in await self.message.channel.history(limit=self.message_number).flatten():
                await msg.delete()
        else:
            await self.channel.send('```Too big number limit is 300```')
