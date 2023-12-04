import wikipedia
import os
os.system("cls")
lang = "en"
mylist = []
with open('WikipediaSearch.txt', "w") as f1:
    f1.write("")
def WikipediaSearch():
    user_lang = input("Language:")
    lang = wikipedia.set_lang(user_lang)
    NumOfRepeats = int(input("Enter number of terms you want to search :"))
    for i in range(NumOfRepeats):
        user_request = input("Type in term to search:")
        try:
            summary = wikipedia.summary(user_request)
            print(f"Summary for {user_request}:\n{summary}\n")
            with open('WikipediaSearch.txt', "r") as f:
                f.write(f"Summary for {user_request}:\n{summary}\n")
        except:
            print(f"Page not found for {user_request}\n")
WikipediaSearch()
