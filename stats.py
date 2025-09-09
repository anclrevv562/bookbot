def get_num_words(str):
    list_words = str.split()
    count = 0
    for word in list_words:
        count += 1
    return count

def get_char_count(str):
    str = str.lower()
    char_dict = {}
    for char in str:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(dicx):
    sorted_tuple = sorted(dicx.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(sorted_tuple)
    return sorted_dict
