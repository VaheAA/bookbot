def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    words = text.split()
    counter = {}

    for word in words:
        for char in word:
            lower_char = char.lower()

            if lower_char in counter:
                counter[lower_char] += 1
            else:
                counter[lower_char] = 1

    return counter

def sort_on(items):
    return items['num']

def show_report(dict):
    sorted = []

    for key in dict:
        new_dict = {}
        new_dict['char'] = key
        new_dict['num'] = dict[key]

        sorted.append(new_dict)

    sorted.sort(reverse=True, key=sort_on)

    return sorted
