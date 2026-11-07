import re

# Default English mapping
ENGLISH_MAPPING = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
    's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
}

# Default Hebrew mapping
HEBREW_MAPPING = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 1, 'כ': 2, 'ל': 3, 'מ': 4, 'נ': 5, 'ס': 6, 'ע': 7, 'פ': 8, 'צ': 9,
    'ק': 1, 'ר': 2, 'ש': 3, 'ת': 4
}

def get_digital_root(n):
    """Calculate the digital root of an integer."""
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

def classify_word(word, mapping=ENGLISH_MAPPING):
    """Classify a word into A, B, or C based on its digital root."""
    # Remove non-alphabetic characters
    clean_word = re.sub(r'[^a-zA-Zא-ת]', '', word).lower()
    if not clean_word:
        return None
    
    # Calculate sum of letter values
    total = sum(mapping.get(char, 0) for char in clean_word)
    root = get_digital_root(total)
    
    # Classify based on digital root
    if root in [3, 6, 9]:
        return 'A'
    elif root in [1, 4, 7]:
        return 'B'
    elif root in [2, 5, 8]:
        return 'C'
    return None

def process_text(text, mapping=ENGLISH_MAPPING):
    """Process a text string and return classified words and counts."""
    words = text.split()
    classified = []
    counts = {'A': 0, 'B': 0, 'C': 0}
    
    for word in words:
        category = classify_word(word, mapping)
        if category:
            classified.append((word, category))
            counts[category] += 1
            
    return classified, counts
