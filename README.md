# VideosMerger
Videos Merger is a very simple and extensible tool and module to merge videos in a certain folder.

## Requirements
The only requirement is OpenCV.

## Installation
You just need to install the aforementioned requirements:
```bash
pip install -r requirements.txt
```

## How to use
Inside the project's directory just run:
```bash
python3 main.py /path/to/the/folder/to/merge/videos
```
This will create a new video named `merged_video.mp4` inside the folder you've provided, in the example above, you'd find a file `/path/to/the/folder/to/merge/videos/merged_video.mp4`

## How to extend and use as a module
In order to use as a module, add it as a git submodule in your project.

You will use the class `VideoMerger` to which you'll pass a `VideoIterator` which is in charge of iterating **in order** through all the videos you want to merge and returning a `Video` object which you can also extend, implementing your own logic.

The class `VideoIterator` will create each video using a `VideoFactory` you must inject in construction, this class can also be extended.
