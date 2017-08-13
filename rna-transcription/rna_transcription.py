def to_rna(sequence):
    transcribed_sequence = list([transcribe(x) for x in sequence])
    transcribed_sequence_str = ''.join(transcribed_sequence)
    return transcribed_sequence_str if len(transcribed_sequence_str) == len(sequence) else ''


def transcribe(rune):
    transcription_map = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    return transcription_map.get(rune, '')
