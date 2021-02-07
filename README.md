## spotify websapi

**Note: This libary can only parse the first 50 songs of a playlist!** (spotify web limitations)

No login, no apikey, no apilimit just webparsing

## How to use:

```python
import spotify_webapi as sp

playlist_string = "https://open.spotify.com/playlist/0r8WNX8191PI6lHnmwXWPA?"
another_playlist_string = "spotify:playlist:37i9dQZF1DWZeKCadgRdKQ"
song_string = '<iframe src="https://open.spotify.com/embed/track/3PQLYVskjUeRmRIfECsL0X" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'

print("pulling playlist...")
pl = sp.Playlist(playlist_string)

print("pulling song...")
tr = sp.Track(song_string)

print("init playlist obj without pulling\n")
pl2 = sp.Playlist(another_playlist_string, False)

print(f"songs of {pl.title}")
print(f"third song of the playlist: {pl.tracks[2].title}\n")

print(f"{tr.title} was released on {tr.releasedate}")
```
