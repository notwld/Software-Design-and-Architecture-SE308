#observer deisgn pattern youtube example

class YouTubeChannel:
    def __init__(self):
        self.subscribers = []
        self.video = None

    def attach(self, subscriber):
        self.subscribers.append(subscriber)

    def detach(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def upload(self, video):
        self.video = video
        self.notify()

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self):
        print(f'{self.name} has been notified of a new video')

yt = YouTubeChannel()

s1 = Subscriber('Waleed')
s2 = Subscriber('Bajwa')
s3 = Subscriber('Farhan')
s4 = Subscriber('Huzzu')

yt.attach(s1)
yt.attach(s2)
yt.attach(s3)
yt.attach(s4)

yt.upload('Python Tutorial')

