import random

# 1. Open the book file
# 2. (optional) Clean the text file, e. g. lowercase
# everything etc.
# 3. split the text into a list of its tokens (i. e.
# words and punctuation). You may use native python
# methods or consult other libraries
# 4. Create a dictionary object, where:
# 1. the keys are the unique tokens
# 2. the values are lists of the next following
# words that occur after the key token (1 next
# word for every occurrence)
# 5. Generate text. Make it so that:
# 1. the program chooses the first word randomly
# from the keys and prints it (you can use  random
# library for this)
# 2. then it consults the occurrence list from the
# dictionary you created to randomly choose the
# next word to print out (you can use  random
# library for this)
# 3. repeat 5.2 200 times


with open("harry_potter.txt", "r") as file:
    text = file.read()

text = text.lower()

text = text.replace(',', '')
text = text.replace('.', '')
text = text.replace('?', '')
text = text.replace('!', '')
text = text.replace('"', '')
text = text.replace("'", '')
text = text.replace(':', '')
text = text.replace('(', '')
text = text.replace(')', '')


tokens = text.split()


word_dict = {}
for i in range(len(tokens)-1):
    current_word = tokens[i]
    next_word = tokens[i+1]
    if current_word in word_dict:
        word_dict[current_word].append(next_word)
    else:
        word_dict[current_word] = [next_word]

key = random.choice(list(word_dict.keys()))
print(f'{key=}')
print(f'key list length {len(word_dict[key])}')


generated_text = []
for x in range(200):
    next_word = random.choice(word_dict[key])
    generated_text.append(next_word)


print(" ".join(generated_text))