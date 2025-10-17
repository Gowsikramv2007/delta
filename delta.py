
age = input("Welcome! Please enter your age: ")

try:
    age = int(age)

 
    if age >= 18:
        print("✅ You are eligible to vote in Tamil nadu election. Make your voice count!")
    else:
        print("⛔ Sorry, you are not old enough to vote in Tamil nadu election yet.")
except ValueError:
    print("⚠️ Please enter a valid number for your age.")
