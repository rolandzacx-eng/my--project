import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits +string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password
def get_strength(length):
    if length <8:
        return "weak"
    elif length <12:
        return "medium"
    else:
        return "strong"

length = int(input("Enter password length: "))
count = int(input("How many passwords do you want? "))

print("\n--- Your Generated Passwords   ---")

file = open("passwords.text", "w")
file.write("Your Generated Passwords\n")
file.write("----------------------------\n")

for i in range(count):
    pwd = generate_password(length)
    strength = get_strength(length)
    print(f"{i+1}. {pwd}  [{strength}]")
    file.write(f"{i+1}. {pwd}  [{strength}]\n")

file.close()
print("\nPasswords saved to passwords.text")