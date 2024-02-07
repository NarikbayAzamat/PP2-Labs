def is_palindrom(str):
    reversed_str = str[::-1]
    if reversed_str == str:
        return True
    else:
        return False
    
print(is_palindrom("aza"))
