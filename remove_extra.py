import pandas as pd
import json




# open json file that is in the same directory
with open('lyrics.json') as f:
    # load json data into a python object
    data = json.load(f)
# loop through 'tweets' looking for certin keys
for tweets in data['tweets']:
    #print(tweets['like count'], tweets['url'])
    del tweets['_type']
    del tweets['annotation_count']
    del tweets['api_path']
    del tweets['full_title']
    del tweets['header_image_thumbnail_url']
    del tweets['header_image_url']
    del tweets['id']
    del tweets['instrumental']
    del tweets['lyrics_owner_id']
    del tweets['lyrics_state']
    del tweets['lyrics_updated_at']
    del tweets['path']
    del tweets['pyongs_count']
    del tweets['song_art_image_thumbnail_url']
    del tweets['song_art_image_url']
    del tweets['stats']
    #del tweets[]['unreviewed_annotations']
    #del tweets['hot']
    #del tweets['pageviews']
    del tweets['title_with_featured']
    del tweets['updated_by_human_at']
    del tweets['url']
    del tweets['primary_artist']
    del tweets['artist']





with open('lyrics_update.json', 'w') as f:
    json.dump(data, f, indent = 2)
