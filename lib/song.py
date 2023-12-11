class Song:
    pass
    count = 0
    genres = set()
    artists = set()
    genre_count = dict()
    artist_count = dict()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        value = cls.genre_count.get(genre)
        value = (value + 1) if bool(value) else 1
        cls.genre_count.update({genre: value})

    @classmethod
    def add_to_artist_count(cls, artist):
        value = cls.artist_count.get(artist)
        value = (value + 1) if bool(value) else 1
        cls.artist_count.update({artist: value})