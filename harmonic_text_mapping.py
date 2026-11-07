# Core Harmonic Text Mapping Logic
def get_digital_root(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def classify_word(word, alphabet_mapping):
    word = ''.join(char for char in word if char.isalnum())
    values = [alphabet_mapping.get(char.lower(), 0) for char in word]
    total_sum = sum(values)
    digital_root = get_digital_root(total_sum)
    return {
        "word": word,
        "values": values,
        "sum": total_sum,
        "digital_root": digital_root
    }
