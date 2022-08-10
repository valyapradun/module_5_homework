def sort_names(input_file_name: str, output_file_name: str):
    """
    Open file data/unsorted_names.txt in data folder.
    Sort the names and write them to a new file called sorted_names.txt.
    Each name should start with a new line
    """
    with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
        names = sorted(input_file.readlines())
        for name in names:
            output_file.write(name)



if __name__ == '__main__':
    sort_names('./data/unsorted_names.txt', './data/sorted_names.txt')
