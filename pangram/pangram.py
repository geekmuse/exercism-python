def is_pangram(sentence):
    full_alpha_ord_list = list(range(ord('a'), ord('z')+1))
    full_alpha_list = [chr(i) for i in full_alpha_ord_list]
    full_alpha_list.sort()
    sentence_chars_as_list = list(sentence.lower())
    sentence_chars_as_list_filtered = [c for c in sentence_chars_as_list if c.isalpha()]
    sentence_chars_as_list_filtered.sort()
    sentence_chars_as_list_unique = set(sentence_chars_as_list_filtered)
    sentence_chars_as_list_unique = list(sentence_chars_as_list_unique)
    sentence_chars_as_list_unique.sort()
    return sentence_chars_as_list_unique == full_alpha_list
