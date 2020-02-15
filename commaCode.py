#found in Stack Overflow

def list_thing(words):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_thing(spam))