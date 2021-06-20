from instabot import Bot


class PostPicture:

    def __init__(self):
        self.bot = Bot()

    def login(self, username, password):
        self.bot.login(username=username, password=password)

    def upload_pic(self, picture_path, caption):
        self.bot.upload_photo(picture_path,
                              caption=caption)
