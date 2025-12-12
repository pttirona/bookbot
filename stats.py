from collections import Counter


def split_text (text):
    return len(text.split())

# def char_count(text):
#     lower = Counter(text)
#     lower_text = {}
#     # for word in text:
#     #     lower_text += word.lower()
#
#     print(lower)
    
    
def char_count(text: str) -> dict[str, int]:
    counts = {}
    for ch in text.lower():  # convert every character to lowercase
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts

def sort_count(char_count):
    new_list = []

    for character, num in char_count.items():
        if not character.isalpha():
            continue

        item = {"char": character, "num": num}
        new_list.append(item)

    new_list.sort(key=sort_on, reverse=True)
    return new_list

def sort_on(item):
    return item["num"]