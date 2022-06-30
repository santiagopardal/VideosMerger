import os
from video import Video


class VideosIterator:
    def __init__(self, path: str):
        self._index = 0
        self._files = [os.path.join(path, file) for file in os.listdir(path) if file.endswith('.mp4')]
        self._files.sort()

    def __iter__(self):
        return self

    def __next__(self):
        if self._index == len(self._files):
            raise StopIteration

        self._index += 1
        return Video(self._files[self._index - 1])

    def __getitem__(self, item):
        return Video(self._files[item])
