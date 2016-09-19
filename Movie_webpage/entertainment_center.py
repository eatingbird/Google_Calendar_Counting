import media
import fresh_tomatos

toy_story = media.Movie("Toy Story",
                        "A story of toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=vwyZH85NQC4")

#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print (avatar.poster_image_url)
#avatar.show_trailer()

movies = [toy_story, avatar]
#fresh_tomatos.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print (media.Movie.__module__)


