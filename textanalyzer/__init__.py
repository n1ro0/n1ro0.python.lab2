#ILYA CHABAN
def word_frequencies(text: str) -> dict:
    """Takes 1 argument text. Returns dictionary
    of words' frequencies in text, where words
    are keys and there frequencies are values."""
    my_dict = {}
    for word in text.split():
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict
