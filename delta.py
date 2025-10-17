
age=input("welcome Enter your age!")
try:
        age=int(age)
if age >= 18:
        print("You are eligible to vote in Tamilnadu election")
else:
        print("Sorry, you are not old enough to vote in Tamilnadu.")
except ValueError:
    print("Please enter a valid number for your age.")

