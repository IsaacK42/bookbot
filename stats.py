def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters_by_frequency(char_counts):
    sorted_char_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            sorted_char_list.append({"char": char, "num": count})

    sorted_char_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_char_list