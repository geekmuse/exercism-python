def distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("{} is not same length as {}".format(seq1, seq2))

    accum = 0
    seq1_as_list = list(seq1)
    seq2_as_list = list(seq2)

    for i, v in enumerate(seq1_as_list):
        if seq2_as_list[i] != v:
            accum = accum + 1

    return accum
