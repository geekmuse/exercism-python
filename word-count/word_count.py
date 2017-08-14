def word_count(phrase):
    filtered_phrase = ''.join([c if c.isalnum() else ' ' for c in phrase])
    filtered_phrase_as_list = filtered_phrase.lower().split()
    filtered_phrase_as_list.sort()
    keys = list(set(filtered_phrase_as_list))
    count = {key: 0 for key in keys}

    for k in keys:
        for word in filtered_phrase_as_list:
            if word == k:
                count[k] = count[k] + 1

    return count
