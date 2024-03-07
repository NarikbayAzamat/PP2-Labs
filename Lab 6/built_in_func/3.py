user_str = input()

def isPalindrom(str):
    reversed_str = str[::-1]
    if str == reversed_str:
        return True
    return False

if isPalindrom(user_str):
    print(f"Yes, {user_str} is palindrom.")
else:
    print(f"No, {user_str} is not palindrom.")