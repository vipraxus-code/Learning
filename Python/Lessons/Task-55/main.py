def make_album(artist, album, tracks=1):
    return {"artist": artist, "album": album, "track_count": tracks}

while True:
    user_input = input("Would you like to add new data? (yes/no) ")
    if user_input.lower() == "no":
        break
    artist = input("Input artist name: ")
    album = input("Input album name: ")
    tracks = int(input("Input number of tracks in album: "))
    print(make_album(artist, album, tracks))