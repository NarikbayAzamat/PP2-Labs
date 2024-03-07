user_str = input()

number_of_uppercase = number_of_lowercase = 0

for i in user_str:
    if ord(i) >= 65 and ord(i) <= 90:
        number_of_uppercase += 1
    elif ord(i) >= 97 and ord(i) <= 122:
        number_of_lowercase += 1

print(f"Number of uppercase letters in {user_str} is {number_of_uppercase}.")
print(f"Number of lowercase letters in {user_str} is {number_of_lowercase}.")

#2
# for i in user_str:
#     if i.isupper():
#         number_of_uppercase += 1
#     elif i.islower():
#         number_of_lowercase += 1

