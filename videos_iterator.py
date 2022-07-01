class VideosIterator:
    def __init__(self, videos: list, video_factory):
        self._video_factory = video_factory
        self._index = 0
        self._videos = videos

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == len(self._videos):
            raise StopIteration

        self._index += 1
        return self[self._index - 1]

    def __getitem__(self, item):
        return self._video_factory.create(self._videos[item])
