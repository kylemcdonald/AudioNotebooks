# AudioNotebooks

A collection of Jupyter Notebooks related to audio processing.

The notebooks act like interactive utility scripts for converting between different representations, usually stored in `data/project/` where `project` is the dataset you're working with. Generally, if you change `data_root` near the top of the notebook and run the reset of the notebook, it will do something useful.

* _Multisamples_ refers to audio that needs to be segmented into samples.
* _Samples_ refers to one-shot sounds, usually less than 1-2 seconds long. These can be loaded from a directory, like `data/project/samples/` or from a precomputed numpy matrix like `data/project/samples.npy`. When they are stored in a `.npy` file, all the samples are necessarily concatenated or expanded to be the same length.
* _Fingerprints_ refer to small images, usually 32x32 pixels, representing a small chunk of time like 250ms or 500ms. Sometimes these are calculated with CQT or STFT, but they are useful for running t-SNE or training neural nets.

Some common formats:

* `.npy` are numpy matrices. Numpy can load and save these very quickly, even for large datasets.
* `.tsv` are tab separated files referring to one sample per line, usally with normalized numbers in each column. These are good for loading into openFrameworks apps, or into the browser.
* `.txt` are like `.tsv` but only have one item per line, usually a single string. Also good for loading into openFrameworks apps, or into the browser.
* `.pkl` are Pickle files, which is the native Python serialization format, and is used for saving and loading datastructures that have lists of objects with lots of different kinds of values (not just numbers or strings).
* `.h5` is the way the Keras saves the weights for a neural net.
* `.json` is good for taking what would usually go into a Pickle file, and saving it in a format that can be loaded onto the web. It's also one of the formats used by Keras, part of a saved model.

## Setup

[librosa](https://github.com/bmcfee/librosa) needs some extra help on OS X, make sure to follow the instructions [here](https://github.com/bmcfee/librosa#hints-for-os-x) first.

```
$ git clone https://github.com/kylemcdonald/AudioNotebooks.git
$ cd AudioNotebooks.git
$ pip install -r requirements.txt
$ jupyter notebook
```