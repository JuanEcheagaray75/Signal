# TODO

- [x] Determine if we should save the data as CSV files, check whether another file format is better.
  - [x] Check if pandas should be used for this conversion
- [X] Check how Librosa "normalizes" the wav file, maybe scipy´s conversion is better (Audio being normalized to [-1, 1] seems to be the way to go)
  - [x] Librosa is the way to go, but definitely have to check how the normalization is done.
- [x] Study the output of FFT, I have already developed a version that returns an output that matches that of scipy's fft