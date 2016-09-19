import webbrowser

class Movie():
    """ This class provides a way to store movie related information """
    # convention is to use capital for class - Google python convention guide
    # Good convention is to keep class separate from other codes, and just call it

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # Google style guide recommends all-capital variable name for the 
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
    # underscore means it is already in python
    # self is to generate a name space. If no self, an error will occur
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
