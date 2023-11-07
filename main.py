from merger import VideoMerger
import sys
import os
from videos_iterator import VideosIterator
import logging
from video_factory import VideoFactory


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
