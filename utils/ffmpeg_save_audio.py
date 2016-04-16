# http://zulko.github.io/blog/2013/10/04/read-and-write-audio-files-in-python-using-ffmpeg/
# https://github.com/Zulko/moviepy/blob/master/moviepy/audio/io/ffmpeg_audiowriter.py

import numpy as np
import subprocess as sp
import os
DEVNULL = open(os.devnull, 'w')

def ffmpeg_save_audio(filename, y, sr=44100):
    # should allow bitrate argument
    # should allow stereo output
    pipe = sp.Popen([
        'ffmpeg',
        '-y', # (optional) means overwrite the output file if it already exists.
        '-f', 's16le', # means 16bit input
        '-acodec', 'pcm_s16le', # means raw 16bit input
        '-r', str(sr), # the input will have 44100 Hz
        '-ac','1', # the input will have 1 channels (mono)
        '-i', '-', # means that the input will arrive from the pipe
        '-vn', # means 'don't expect any video input'
        filename],
        stdin=sp.PIPE, stdout=DEVNULL, stderr=DEVNULL, bufsize=4096, close_fds=True)
    y16 = (y * np.iinfo(np.int16).max).astype(np.int16)
    pipe.stdin.write(y16.tostring())
    pipe.stdin.close()
    pipe.wait()