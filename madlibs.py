"""

Basic python project by Krish Srivastava
Madlibs using string concatenation


String concatenation:
Suppose we want to create a string  that says "Competitive programming is __________"
var = "Thrilling"  "some string variable"

A few ways to do concatenation are :
a) print("Competitive programming is " + var)
b) print("Competitive programming is {}".format(var))
c) print(f"Competitive programming is {var}")


"""

# for this project we will use the 3rd method of string concatenation

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
