def get_num_words(text):
    return len(text.split())

def character_occurrences(text):
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def print_character_occurrences(character_occurrences):
    print(character_occurrences)

def sort_characters(char_counts):
    def sort_key(item):
        return item["num"]
    
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=sort_key, reverse=True)
    return char_list

def print_sorted_character_occurrences(character_occurrences):
    for character, count in sorted(character_occurrences.items()):
        print(f"The '{character}' character was found {count} times")