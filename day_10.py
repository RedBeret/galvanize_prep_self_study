# Day 10: Functions and Text Manipulation - Made 2021 edited in 2023 to fix notes

# Function to change spaces to underscores in column names
def snake_caser(in_lst):
    out_lst = []
    for txt in in_lst:
        out_lst.append(txt.replace(" ", "_"))
    return out_lst

column_names = ['gender', 'longest absence from school', 'is enrolled', 'enlist', 'unemployed', 'filed for bankruptcy', 'school', 'peace corps']
print(snake_caser(column_names))

# Text Manipulation - Capitalization
txt = 'And miles to go before i sleep.'
print(txt)
print(txt.lower())
print(txt.upper())
print(txt.title())
print(txt.capitalize())

# Text Manipulation - Count unique characters in a string
def unique_counter(string):
    unique_list = {}
    for char in string:
        if char not in unique_list.keys():
            unique_list[char] = 1
        elif char in unique_list.keys():
            unique_list[char] += 1
    return unique_list.keys(), unique_list.values()

s = 'This is a string, we want you to count how many times each unique character appears in this string!'
print(unique_counter(s))

# Text Manipulation - Split string into a list of lowercase words
def split_words(string):
    remove_punct_lst = [",", ".", ";", ":", "!", "?", "'", '"']
    for punct in remove_punct_lst:
        string = string.replace(punct, "")
    return string.lower().split()

text = "Hello there! How are you? Why don't you take a seat over there? Once we went to the store and we found ourselves in a strange place. We ran into two people. They were very interesting to talk to. Each of them had an interesting accent and we wondered where they were from."
print(split_words(text))

# Function to take food orders using a while loop
food_lst = ['Pancakes', 'Omelet', 'Toast', 'Waffles', 'Bacon', 'Sausage', 'Orange Juice']
order = []
while True:
    print('Make a selection from this list: ')
    for idx, item in enumerate(food_lst, 1):
        print(f'{idx}: {item}')
    order.append(food_lst[int(input('Choose an item by number: ')) - 1])
    if input('Choose another item? (Y/N) ') in "nNqQ":
        break
print(order)

# Function to return parallel lists of unique characters and their counts
def chars_counter(txt):
    unique_chars = []
    char_counts = []
    for ch in txt:
        if ch not in unique_chars:
            unique_chars.append(ch)
            char_counts.append(txt.count(ch))
    return unique_chars, char_counts

s = 'This is a string, we want you to count how many times each unique character appears in this string!'
print(chars_counter(s))

# Function to remove punctuation and common English words from a string
def string_cleaner(txt):
    txt = txt.lower()
    remove_punct_lst = [",", ".", ";", ":", "!", "?", "'", '"']
    for punct in remove_punct_lst:
        txt = txt.replace(punct, "")
    remove_word_lst = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "can", "will", "just", "don", "should", "now"]
    lst = []
    for word in txt.split():
        if word not in lst and word not in remove_word_lst:
            lst.append(word)
    return lst

inp = "Hello there! How are you? Why don't you take a seat over there? Once we went to the store and we found ourselves in a strange place. We ran into two people. They were very interesting to talk to. Each of them had an interesting accent and we wondered where they were from."
print(" ".join(string_cleaner(inp)))
