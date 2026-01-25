def make_album(artist, album, tracks=1):
    return {"artist": artist, "album": album, "number of tracks": tracks}

print(make_album("aj47", "new_album", 15))