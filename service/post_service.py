import uuid

from discord import Message

from service.util import PostPicture


class PostPictureService:

    def __init__(self, channel, client):
        self.channel = channel
        self.client = client

    async def post(self):
        def check(m):
            return m.channel == self.channel

        await self.channel.send('Type you instagram username')
        username: Message = await self.client.wait_for('message', check=check)
        await self.channel.send('Type you instagram password')
        password: Message = await self.client.wait_for('message', check=check)
        await self.channel.send('Upload your picture')
        picture_path: Message = await self.client.wait_for('message', check=check)
        imageName = str(uuid.uuid4()) + '.jpg'
        await self.channel.message.attachments[0].save(imageName)
        caption: Message = await self.client.wait_for('message', check=check)
        await self.channel.send('We will upload picture now')
        post_picture = PostPicture()
        post_picture.login(username, password)
        post_picture.upload_pic(picture_path, caption)


