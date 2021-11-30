import os
import pydub
import librosa
import numpy as np
import pandas as pd

MP3_DIR = "songs\\mp3"
WAV_DIR = "songs\\wav"
DATA_DIR = "data"


def get_songs() -> list:
    """
    ### Generates a list of all the available songs on the "database".

    #### Returns:
        list: List of available songs on the database (not sorted)
    """
    return os.listdir(MP3_DIR)


def print_songs():
    """Print the list of all available songs on the "database"."""
    print('Available songs:')
    for song in get_songs():
        print(song)


def convert_to_wav(song_path: str):
    """
    ### Conversion of mp3 file to wav.

    #### Args:
        - song_path (str): Path of the mp3 file to be converted
    """
    song_name = song_path.split('.')[0]
    if song_name + '.wav' not in os.listdir(WAV_DIR):
        print('Converting ' + song_name + '.mp3 to ' + song_name + '.wav')
        song_path = os.path.join(MP3_DIR, song_path)
        song_wav = pydub.AudioSegment.from_mp3(song_path)
        song_wav = song_wav.set_channels(1)
        song_wav.export(os.path.join(
            WAV_DIR, song_name + '.wav'), format="wav")
    else:
        print(f'Already converted {song_name}.mp3 to {song_name}.wav')


def convert_all_songs():
    """Apply convert_to_wav to all files on MP3_DIR."""
    for song in get_songs():
        convert_to_wav(song)


def get_song_data(song_path: str):
    """
    ### Get data and sample rate from a song in WAV format.

    #### Args:
        - song_path (str): Path to the song

    #### Returns:
        - list: Data and sample rate of the WAV file

    - Librosa loads the audio file as mono by default.
    - The sampling rate used by default is 22050 Hz, however, given that the
    files I'm working with on my school project were sampled with 48000 Hz,
    I decided to use that frequency, in the future I'll set it as an optional
    parameter for the developer to play with.
    """
    song_name = song_path.split('.')[0]
    path = os.path.join(WAV_DIR, song_name + '.wav')
    data, sample_rate = librosa.load(path, sr=48000)
    return data, sample_rate


def song_data_to_csv(song_name: str, song_data: list, song_sample_rate: float):
    """
    ### Convert WAV file to a CSV.

    #### Args:
        - song_name (str): Name of the song
        - song_data (list): Amplitudes returned by get_song_data
        - song_sample_rate (float): Sample rate of the song (44100 - 48000 Hz)

    Investigate whether pandas is necessary for the conversion
    """
    if song_name + '.csv' not in os.listdir(DATA_DIR):
        df = pd.DataFrame(song_data, columns=['Amplitude'])
        df.index = [(1 / song_sample_rate) * i for i in range(len(df.index))]
        df.to_csv(os.path.join(DATA_DIR, song_name + '.csv'))
    else:
        print('Already converted ' + song_name +
              '.wav to ' + song_name + '.csv')


def songs_to_csv():
    """Convert all songs to CSV."""
    for song in get_songs():
        song_name = song.split('.')[0]
        song_data, song_sample_rate = get_song_data(song)
        song_data_to_csv(song_name, song_data, song_sample_rate)
