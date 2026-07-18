# User albums
import importlib

make_album = importlib.import_module('8_7').make_album

while True:
    print("\nEnter 'q' at any time to quit.")
    artist = input("Enter the artist's name: ")
    title = input("Enter the album title: ")
    tracks_input = input("Enter the number of tracks (or leave blank): ")
    if artist.lower() == 'q' \
    or title.lower() == 'q' \
    or tracks_input.lower() == 'q':
        break

    tracks = int(tracks_input) if tracks_input else None
    album = make_album(artist, title, tracks)
    print(album)
