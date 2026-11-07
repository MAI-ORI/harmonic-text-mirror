import string

# Define the custom alphabet mapping (A, B, C)
ALPHABET_MAPPING = {
    'a': 'A', 'b': 'B', 'c': 'C', 'd': 'A', 'e': 'B', 'f': 'C',
    'g': 'A', 'h': 'B', 'i': 'C', 'j': 'A', 'k': 'B', 'l': 'C',
    'm': 'A', 'n': 'B', 'o': 'C', 'p': 'A', 'q': 'B', 'r': 'C',
    's': 'A', 't': 'B', 'u': 'C', 'v': 'A', 'w': 'B', 'x': 'C',
    'y': 'A', 'z': 'B'
}

def get_digital_root(n):
    """Calculate the digital root of an integer."""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

def clean_word(word):
    """Remove punctuation from a word and convert to lowercase."""
    return word.strip(string.punctuation).lower()

def classify_word(word):
    """Classify a word into A, B, or C based on its digital root."""
    cleaned = clean_word(word)
    if not cleaned:
        return None
    
    total_val = 0
    for char in cleaned:
        if char in ALPHABET_MAPPING:
            # Map char to A, B, or C, then convert to numeric value (A=1, B=2, C=3)
            mapped = ALPHABET_MAPPING[char]
            val = {'A': 1, 'B': 2, 'C': 3}[mapped]
            total_val += val
        else:
            # Ignore non-alphabet characters
            pass
            
    if total_val == 0:
        return None
        
    root = get_digital_root(total_val)
    
    # Map digital root to final classification
    if root in [1, 4, 7]:
        return 'A'
    elif root in [2, 5, 8]:
        return 'B'
    elif root in [3, 6, 9]:
        return 'C'
    return None
