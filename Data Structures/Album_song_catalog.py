"""
Module Name: Album and Song Catalog Template
Description: Stores album information, including artist details and a list of songs with their lyrics and track numbers, then displays the catalog.
Author: Kollier
"""

albums = []
album_count = int(input("How many albums would you like to enter? "))

for i in range(album_count):
    print(f"\n--- Album {i + 1} ---")
    album_name = input("Album name: ")
    artist = input("Artist name: ")
    publication_year = int(input("Publication year: "))

    general_info = (artist, publication_year)

    songs = []
    song_count = int(input("How many songs would you like to enter? "))

    for j in range(song_count):
        print(f"\n--- Song {j + 1} ---")
        song_name = input("Song title: ")
        lyrics = input("Song lyrics: ")
        track_number = int(input("Track number: "))

        song = {
            "song_name": song_name,
            "lyrics": lyrics,
            "track_number": track_number
        }

        songs.append(song)

    album = {
        "album_name": album_name,
        "general_info": general_info,
        "songs": songs
    }

    albums.append(album)

for album in albums:
    print("\nAlbum:")
    print(f"  Name: {album['album_name']}")
    print(f"  General information: {album['general_info']}")

    print("  Songs:")

    for song in album["songs"]:
        print(f"    Track number: {song['track_number']}")
        print(f"    Name: {song['song_name']}")
        print(f"    Lyrics: {song['lyrics']}")