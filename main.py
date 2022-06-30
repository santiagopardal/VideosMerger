import time
from merger import VideoMerger
import sys
import os
from video import Video
from videos_iterator import VideosIterator


if __name__ == '__main__':
    folders = sys.argv[1:]
    for folder in folders:
        merged_videos_path = os.path.join(folder, 'merged_video.mp4')

        if os.path.exists(merged_videos_path):
            os.remove(merged_videos_path)

        print("Merging videos in", folder)
        folder = os.path.abspath(folder)
        #videos = [Video(os.path.join(folder, path)) for path in sorted(os.listdir(folder)) if path.endswith('.mp4')]
        merger = VideoMerger(VideosIterator(folder))
        merger.merge(merged_videos_path)
