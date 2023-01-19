import sys

#read everything from stdin, until enter+ctrl+d used to signal the end; each line before "::" is one WTI, each line after "::" is one sentence to be sorted
input_string = sys.stdin.read()
a = input_string.split("::")
ig_words = a[0].lower().strip('\n').split('\n')
sentences = a[1].lower().strip('\n').split('\n')
# ['descent of man', 'the ascent of man', 'the old man and the sea', 'a portrait of the artist as a young man', 'a man is a man but bubblesort is a dog']
all_words = []
for i in sentences:
    word = i.split()
    all_words.append(word)

#get sorted unique sets of keywords that can be used to get corresponding sentence in all sentences 
key_words = []
for i in all_words:
    for j in i:
        if j not in ig_words:
            key_words.append(j)
key_words = sorted(list(set(key_words)))

for i in key_words:
    for j in sentences:
        #track the starting index of keyword in each sentence, if multiple keywords, record multiple times
        loc = []
        m = j.find(i)
        while m != -1:
            loc.append(m)
            m = j.find(i, m + len(i))

        if loc:
            #replace the lowercase keyword with uppercase keyword
            for n in loc:
                temp_dele = j[:n] + j[(n + len(i)):]
                temp_inse = temp_dele[:n] + i.upper() + temp_dele[n:]
                print(temp_inse)




