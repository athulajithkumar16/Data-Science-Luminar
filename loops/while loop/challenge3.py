# 3. Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number.
# If they enter "y", ask them to enter another number and keep adding numbers until they do not answer "y".
# Once the loop has stopped, display the total.

num1 = int(input('Enter a number : '))
num2 = int(input('Enter another number : '))
total = num1 + num2

choice = input('Do you want to add another number ? ')

while choice.lower() == 'y':
    num3 = int(input('Enter another number : '))
    total += num3

    choice = input('Do you want to add another number ? ')

print('Total is',total)

    