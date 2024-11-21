# program to print all even numbers between 1 and 20.
for number in range(1,21): 
    if number % 2==0: 
        print (number) 

# : Use a while loop to ask the user to input a number until they provide a number greater than 10

while True:
    number = int(input("Enter a number greater than 10: "))
    if number > 10:
        break

 # Write a program that prints the multiplication table (from 1 to 10) for numbers
 # from 1 to 5 using nested for loops.
 
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print() 



# Given a list of integers, [4, 7, 2, 9, 12, 15], 
# write a program using a for loop to find the sum of all odd numbers and print the result.

numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0

for number in numbers:
    if number % 2 != 0:
        odd_sum += number

print("Sum of odd numbers:", odd_sum) 
# If the remainder of the division by 2 is not 0, the number is odd.     