#Program Name: string_finder.py
#Course: IT3883/Section W01
#Student Name: Anthony Henry
#Assignment Number: Lab7
#Due Date: 11/9/2020
#Purpose: This program will read each line of a text file and find the word "the".
#After finding the word "the" it will list the word immediately after in an array.

words = open("President Washinton Inaugural Speech.txt", "r").read().split()
newlist = open("Speech Alt.txt", "w")
count = 0
for word in words:
    if word.lower() == "the":
        newlist.write(words[count+1] + "\n")
    count  += 1