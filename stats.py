def get_num_words(book):
    words = book.split()
    return len(words)


def get_chars_dict(text):
    unique_chars =  {}
    for c in text:
        char_lower = c.lower()
        if char_lower in unique_chars:
            unique_chars[char_lower] += 1
        else:
            unique_chars[char_lower] = 1
    return unique_chars

# mine solution

def chars_dict_to_sorted_list(unique_chars_dict):
    unique_character_list = [{"char": key, "num": value} for key, value in unique_chars_dict.items()]
    unique_character_list.sort(reverse = True, key = lambda x: x['num'])
    return unique_character_list

# original solution

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list_orig(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse = True, key=sort_on)
    return sorted_list