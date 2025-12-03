# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# if num1>num2 and num1>num3:
#     print(f"{num1} is the greatest number")
# elif num2>num1 and num2>num3:
#     print(f"{num2} is the greatest number") 
# else:
#     print(f"{num3} is the greatest number")
# #adsf
# # Program to print month name from month number

# monthnumber = int(input("Enter a month number (1-12): "))

# months = [
#     "January", "February", "March", "April",
#     "May", "June", "July", "August",
#     "September", "October", "November", "December"
# ]

# if 1 <= monthnumber <= 12:
#     print("Month:", months[monthnumber - 1])
# else:
#     print("Invalid month number!")

# # program to swap two variables

# ----------------------------------------------------------------
# swapping two variables
# num1=int(input('Enter a first number: '))
# num2=int(input('Enter a second number: '))
# print(f'num1 {num1}')
# print(f'num2: {num2}')
# print('Before swapping the values of num1 and num2')
# num1,num2=num2,num1
# print(f'num1 {num1}')
# print(f'num2: {num2}')
# print('After swapping values of num1 and num2')
# -------------------------------------------------------------------
# Movie Ticket Price Calculator using nested if-else


# Movie Ticket Price Calculator using nested if-else


age = int(input("Enter your age: "))
member = input("Do you have a membership card? ")

if age < 12:
    print("FREE")
else:
    if age <= 60 and age >= 12:
        if member == "yes":
            print("Ticket Price: Rs. 150")
        else:
            print("Ticket Price: Rs. 200")
    else:
        print("Ticket Price: Rs. 100")  



#       to calculate electricity bill

units = int(input("Enter electricity usage in units: "))

if units < 100:
    cost = units * 5

else:

    if units <= 300 and units > 100:
        
        cost = 100 * 5
        
        cost += (units - 100) * 8
    else:

        
        cost = 100 * 5            
        cost += 200 * 8            
        cost += (units - 300) * 10 

print("Total Electricity Bill: Rs", cost)



# Rock Paper Scissors using nested if-else

p1 = input("Player 1, enter your move (rock/paper/scissors): ")
p2 = input("Player 2, enter your move (rock/paper/scissors): ")

if p1 == p2:
    print("It's a tie!")
else:
    if p1 == "rock":
        if p2 == "scissors":
            print("Player 1 wins")
        else:
            print("Player 2 wins!")

    else:
        if p1 == "paper":
            if p2 == "rock":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

        else:
            if p1 == "scissors":
                if p2 == "paper":
                    print("Player 1 wins!")
                else:
                    print("Player 2 wins!")







#program to check numbers of desks

a = int(input("Enter number of students in class A: "))
b = int(input("Enter number of students in class B: "))
c = int(input("Enter number of students in class C: "))


desks_a = (a + 1) // 2
desks_b = (b + 1) // 2
desks_c = (c + 1) // 2

total_desks = desks_a + desks_b + desks_c

print("Minimum number of desks needed:", total_desks)



#profram to decide whether the lift goes up down or stays


current_floor = 5
requested_floor = 3

if requested_floor > current_floor:
    print("The lift will go UP.")
else:
    if requested_floor < current_floor:
        print("The lift will go DOWN.")
    else:
        print("The lift will STAY at the current floor.")





  #program to check whether the input number is positive and if positive check whether it is even or odd
  

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is EVEN.")
    else:
        print("The number is ODD.")
else:
    print("The number is NOT positive.")



#o check which number is greater and if equal check whether positive negative or zero

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print(a, "is greater.")
else:
    if b > a:
        print(b, "is greater.")
    else:
        print("Both numbers are equal.")

        
        if a > 0:
            print("The number is positive.")
        else:
            if a < 0:
                print("The number is negative.")
            else:
                print("The number is zero.")


    #fizz buzz program
num = int(input("Enter a number: "))

if num % 3 == 0:
    if num % 5 == 0:
        print("Fizz Buzz")
    else:
        print("Fizz")
else:
    if num % 5 == 0:
        print("Buzz")
    else:
        print(num)



#Use the random module to create a number from 0 to 5. Then use an if/elif/else statement to print out one of these six random Snapple facts:
import random
num = random.randint(0, 5)
if num == 0:
    print('Flamingos turn pink from eating shrimp.')
elif num == 1:
    print("The only food that doesn't spoil is honey.")
elif num == 2:
    print('Shrimp can only swim backwards.')
elif num == 3:
    print("A taste bud's life span is about 10 days.")
elif num == 4:
    print('It is impossible to sneeze while sleeping.')
else:
    print('It is illegal to sing off-key in North Carolina.')



  # Write a program that takes total_amount andis_member (True/False) as input and prints the final amount after applying the correct discount (or no discount).
total_amount = float(input("Enter total purchase amount: Rs "))
is_member = input("Are you a member? (True/False): ")
is_member = True if is_member == "True" else False
if total_amount > 1000 and is_member:
    discount = 0.20
elif total_amount > 1000 and not is_member:
    discount = 0.10
else:
    discount = 0.0
final_amount = total_amount - (total_amount * discount)
print("Final amount to pay: Rs", final_amount)



