""""
@author: Emad Bin Abid
@date: 02-11-2018
"""

### Program to purify scraped text of roman-urdu sentences

## Dependencies


special_chars = ['.', ',', '/', '?', ':', ';', '(', ')', "'", "!", "+", "-", "*", "_", "=", "@", "#", "$", "%", "^", "&",
                 "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
english_alphabets = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
SPLITFACTOR = " <>"
file = None

def load_file(filename):
    file = open(filename, "r")
    raw_data = file.readlines()
    file.close()
    return raw_data

raw_data = load_file("../data/database-1.txt")

def init_clean():
    print("Initial cleaning in process...")
    # Removing '\n' from the list
    while 'Copyright © 2018. Jang Group of Newspapers All rights reserved.\n' in raw_data:
        raw_data.remove('Copyright © 2018. Jang Group of Newspapers All rights reserved.\n')
    while '\n' in raw_data:
        raw_data.remove('\n')

def split_para_into_sentences():
    print("Splitting paragraphs into sentences...")
    sentences = list()
    for entry in raw_data:
        sentences += entry.split('.')
    return sentences
init_clean()

sentences = split_para_into_sentences()
all_sentences = ""

# Concatenating all sentences into one string
print("Concatenating all sentences...")
for s in sentences:
    all_sentences += s
    all_sentences += SPLITFACTOR

# Removing special chars
print("Removing special characters...")
for ch in special_chars:
    while ch in all_sentences:
        all_sentences = all_sentences.replace(ch, "")
    # print(ch, "done!")
print("... done!")

# Removing non-english scripts
print("Removing non-english scripts...")
new_all_sentences = ""
for s in all_sentences:
    if s.lower() in english_alphabets:
        new_all_sentences += s
print("... done!")

all_words = all_sentences.split(' ')
unique_words = set(all_words)

print("All Sentences: ", len(sentences))
print("All Words: ", len(all_words))
print("Unique Words: ", len(unique_words))

new_all_sentences = new_all_sentences.split(SPLITFACTOR)


print("Writing to File...")
fileW = open("../data/corpus-1.txt", "w+")
for s in new_all_sentences:
    fileW.write(s)
    fileW.write('\n')
fileW.close()