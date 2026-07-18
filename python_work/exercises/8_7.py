# Album
from typing import Optional


def make_album(artist: str, title: str, tracks: Optional[int] = None) -> dict:
    """Return a dictionary representing an album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album['tracks'] = tracks
    return album

# Guard it with if __name__ == '__main__': to prevent it from running when imported
if __name__ == '__main__':
    print(make_album('Metallica', 'Master of Puppets'))
    print(make_album('Geoff Zanelli', 'Squadron 42'))
    print(make_album('ABBA', 'The Best of ABBA, Vol. 1', tracks=12))
