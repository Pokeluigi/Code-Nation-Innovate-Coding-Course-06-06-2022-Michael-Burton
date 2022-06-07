# # Activity 1

# def add_up():    
#     num1 = input("please input a number ")
#     num2 = input("please input a second number ")
#     if num1 and num2: 
#         try:
#             int(num1)
#             int(num2)
#             print("Your two numbers add up to:")
#             print(int(num1)+int(num2))
#         except:
#             print("please only input numbers")
#     else:
#         print("You didn't input anything...")

# add_up()

# Activity 2
# Using the IMDB Page as reference I will create 2 functions one that gives a summary of the movie and 1 that gives one of the quotes from the movie

# import random

# quote_array = [
#     "Dorian Corey: I always had hopes of being a big star. But as you get older, you aim a little lower.",
#     "Dorain Corey: Everybody wants to make an impression, some mark upon the world. Then you think, you've made a mark on the world if you just get through it, and a few people remember your name. Then you've left a mark. You don't have to bend the whole world. I think it's better to just enjoy it. Pay your dues, and just enjoy it.",
#     "Dorian Corey: If you shoot an arrow and it goes real high, hooray for you.",
#     "Venus Xtravaganza: Some of them say that we're sick, we're crazy. And some of them think that we are the most gorgeous, special things on Earth.",
#     "Octavia St. Laurent: I'm not looking for anything. I think all men are dogs. I honestly do. You know, every man starts barking sooner or later.",
#     "A young Pepper LaBeija can be seen very briefly as a contestant in the 1968 documentary The Queen, about a drag beauty pageant held in New York City. The legendary Crystal LaBeija, original mother and founder of the House of LaBeija, is also featured giving a fierce and shady reading.",
#     "Picked by Entertainment Weekly magazine as one of the '50 Greatest Independent Films' in a special supplement devoted to independent films that was only distributed to subscribers in October 1997.",
#     "This documentary was a major inspiration for the television series Pose (2018). A fictional dramatization of 1980s and early 1990s ball culture in New York. Dorian Corey and Venus Xtravaganza inspired specific stories. After Corey's death, a dead body was found in her closet, just as Elektra is seen hiding a dead body in hers. Venus's death while turning tricks is not unlike the fate of Candy Ferocity,",
#     "After Dorien Corey's death a mummified corpse was found hidden in a trunk in their closet the identity of which has never been identified with certainty"
# ]

# summary = "A documentary of New York's LGBT scene in the 1980s, showing the real life of poor Black and Latin LGBT people, introduce the ballrooms, the categories, the houses, the voguing, and the dreams and ambitions of these people who are systematically excluded from society, they fight to conquer the right to be and to reinvent themselves in a world starring straight and white people. They use the balls to show their creativity, have fun with their community and family, shining, and having their names recognized in the ballroom scene."

# def movie_stuff():
#     cont = True
#     while cont == True:
#         choice = input("Would you like a Quote/Trivia or a Summary of the Documentary? [1/2] or use quit to end ")
#         if choice == "1":
#             print(quote_array[random.randint(0, 8)])
#         elif choice == "2":
#             print(summary)
#         elif choice == "quit":
#             cont = False
#         else:
#             print("Please pick either 1 for Quotes and Trivia or 2 for Summary or quit to quit")

# movie_stuff()