#Question 1
# while True:
#     age = input("Enter your age (or type 'stop'): ")

#     if age.lower() == "stop":
#         break

#     age = int(age)

#     if age < 18:
#         print("You are a minor.")
#     elif age <= 60:
#         print("You are an adult.")
#     else:
#         print("You are a senior citizen.")


# #Question 2
# while True:
#     vehicle = input("Enter vehicle name: ")

#     if vehicle.lower() == "bus":
#         print("Finally the wait is over")
#         break
#     else:
#         print("Waiting")

# #Question 3
# while True:
#     fruit = input("Enter a fruit name: ")

#     if fruit.lower() == "apple":
#         print("You got it!")
#         break
#     else:
#         print("Try again")


# #Question 4
# while True:
#     password = input("Enter the password: ")

#     if password == "open sesame":
#         print("Access granted!")
#         break
#     else:
#         print("Wrong password, try again.")



# #Question 5
# ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']

# content_ratings = {}

# for rating in ratings:
#     if rating in content_ratings:
#         content_ratings[rating] += 1
#     else:
#         content_ratings[rating] = 1

# print(content_ratings)


# #Question 6
# import random

# number = random.randint(1, 10)
# attempts = 0

# while True:
#     guess = int(input("Guess the number (1-10): "))
#     attempts += 1

#     if guess < number:
#         print("Guess higher")
#     elif guess > number:
#         print("Guess lower")
#     else:
#         print(f"Correct! Attempts taken: {attempts}")
#         break



# #Question 7
# attempts = 0

# while attempts < 3:
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username == "admin" and password == "1234":
#         print("Login successful")
#         break
#     else:
#         print("Invalid credentials, try again.")
#         attempts += 1

# if attempts == 3:
#     print("Too many failed attempts.")


# #Question 8
# import random

# while True:
#     num1 = random.randint(1, 30)
#     num2 = random.randint(1, 30)

#     answer = input(f"What is {num1} × {num2}? (type 'exit' to stop): ")

#     if answer.lower() == "exit":
#         break

#     if int(answer) == num1 * num2:
#         print("Correct!")
#     else:
#         print("Incorrect, try again.")


# #Question 9
# while True:
#     value = input("Enter a number (or 'exit'): ")

#     if value.lower() == "exit":
#         break

#     num = int(value)
#     is_prime = True

#     if num < 2:
#         is_prime = False
#     else:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break

#     if is_prime:
#         print("The number is prime.")
#     else:
#         print("The number is not prime.")


# #Question 10
# secret_word = "python"

# while True:
#     guess = input("Guess the word (or type 'quit'): ")

#     if guess.lower() == "quit":
#         break
#     elif guess == secret_word:
#         print("Congratulations, you guessed the word!")
#         break
#     else:
#         print("Incorrect, try again")


# #Question 11
# count = 0

# while count < 3:
#     text = input("Enter a phrase: ")

#     if text.lower() == "good luck":
#         count += 1
#         if count < 3:
#             print(f"You typed the same word {count} times.")
#         else:
#             print("You typed good luck three times.")


# #Question 12
# current_floor = 1

# while True:
#     destination = input("Enter destination floor (0 to exit): ")

#     if destination == "0":
#         print("Goodbye!")
#         break

#     try:
#         destination = int(destination)

#         if destination > current_floor:
#             print("Going up")
#         elif destination < current_floor:
#             print("Going down")
#         else:
#             print("You are already on this floor.")

#         current_floor = destination

#     except ValueError:
#         print("Invalid input. Please enter a number.")