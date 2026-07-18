# User albums
import importlib

make_album = importlib.import_module('8_7').make_album

print(make_album('Metallica', 'Master of Puppets'))
print(make_album('Geoff Zanelli', 'Squadron 42'))
