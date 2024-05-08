class Settings:
    def __init__(self):
        self.DATABASE_URI = "sqlite+aiosqlite:///db.sqlite3"
        self.VOICE_PATH = "content/voice/"
        self.PHOTO_PATH = "content/photo/"
        self.VIDEO_PATH = "content/video/"

settings = Settings()