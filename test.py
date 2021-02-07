import unittest
import spotify_webapi as sp


class TestWhole(unittest.TestCase):

    def test_track(self):
        track = 'https://open.spotify.com/track/2HRYa6iG1M5DRefO8pK2I3'
        tr = sp.Track(track)

        self.assertEqual(tr.title, 'Reagan')
        self.assertEqual(tr.artist, 'Killer Mike')
        self.assertEqual(tr.artist_url, 'https://open.spotify.com/artist/2N4EYkIlG1kv25g6Wv8LGI')

        self.assertEqual(tr.duration, 250)
        self.assertEqual(tr.releasedate, '2012-05-15')

        self.assertEqual(tr.album_url, 'https://open.spotify.com/album/5EAhUoAz1G3WTvIfGZvmrh')
        self.assertEqual(tr.album_number, 6)


    def test_playlist(self):
        playlist_string = "https://open.spotify.com/playlist/0r8WNX8191PI6lHnmwXWPA?"
        pl = sp.Playlist(playlist_string)

        self.assertEqual(pl.title, 'Musikalischer Samt.')

        self.assertEqual(pl.tracks[0].title, 'Reagan')
        self.assertEqual(pl.tracks[1].title, 'Words I Never Said (feat. Skylar Grey)')
        self.assertEqual(pl.tracks[2].title, 'Waiting Room')


class TestConvert(unittest.TestCase):
    """
    Test convertion of input str to clean url
    """
    def test_url(self):
        convert_str = "https://open.spotify.com/playlist/0r8WNX8191PI6lHnmwXWPA?si=0IUc7t4FRZWCgNwJLmGjQ"
        url = "https://open.spotify.com/playlist/0r8WNX8191PI6lHnmwXWPA"

        converted_url = sp.SpotifyGeneric.convert_to_url(convert_str)
        self.assertEqual(url, converted_url)

    def test_embed(self):
        convert_str = '<iframe src="https://open.spotify.com/embed/playlist/0r8WNX8191PI6lHnmwXWPA" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'
        url = "https://open.spotify.com/playlist/0r8WNX8191PI6lHnmwXWPA"

        converted_url = sp.SpotifyGeneric.convert_to_url(convert_str)
        self.assertEqual(url, converted_url)

    def test_id(self):
        convert_str = "spotify:playlist:0r8WNX8191PI6lHnmwXWPA"
        url = "https://open.spotify.com/playlist/0r8WNX8191PI6lHnmwXWPA"

        converted_url = sp.SpotifyGeneric.convert_to_url(convert_str)
        self.assertEqual(url, converted_url)

    def test_uri(self):
        convert_str = "spotify://playlist/0r8WNX8191PI6lHnmwXWPA"
        url = "https://open.spotify.com/playlist/0r8WNX8191PI6lHnmwXWPA"

        converted_url = sp.SpotifyGeneric.convert_to_url(convert_str)
        self.assertEqual(url, converted_url)

    def test_android_uri(self):
        convert_str = "android-app://com.spotify.music/spotify/playlist/0r8WNX8191PI6lHnmwXWPA"
        url = "https://open.spotify.com/playlist/0r8WNX8191PI6lHnmwXWPA"

        converted_url = sp.SpotifyGeneric.convert_to_url(convert_str)
        self.assertEqual(url, converted_url)


if __name__ == '__main__':
    unittest.main()