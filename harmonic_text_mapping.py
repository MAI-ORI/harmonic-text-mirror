import re
import unicodedata

# Digital root function
def digital_root(n):
    """Calculate the digital root of an integer using 1-9 modular reduction."""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

# Function to map any character to a numeric value using Unicode code points
def char_to_value(char):
    """
    Map a character to a 1-9 value.
    Uses traditional 1-9 mapping for English letters,
    and Unicode code point digital roots for all other languages.
    """
    # Normalize character to handle accents and diacritics
    normalized = unicodedata.normalize('NFD', char)
    # Filter out non-spacing marks (accents)
    clean_char = "".join([c for c in normalized if unicodedata.category(c) != 'Mn'])
    
    if not clean_char:
        return 0
        
    # For standard English letters, use traditional 1-9 mapping
    if clean_char.lower() in 'abcdefghijklmnopqrstuvwxyz':
        val = ord(clean_char.lower()) - 96
        return (val - 1) % 9 + 1
        
    # For other languages, use Unicode code point reduced to 1-9
    return digital_root(ord(clean_char))

# Function to classify a word into A, B, or C
def classify_word(word):
    """Classify a word into A, B, or C based on its digital root sum."""
    # Remove punctuation
    word_clean = re.sub(r'[^\w\s]', '', word)
    if not word_clean:
        return None
        
    # Calculate sum of character values
    char_values = [char_to_value(c) for c in word_clean]
    word_sum = sum(char_values)
    root = digital_root(word_sum)
    
    # Classification rules
    if root in [3, 6, 9]:
        return 'A'  # Symbolic / Spiritual
    elif root in [1, 4, 7]:
        return 'B'  # Emotional / Relational
    elif root in [2, 5, 8]:
        return 'C'  # Physical / Action-oriented
    return None

# Function to process a sentence and return classification counts
def process_sentence(sentence):
    """Process a sentence and return word classifications and category counts."""
    words = sentence.split()
    results = {'A': 0, 'B': 0, 'C': 0}
    word_details = []
    
    for word in words:
        category = classify_word(word)
        if category:
            results[category] += 1
            word_details.append((word, category))
            
    return results, word_details
