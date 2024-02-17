#File: q1.py
#Author: Leah Philip
#Date: 2/16/2023
#Section: 506
#E-mail: leahephilip@tamu.edu
#Description: This program takes a number in and recognizes if it is a plaindrome or not.
def reverse_number(num):
    reversed_num = 0
    original_num = num

    while num > 0:
        last_digit = num % 10
        reversed_num = (reversed_num * 10) + last_digit
        num //= 10

    return reversed_num

def is_palindrome(num):
    return num == reverse_number(num)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Reverse of the number:", reverse_number(num))
    if is_palindrome(num):
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
