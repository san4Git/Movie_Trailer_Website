
import webbrowser
""""This is Video Class I have created to child class called Movie and
TVShow for Parent class Video in same class for convenience"""

"""This is Parent Class  Which contains show_trailer method to show trailer """
class Video():
     def __init__(self,movie_title,movie_duration ,poster_image ,trailer_youtube):
        self.title = movie_title
        self.duration = movie_duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

      
        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)


"""This is Child Class to display Movies"""        
class Movie(Video):
    def __init__(self,title,duration,movie_storyline,poster_image_url,trailer_youtube_url):
        Video.__init__(self,title,duration ,poster_image_url,trailer_youtube_url)
        self.storyline = movie_storyline


"""This is Child Class to display TVShow"""       
class TVShow(Video):
    def __init__(self, title,duration ,season ,poster_image_url,trailer_youtube_url):
        Video.__init__(self,title,duration ,poster_image_url,trailer_youtube_url)
        self.season = season
       
