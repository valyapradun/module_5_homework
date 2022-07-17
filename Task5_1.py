def sort_names():
    """
    Open file data/unsorted_names.txt in data folder.
    Sort the names and write them to a new file called sorted_names.txt.
    Each name should start with a new line
    """
    file = open('./data/unsorted_names.txt', 'r')
    names = sorted(file.readlines())
    file.close()
    file = open('./data/sorted_names.txt', 'w')
    for name in names:
        file.write(name)
    file.close()


if __name__ == '__main__':
    sort_names()