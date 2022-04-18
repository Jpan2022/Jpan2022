#
#Joshua Pantoja
#SEC 290 24194.B1 Spring 2020
#2/16/2020
#Programming Assignemet week 5 
#

menu = """
=========================
Frequently Asked Questions
=========================

0: Exit
1: List FAQ's
2: Add FAQ
3: Delete FAQ
"""
print()

faq_dictionary = {}

finished = False

while not finished:
    
    print(menu)
    print()

    selection = input("Pleas enter a choice: ")
    if selection == "0":
        finished = True
    elif selection == "1":
        for result in faq_dictionary:
            print()

            print("Question: {}".format(result))
            print("Answer: {}".format(faq_dictionary[result]))
    elif selection == "2":        
        print()
        add_faq = True
        while not add_faq == False:
            print()
            add_faq = input("Please enter a question: ")
            print()
            if add_faq in faq_dictionary.keys():
                print("{} is already in the dictionary!".format(add_faq))
                print("Please rephrase the question.")
            else:
                answer = input("Please enter the answer: ")
                faq_dictionary[add_faq]= "{}".format(answer)
                print()
                print("Has been added to the FAQ!")
                add_faq = False
    elif selection == "3":
        print()
        delete_faq = input("Please enter the question to be deleted: ")
        if delete_faq in faq_dictionary:
            del(faq_dictionary[delete_faq])
            print()
            print("{} has been deleted from the FAQ's.".format(delete_faq))
        else:
            print()
            print("{} could not be found in the FAQ's.".format(delete_faq))
            print("No changes were made!")
            
    else:
        print()
        print("{} is not a valid entry!".format(selection))
print("Done!")  
