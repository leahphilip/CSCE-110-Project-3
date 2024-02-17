#File: q5.py
#Author: Leah Philip
#Date: 02/07/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program prints the total number of letters in the user's sentence input and the total number of occurrences of the first and last letter of the sentence.
phrase=str(input("Enter text :"))
if len(phrase) !=6:
    print("The string is invalid!!")
elif(phrase[0].islower()):
    print("The string is invalid!!")
else:
    print("The string is valid!")