#program to calculate weight according to planet
earth_weight = float(input("Enter your weight on Earth (kg): "))
planet_number = int(input("Enter planet number (1-7): "))
if planet_number == 1:
    gravity = 0.38
elif planet_number == 2:
    gravity = 0.91
elif planet_number == 3:
    gravity = 0.38
elif planet_number == 4:
    gravity = 2.53
elif planet_number == 5:
    gravity = 1.07
elif planet_number == 6:
    gravity = 0.89
elif planet_number == 7:
    gravity = 1.14
else:
    gravity = None
if gravity is None:
    print("Invalid planet number.")
else:
    destination_weight = earth_weight * gravity
    print("Your weight on that planet is:", destination_weight, "kg")



#program that accepts marks of four supjects and prints total marks percentagw and grade
# Take marks of four subjects
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100
if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First Division"
elif percentage > 40:
    grade = "Pass"
else:
    grade = "Fail"
print("\n--- Result ---")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)


# Write a program to accept the cost price of a bike and display the road tax to bepaid according to the  criteria:
cost_price = float(input("Enter the cost price of the bike (Rs): "))
if cost_price > 100000:
    tax = 0.15
elif cost_price > 50000:
    tax = 0.10
else:
    tax = 0.05
tax_amount = cost_price * tax
print("\n--- Road Tax Details ---")
print("Cost Price: Rs", cost_price)
print("Tax Rate:", tax * 100, "%")
print("Tax to be Paid: Rs", tax_amount)


#A company decided to give bonus to employee according to given criteria calculate total bonus 
salary = float(input("Enter the employee's salary: Rs "))
years = float(input("Enter years of service: "))
if years > 10:
    bonus = 0.10
elif years >= 6:
    bonus = 0.08
else:
    bonus = 0.05
bonus_amount = salary * bonus
print("\n--- Bonus Details ---")
print("Years of Service:", years)
print("Bonus Rate:", bonus * 100, "%")
print("Bonus Amount: Rs", bonus_amount)


#wap to take subject score as input and display message according to criteria
score = float(input("Enter your subject score: "))
if score > 90:
    print("🎉 Congratulations! Excellent performance!")
elif score >= 50:
    print("🙂 Good effort! But you can still improve.")
else:
    print("⚠️ You should retake the course for better understanding.")

#wap to CHECK eligibility for job
age = int(input("Enter candidate's age: "))
has_degree = input("Do you have a degree? (yes/no): ").lower()
experience = float(input("Enter years of work experience: "))
if age >= 18:
    if has_degree == "yes":
        if experience > 3:
            print("Highly Eligible.")
        elif experience >= 1:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("Not eligible: Degree required.")
else:
    print("Not eligible: Age must be 18 or above.")

#wap to display wages
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of working days: "))
if age >= 18 and age < 30:
    if gender == "M":
        wage_per_day = 700
    else:
        wage_per_day = 750
elif age >= 30 and age <= 40:
    if gender == "M":
        wage_per_day = 800
    else:
        wage_per_day = 850
else:
    wage_per_day = None  

if wage_per_day is None:
    print("Invalid age for wage calculation.")
else:
    total_wage = wage_per_day * days
    print("\n--- Wage Details ---")
    print("Wage per day: Rs", wage_per_day)
    print("Total wage for", days, "days: Rs", total_wage)

#wap to make simple atm 
# ATM Simulation

is_valid = True
balance = 50000
correct_pin = 123
pin = int(input("Enter your PIN: "))
if pin == correct_pin:
    print("\n--- ATM MENU ---")
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Exit")

    option = int(input("Choose an option (1-3): "))

    if option == 1:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient balance!")
    else:
        if option == 2:
            print("Your current balance is:", balance)
        else:
            if option == 3:
                print("Thank you for visiting")
            else:
                print("Invalid option!")
else:
    print("Wrong PIN!")


#create magic forest game
print("Welcome to the Magic Forest!")
direction = input("Do you want to go 'north' or 'south'? ").lower()

if direction == "south":
    print("Game Over")
else:
    if direction == "north":
        river_path = input("Do you want to 'cross the river' or 'follow the path'? ").lower()
        if river_path == "cross the river":
            print("Game Over")
        else:
            if river_path == "follow the path":
                creature = input("Choose your companion: 'fairy', 'ogre', or 'elf': ").lower()
                if creature == "elf":
                    print("You Win")
                else:
                    print("Game Over")
            else:
                print("Invalid choice! Game Over")
    else:
        print("Invalid direction! Game Over")


#wap to create hunted house game
print("Welcome to the Haunted House!")
direction = input("Do you want to go 'upstairs' or 'downstairs'? ").lower()

if direction == "downstairs":
    print("Game Over")
else:
    if direction == "upstairs":
        action = input("Do you want to 'enter the room' or 'stay outside'? ").lower()
        if action == "enter the room":
            print("Game Over")
        else:
            if action == "stay outside":
                creature = input("Choose your companion: 'ghost', 'vampire', or 'werewolf': ").lower()
                if creature == "werewolf":
                    print("You Win")
                else:
                    print("Game Over")
            else:
                print("Invalid choice! Game Over")
    else:
        print("Invalid direction! Game Over")

    
    

