# Album
def make_album(artist: str, title: str, tracks: int = None) -> dict:
    """Return a dictionary representing an album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album['tracks'] = tracks
    return album
print(make_album('Metallica', 'Master of Puppets'))
print(make_album('Geoff Zanelli', 'Squadron 42'))
print(make_album('ABBA', 'The Best of ABBA, Vol. 1', tracks=12))
