"""
    1. access https://spotify-downloader.com/ to download Spotify playlists.
    2. unzip the downloaded folder to this script folder
    3. run the program
    4. type the folder name
    5. done!
"""

from mutagen.easyid3 import EasyID3
import os


while True:

    playlist_name = input('Playlist: ')

    if os.path.isdir(playlist_name):
        break
    else:
        print(f"Invalid folder.\nAvailable folders are: {next(os.walk('.'))[1]}")

playlist_path = os.path.abspath(playlist_name)

counter = 0
print()

for file in os.listdir(playlist_path):

    counter += 1
    song = EasyID3(f'{playlist_path}/{file}')

    old_name = f'{playlist_path}/{file}'

    # pattern = artist - title - album (album name) - year

    # avoid multiple artists
    artists = song['artist'][0].replace('/', ' & ')

    os.rename(old_name, f"{playlist_path}/"
                        f"{artists} - "
                        f"{song['title'][0]} - "
                        f"álbum ({song['album'][0]}) - "
                        f"{song['date'][0]}")

    print(song['title'][0])

print(f"\n{counter} files changed.")
