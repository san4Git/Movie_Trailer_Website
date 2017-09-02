import media
import fresh_tomatoes

"""Here are some of movie colection for San Movie"""
toy_story = media.Movie("Sleepless In Seattle",
                        "1-Minut",
                        "A story in Seattle",
                        "https://upload.wikimedia.org/wikipedia/en/e/e1/Sleepless_in_seattle.jpg",
                        "https://www.youtube.com/watch?v=4J7gg1V0oak")
friends = media.TVShow("Friends",
                       "30-Minuts",
                       "Season-1",
                       "https://upload.wikimedia.org/wikipedia/en/1/1c/Friends_Season_1_DVD.jpg",
                       "https://www.youtube.com/watch?v=hDNNmeeJs1Q")


everyBodysFine = media.Movie("Eveybody's Fine",
                             "3-Minuts",
                             "About Dad and children",
                             "https://upload.wikimedia.org/wikipedia/en/2/2e/Everybodys_fine.jpg",
                             "https://www.youtube.com/watch?v=T3tMPp8fRxk")

princes_Bride = media.Movie("The Princess Bride",
                            "2-Minuts",
                            "Story of Princess and love",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                            "https://www.youtube.com/watch?v=GNvy61LOqY0")

house_of_Cards = media.TVShow("House of Cards",
                              "30-Minuts",
                              "Season-1",
                              "https://upload.wikimedia.org/wikipedia/en/a/a9/Frank_Underwood_-_House_of_Cards.jpg",
                              "https://www.youtube.com/watch?v=ULwUzF1q5w4")

italian_job = media.Movie("The Italian Job",
                            "5-Minuts",
                            "Story of well executed Job",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/Italianjob.jpg",
                            "https://www.youtube.com/watch?v=Z0uN32GV1_c")

eraser = media.Movie("Eraser",
                            "3-Minuts",
                            "Story of Eraser a persons past to protect his future",
                            "https://upload.wikimedia.org/wikipedia/en/2/2c/Eraser_%28movie_poster%29.jpg",
                            "https://www.youtube.com/watch?v=31_OEhX30sY")

"""We use fresh_tomatoes class and method open_movies_page uses list so we are collecting movies in list"""
movies =[toy_story ,friends ,everyBodysFine ,princes_Bride ,house_of_Cards ,italian_job,eraser ]
fresh_tomatoes.open_movies_page(movies)

