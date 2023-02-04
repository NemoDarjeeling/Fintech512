def remove_leading_chars(filename):
    with open(filename, 'r') as f:
        content = f.readlines()
    
    modified_content = []
    for line in content:
        if line.startswith('    '):
            modified_line = line[4:]
            modified_content.append(modified_line)
        else:
            modified_content.append(line)
    
    with open(filename, 'w') as f:
        f.writelines(modified_content)

def main():
    filename = input("Enter the name of the file: ")
    remove_leading_chars(filename)

if __name__ == "__main__":
    main()