from difflib import get_close_matches

def printFunction(output):
    if type(output) == list:
        i = 1
        for item in output:
            print ("{}) {}".format(i,item))
            i = i + 1
    else:
        print (output)

def findMeaning(w):
        if w in data.keys():
            printFunction(data[w])
        elif w.title() in data:
            printFunction(data[w.title()])
        elif w.upper() in data: #in case user enters words like USA or NATO
            printFunction(data[w.upper()])
        elif len(get_close_matches(w,data.keys()))>0:
            ask = input("Did you mean %s instead? (Press 'y' for YES and 'n' for NO) : " % get_close_matches(w,data.keys())[0]).lower()
            if ask == 'y':
                printFunction(data[get_close_matches(w,data.keys())[0]])
            elif ask == 'n':
                printFunction("Sorry, try again")
            else:
                printFunction("Enter it correctly")
        else:
            printFunction("Enter it correctly")

while True:
    word = input("Enter word:")
    output = findMeaning(word.lower())
    another = input("Do you want to search another word? 'y' or 'n' :")
    if another == 'y':
        continue
    else:
        print("Thanks! Hope to see you again! :)")
        break
    

