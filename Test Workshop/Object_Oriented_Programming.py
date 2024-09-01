""""
class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def drive(self):
        print("This car drives.")
    
    def stop(self):
        print("This car stops.")

car_1 = Car("Chevy", "Corvette", "blue", 2011)

print(car_1.make, car_1.year) 
"""

class Book:
    def __init__(self, year, title, author, audience, genre, rating):
        self.year = year
        self.title = title
        self.author = author
        self.audience = audience
        self.genre = genre
        self.rating = rating

    def book_recommendation(self):
        print("I would give", self.title, "by", self.author, "a rating of", self.rating, "out of 10. It was published in", self.year, ". It is a", self.genre, "book, and I recommend it to", self.audience)

print("Welcome to Book Recommendation Maker!")

year = input("Enter the year your book was published in: ")
title = input("Enter your book title: ")
author = input("Name the author: ")
audience = input("Describe the demographic you recommend this book to: ")
genre = input("Enter the book genre: ")
rating = input("Give yoru book a rating out of 10: ")

book_1 = Book(year, title, author, audience, genre, rating)

book_1.book_recommendation()