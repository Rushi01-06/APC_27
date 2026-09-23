class Media:
    def play(self):
        pass

class Audio(Media):
    def play(self):
        return "Playing audio track..."

class Video(Media):
    def play(self):
        return "Playing video stream..."

class Podcast(Media):
    def play(self):
        return "Playing podcast episode..."

if __name__ == "__main__":
    media_items = [
        Audio(),
        Video(),
        Podcast()
    ]

    for item in media_items:
        print(item.play())
