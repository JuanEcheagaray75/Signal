# Signal

## Installation

Run the following commands on your terminal of choice:

```{bash}
pip install numpy
pip install pandas
pip install matplotlib
pip install librosa
pip install pydub
```

*WARNING:* In order to run this script you must also make sure to have installed `ffmpeg`, it also needs to be added to your `PATH` environment variable. Depending upon the version of Python you are running you may or may not have it already installed. For further documentation on how to properly install `ffmpeg` please refer to the [installation site](https://ffmpeg.org/download.html).

## Usage

As of now, this project uses a list of csv files contained in `data\test_data` and the sampling frequency is set to 48 KHz. Our script loops through the directory and converts each `csv` file into a data frame with 2 columns, we are supposing that the files contained a stereo signal.

Then it merges the signals to create a mono file, and finally a FFT (Fast Fourier Transform) is performed on the signal. The results are plotted considered a frequency domain of around 20 KHz, then they are saved in `images`.

However, this is just a *beta* version of our project. We plan to implement further features such as:

- Numerical matching
- Capability of receiving a signal from a microphone
- A GUI
  
## Contents

- Small audio preprocessing module
- Our own implementation of the FFT

## Contributing

Feel free to make any pull requests! We'd like to see your contribution!

## License

[GPL-3.0 License](https://github.com/JuanEcheagaray75/Signal/blob/master/LICENSE)