def fahrenheit_to_centrigrade(fahrenheit):
    centrigrade = (5 / 9) * (fahrenheit - 32)
    return f"{fahrenheit} fahrenheit is equal to {centrigrade} centrigrade."

print(fahrenheit_to_centrigrade(100))