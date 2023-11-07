from video import Video


class VideoFactory:
    def create(self, path: str) -> Video:
        return Video(path)
