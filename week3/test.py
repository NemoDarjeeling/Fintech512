import sys


    # input_string = sys.stdin.read()
    # if not input_string:
    #     raise ValueError("empty input")
    input_string = "of\na\nthe\nis\nbut\n::\ndescent of man\nthe ascent of man\nthe old man and the sea\na man is a man but bubblesort is a dog"
    a = input_string.split("::")
    print(a)
    ig_words = a[0].lower().strip('\n').split('\n')

    sentences = a[1].lower().strip('\n').split('\n')
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

    result = ""

    for i in key_words:
        for j in sentences:
            loc = []
            m = j.find(i)
            while m != -1:
                loc.append(m)
                m = j.find(i, m + len(i))

            if loc:

                for n in loc:
                    temp_dele = j[:n] + j[(n + len(i)):]
                    temp_inse = temp_dele[:n] + i.upper() + temp_dele[n:]
                    print(temp_inse)
                    result += temp_inse + "\n"

    # ulti_result = result[:-1] 
    # return ulti_result
