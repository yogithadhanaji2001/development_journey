class Movie:

    def __init__(self,title,director,language,year):

        self.title=title

        self.director=director

        self.language=language

        self.year=year

    def __str__(self):
        return self.title
            


    def display_movies(self):

        print(self.title,self.director,self.language,self.year)


movie_instance=Movie("goat_life","bengiman","malayalam",2024)

movie_instance.display_movies()

print(movie_instance)




