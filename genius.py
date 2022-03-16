import lyricsgenius
import json

# Client Access Token
token = "t19ZRmG1y5jaY-LjD1SEFdLuTB0dDiwQab4SNxWIofs7g8XHt6uJLCX8bnd-dow1"

genius = lyricsgenius.Genius(token)
genius.response_format = 'plain'


# open json file that is in the same directory
with open('master_json.json') as f:
    # load json data into a python object
    data = json.load(f)


# loop through each song/artist and fins lyrics then append to JSON obj
for tweets in data['tweets']:
    content_artist = tweets['Artist']
    content_track = tweets['Track Name']




    artist = genius.search_artist(f"{content_artist}", max_songs=1, sort="title", include_features=True)
    song = artist.song(f"{content_track}")

    # or:
    # song = genius.search_song("To You", artist.name)
    print(song.lyrics)
    #print(artist.songs)
    tweets['Lyrics'] = song.lyrics



# save
    with open('master_lyrics_added.json', 'w') as f:
        json.dump(data, f, indent = 2)

#song.save_lyrics()

#tweets['metaphorsFound'] = metaphorsFound
#tweets['metaphorFamily'] = metaphorFamilyFound
