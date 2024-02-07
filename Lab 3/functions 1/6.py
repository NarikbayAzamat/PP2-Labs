def reverse_sentence(sentence):
    words = sentence.split()
    new_sentence = " ".join(reversed(words))
    return new_sentence

user_input = input()
print(reverse_sentence(user_input))