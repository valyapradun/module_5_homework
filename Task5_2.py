from collections import defaultdict


def most_common_words(filepath, number_of_words=3):
    """
    Implement a function which search for most common words in the file.
    Use `data/lorem_ipsum.txt` file as a example.
    """
    temp_dict = defaultdict(int)
    file = open(filepath, 'r')
    strings = file.readlines()
    for string in strings:
        for word in string.split():
            temp_dict[word] += 1
    file.close()
    res = sorted(temp_dict, key=temp_dict.get, reverse=True)
    return res[0:number_of_words]


if __name__ == '__main__':
    print(most_common_words(filepath='./data/lorem_ipsum.txt', number_of_words=4))