import sys

# input_string = "of\na\nthe\nis\nand\nbut\n::\ndescent of man\nthe ascent of man\nthe old man and the sea\na man is a man but bubblesort is a dog"

def stdIn():
    print("Please input strings here: ")
    buffer = sys.stdin.read()
    return buffer

def stdOut(string):
    print(string)

def strToList(string):
    aList = string.lower().strip('\n').split('\n')
    return aList

def parseAW(list):
    aw = []
    for i in list:
        word = i.split()
        aw.append(word)
    return aw

def parseKW(content, target):
    kw = []
    for i in content:
        for j in i:
            if j not in target:
                kw.append(j)
    kw = sorted(list(set(kw)))
    return kw    

# ???possible object creation?For all lines of title: keyword1:[list1,[indexInList]];[list2,[indexInList]]...keyword2:[list1,[indexInList]];[list2,[indexInList]]...
def oneKwOneTitleLoc(kw, title):
    loc = []
    m = title.find(kw)
    while m != -1:
        loc.append(m)
        m = title.find(kw, m + len(kw))
    return loc    

def oneKwOneTitleRep(kw, title, loc):
    result = ""
    for i in loc:
        temp = title[:i] + title[(i + len(kw)):]
        replace = temp[:i] + kw.upper() + temp[i:]
        if replace:
            result += replace + "\n"
    if len(result) > 0:
        return result

# ???unable to encapsule this method as the Nones in result prevent from assignment
# def catResult(res, rep):
#     if rep is not None:
#         res += rep
#         return res


if __name__ == "__main__":
    input_string = stdIn()
    a = input_string.split("::")
    ig_words = strToList(a[0])
    sentences = strToList(a[1])
    all_words = parseAW(sentences)
    key_words = parseKW(all_words, ig_words)

    ans = ""
    for i in key_words:
        for j in sentences:
            aLoc = oneKwOneTitleLoc(i, j)
            aRep = oneKwOneTitleRep(i, j, aLoc)
            if aRep is not None:
                ans += aRep
    ans = ans[:-1]
    stdOut(ans)
        
        






