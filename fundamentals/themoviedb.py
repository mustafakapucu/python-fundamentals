import requests


class theMovieDb:
    def __init__(self):
        self.apiUrl = "https://api.themoviedb.org/3"
        self.apiKey = "f29fa73ca27ea9f63aae2e3a2af8bf2a"

    def getPopulars(self):
        response = requests.get(
            f"{self.apiUrl}/movie/popular?api_key={self.apiKey}&language=en-US&page=1")
        return response.json()

    def getSearhcResult(self):
        search = input("Film Name: ")
        response = requests.get(
            f"{self.apiUrl}/search/company?api_key={self.apiKey}&query={search}&page=1")
        return response.json()


movieApi = theMovieDb()

while True:
    secim = input("1- Popular Movies\n2- Search Movies\n3- Exit\nSeçim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            # print(movies)

            for movie in movies["results"]:
                print(movie["title"])

        if secim == "2":
            movies = movieApi.getSearhcResult()
            # print(movies)

            for movie in movies["results"]:
                print(movie["name"])
