# can we adda aframes to avoid reading more than necessary?
# what is the correct bufsize? do we need bufsize at all?
# what is the best chunk_size for reading data?
# could we ask ffmpeg to do type conversion for us?
# reference:
# http://git.numm.org/?p=numm.git;a=blob_plain;f=numm3/media.py;hb=refs/heads/numm3

import numpy as np
import subprocess as sp
import os
DEVNULL = open(os.devnull, 'w')

# load_audio can not detect the input type
def ffmpeg_load_audio(filename, sr=44100, mono=False, normalize=True, in_type=np.int16, out_type=np.float32):
    channels = 1 if mono else 2
    format_strings = {
        np.float64: 'f64le',
        np.float32: 'f32le',
        np.int16: 's16le',
        np.int32: 's32le',
        np.uint32: 'u32le'
    }
    format_string = format_strings[in_type]
    command = [
        'ffmpeg',
        '-i', filename,
        '-f', format_string,
        '-acodec', 'pcm_' + format_string,
        '-ar', str(sr),
        '-ac', str(channels),
        '-']
    p = sp.Popen(command, stdout=sp.PIPE, stderr=DEVNULL, bufsize=4096)
    bytes_per_sample = np.dtype(in_type).itemsize
    frame_size = bytes_per_sample * channels
    chunk_size = frame_size * sr # read in 1-second chunks
    raw = b''
    with p.stdout as stdout:
        while True:
            data = stdout.read(chunk_size)
            if data:
                raw += data
            else:
                break
    audio = np.fromstring(raw, dtype=in_type).astype(out_type)
    if issubclass(out_type, np.floating):
        if normalize:
            audio /= np.abs(audio).max()
        elif issubclass(in_type, np.integer):
            audio /= np.iinfo(in_type).max
    if channels > 1:
        audio = audio.reshape((-1, channels)).transpose()
    return audio, sr