#Program Name: string_finder.py
#Course: IT3883/Section W01
#Student(s) Name: Anthony Henry, Edward Koranteng
#Assignment Number: Lab7
#Due Date: 11/9/2020
#Purpose: This program will read each line of a text file and find the word "the".
#After finding the word "the" it will list the word immediately after in an array.

words = open("President Washinton Inaugural Speech.txt", "r").read().split() #reading Inaugural Speech and making each word an element of an array
newlist = open("Speech Alt.txt", "w") #creating a list for the words coming after each word "the" in the speech
count = 0 #to keep track of for loop (@Edward: I am looking for ways to get rid of this if possible)

for word in words:
    if word.lower() == "the": #for every word, place all letters of the word into a lower case form and check for the word "the"
        newlist.write(words[count+1] + "\n") #once found, take the word after the word "the", and place it in the alt file
    count  += 1 #increment count