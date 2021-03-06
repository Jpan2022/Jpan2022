#
#Joshua Pantoja
#SEC 290 24194.B1 Spring 2020
#2/9/2020
#Programming Assignemet week 4 
#

menu = """
Scoring engine

1: Exit
2: List scores so far
3: Add a score
4: Display the Highest and lowest scores
"""
print()
number_list= [85.3,85.2,21.99]


finished = False


while not finished:
    print(menu)
    print()

    selection = input("Pleas enter a selection between 1 and 4: ")
    if selection == "1":
        finished = True
    elif selection == "2":
        print()
        print("Scores recorded so far:")
        print()
        number_list.sort()
        number_list.reverse()
        for number in number_list:
            print("{:.2f}".format(number))
    elif selection == "3":
        print()
        add_score = input("Please enter a score between 0 and 100: ")
        add_score = float(add_score)
        if add_score < 0:
            print()
            print("{} is too low! Scores must be btween 0 and 100".format(add_score))
        elif add_score > 100:
            print()
            print("{} is too high! Scores must be btween 0 and 100".format(add_score))
        else:
            added_score = number_list.append(add_score)
    elif selection == "4":
        print()
        number_list.sort()
        number_list.reverse()
        lowest_score = len(number_list)-1
        print("Highest score: {:.2f}, Lowest score: {:.2f}".format(number_list[0],number_list[lowest_score]))
            
    else:
        print()
        print("{} is not a valid entry!".format(selection))
    
print("Done!")    
