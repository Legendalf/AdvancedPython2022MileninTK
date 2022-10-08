import json
from typing import Union

NUMBER_TYPE = Union[int, float]


class Movie:
    def __init__(self, name, director, year: NUMBER_TYPE, country, duration: NUMBER_TYPE, age_rating: NUMBER_TYPE):
        self.name = name
        self.director = director
        self.year = year
        self.country = country
        self.duration = duration
        self.age_rating = age_rating
        
    def is_allowed(self, human):
        if (2022 - human.year_of_birth) < self.age_rating:
            permission = "False"
        else:
            permission = "True"
        return permission


class Cartoon(Movie):
    def __init__(self, name, director, year: NUMBER_TYPE, country, duration: NUMBER_TYPE, age_rating: NUMBER_TYPE, technique):
        self.name = name
        self.director = director
        self.year = year
        self.country = country
        self.duration = duration
        self.age_rating = age_rating
        self.technique = technique
    
    def is_allowed(self, human):
        if (2022 - human.year_of_birth) < self.age_rating:
            permission = "False"
        else:
            permission = "True"
        return permission


class Anime(Cartoon):
    def __init__(self, name, director, year: NUMBER_TYPE, duration: NUMBER_TYPE, age_rating: NUMBER_TYPE, technique):
        self.name = name
        self.director = director
        self.year = year
        self.country = "Japan"
        self.duration = duration
        self.age_rating = age_rating
        self.technique = technique
    
    def is_allowed(self, human):
        if (2022 - human.year_of_birth) < self.age_rating:
            permission = "False"
        else:
            permission = "True"
        return permission


class Human:
    def __init__(self, name, sex, year_of_birth: NUMBER_TYPE):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
