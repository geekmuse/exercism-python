def is_isogram(phrase):
    phrase_as_list = list(phrase.lower())
    phrase_as_list_filtered = [c for c in phrase_as_list if c.isalpha()]
    return len(phrase_as_list_filtered) == len(set(phrase_as_list_filtered))