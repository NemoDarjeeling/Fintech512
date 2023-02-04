import sys
# 1. read lines from input


def read_line():
    lines = sys.stdin.readlines()
    # strip the newline character in each line and stores each line in list
    # since the list is ordered, we do nothing to "::" and leave it for next step
    lines = [line.strip().lower() for line in lines]
    return lines

# 2. data storage (no error handling yet)


def data_store(input):
    list1 = []
    list2 = []
    state = 0
    for line in input:
        if line != "::" and state == 0:
            list1.append(line)
        if line == "::":
            state = 1
            continue
        if state == 1:
            list2.append(line)

    return (list1, list2)

# 3. find all keywords


def find_key(list_ignore, list_titles):
    list_key = []
    for title in list_titles:
        # split title by whitespace
        words = title.split(" ")
        for word in words:
            if word in list_ignore:
                continue
            else:
                if word in list_key:
                    continue
                else:
                    list_key.append(word)
    return list_key

# 4. get output


def get_output(list_titles, list_key):
    # each element of the result is a tuple in the form of (keyword, index in list_titles, content)
    # so after sorting, all requirements of output can be satisfied (save time in cost of space)
    result = []
    for index, title in enumerate(list_titles):
        # split title by whitespace
        words = title.split(" ")
        for i in range(len(words)):
            if words[i] in list_key:
                words[i] = words[i].upper()
                result.append((words[i].upper(), index, " ".join(words)))
                # the idea is similar to backtracing, revert the word back to lower case, i.e. back to the previous state
                words[i] = words[i].lower()

    result.sort()

    for res in result:
        print(res[2])


# main function
if __name__ == "__main__":
    result = read_line()
    list_ignore, list_titles = data_store(result)
    list_key = find_key(list_ignore, list_titles)
    get_output(list_titles, list_key)
