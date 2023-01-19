input_str = '''
is
the
of
and
as
a
but
::
Descent of Man
The Ascent of Man
The Old Man and The Sea
A Portrait of The Artist As a Young Man
A Man is a Man but Bubblesort IS A DOG
'''

# read each line from stdin, each line before "::" is one WTI, each line after "::" is one sentence to be sorted
a = input_str.split("::")
ig_words = a[0].lower().strip('\n').split('\n')
sentences = a[1].lower().strip('\n').split('\n')
# ['descent of man', 'the ascent of man', 'the old man and the sea', 'a portrait of the artist as a young man', 'a man is a man but bubblesort is a dog']
all_words = []
for i in sentences:
    word = i.split()
    all_words.append(word)

key_words = []
for i in all_words:
    for j in i:
        if j not in ig_words:
            key_words.append(j)
key_words = sorted(list(set(key_words)))

for i in key_words:
    for j in sentences:
        loc = []
        m = j.find(i)
        while m != -1:
            loc.append(m)
            m = j.find(i, m + 1)
        if loc:
            print(loc)




