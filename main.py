from merger import VideoMerger
import sys
import os
from videos_iterator import VideosIterator
from cv2 import VideoCapture, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS
import logging


class Video:
    _video: VideoCapture

    def __init__(self, path: str):
        self._video = VideoCapture(path)

    def __iter__(self):
        return self

    def __next__(self):
        ret, frame = self._video.read()

        if ret:
            return frame
        else:
            self._video.release()
            raise StopIteration

    @property
    def width(self):
        return int(self._video.get(CAP_PROP_FRAME_WIDTH))

    @property
    def height(self):
        return int(self._video.get(CAP_PROP_FRAME_HEIGHT))

    @property
    def frame_rate(self):
        return self._video.get(CAP_PROP_FPS)


class VideoFactory:
    def create(self, path: str) -> Video:
        return Video(path)


logging.basicConfig(
    filename='merger.log',
    filemode='a',
    level=logging.INFO,
    format="{asctime} {levelname:<8} {message}",
    style="{"
)


if __name__ == '__main__':
    folders = sys.argv[1:]

    logging.info("Beginning merge")
    for folder in folders:
        merged_videos_path = os.path.join(folder, 'merged_video.mp4')

        try:
            if os.path.exists(merged_videos_path):
                logging.warning(f"A folder with name {merged_videos_path} already exists, deleting it.")
                os.remove(merged_videos_path)

            logging.info("Merging videos in", folder)

            folder = os.path.abspath(folder)
            videos = [os.path.join(folder, path) for path in sorted(os.listdir(folder)) if path.endswith('.mp4')]
            factory = VideoFactory()
            merger = VideoMerger(VideosIterator(videos, factory))
            merger.merge(merged_videos_path)
        except Exception as e:
            logging.error(f"Failed merging videos for folder {folder}: {e}")

    logging.info("Merge finished")
