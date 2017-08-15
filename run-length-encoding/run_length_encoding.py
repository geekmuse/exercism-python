def decode(to_be_decoded):
    """
    Decodes a run-length encoded string.

    :param to_be_decoded: run-length encoded string
    :return: run-length decoded string
    """
    to_be_decoded_list = list(to_be_decoded)
    decoded_str_as_list = list()
    num_to_print_as_list = list()
    for c in to_be_decoded_list:
        if c.isdigit():
            num_to_print_as_list.append(c)
        else:
            if len(num_to_print_as_list) > 0:
                num_to_print = int(''.join(num_to_print_as_list))
                append = c * num_to_print
                decoded_str_as_list.append(append)
                num_to_print_as_list = list()
            else:
                decoded_str_as_list.append(c)

    return ''.join(decoded_str_as_list)


def encode(to_be_encoded):
    """
    Run-length encodes a string

    :param to_be_encoded: string to be run-length encoded
    :return: run-length encoded string
    """
    last_seen = None
    last_seen_count = 0
    to_be_encoded_as_list = list(to_be_encoded)
    encoded_str_as_list = list()

    for c in to_be_encoded_as_list:
        if last_seen:
            if last_seen == c:
                last_seen_count += 1
            else:
                if last_seen_count > 1:
                    encoded_str_as_list.append('{}{}'.format(last_seen_count, last_seen))
                else:
                    encoded_str_as_list.append('{}'.format(last_seen))
                last_seen_count = 1
        else:
            last_seen_count += 1
        last_seen = c

    if last_seen_count > 1:
        encoded_str_as_list.append('{}{}'.format(last_seen_count, last_seen))
    else:
        if last_seen:
            encoded_str_as_list.append('{}'.format(last_seen))
        else:
            encoded_str_as_list = list()

    return ''.join(encoded_str_as_list)
