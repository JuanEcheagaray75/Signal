import os
import sys
import pydub
import librosa
import numpy as np
import pandas as pd

MP3_DIR = "songs\\mp3"
WAV_DIR = "songs\\wav"
DATA_DIR = "data"


def get_songs() -> list:
    """
    ## Genera lista de canciones en la base de datos.

    ### Returns:
        list: Lista de canciones en la base de datos.
    """
    return os.listdir(WAV_DIR)


def print_songs():
    """Impresión de todas las canciones disponibles en la base de datos."""
    print('Available songs:')
    for song in get_songs():
        print(song)


# Function that converts a mp3 file to a wav file if it is not already inside WAV_DIR
def convert_to_wav(song: str):

    song_name = song.split('.')[0]
    if song_name + '.wav' not in os.listdir(WAV_DIR):
        print('Converting ' + song_name + '.mp3 to ' + song_name + '.wav')
        song_path = os.path.join(MP3_DIR, song)
        song_wav = pydub.AudioSegment.from_mp3(song_path)
        song_wav = song_wav.set_channels(1)
        song_wav.export(os.path.join(
            WAV_DIR, song_name + '.wav'), format="wav")
    else:
        print(f'Already converted {song_name}.mp3 to {song_name}.wav')


# Function that converts all songs in the "database" to wav files
def convert_all_songs():
    for song in get_songs():
        convert_to_wav(song)


def get_song_data(song: str):
    # This function takes so long to run because it normalizes the data to be between -1 and 1
    song_name = song.split('.')[0]
    song_path = os.path.join(WAV_DIR, song_name + '.wav')
    data, sample_rate = librosa.load(song_path)
    return data, sample_rate


def song_data_to_csv(song_name, song_data, song_sample_rate):
    # Check if the song is already in the data directory
    if song_name + '.csv' not in os.listdir(DATA_DIR):
        df = pd.DataFrame(song_data, columns=['Amplitude'])
        df.index = [(1 / song_sample_rate) * i for i in range(len(df.index))]
        # Convert the dataframe to a csv file
        df.to_csv(os.path.join(DATA_DIR, song_name + '.csv'))
    else:
        print('Already converted ' + song_name +
              '.wav to ' + song_name + '.csv')


def songs_to_csv():
    for song in get_songs():
        song_name = song.split('.')[0]
        song_data, song_sample_rate = get_song_data(song)
        song_data_to_csv(song_name, song_data, song_sample_rate)


