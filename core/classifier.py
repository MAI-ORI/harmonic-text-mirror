import re
from core.language_mappings import char_to_value

def classify_word(word):
    """Classify a word into A, B, or C based on its digital root sum."""
    word_clean = re.sub(r'[^\w\s]', '', word)
    if not word_clean:
        return None
        
    char_values = [char_to_value(c) for c in word_clean]
    word_sum = sum(char_values)
    from core.utils import digital_root
    root = digital_root(word_sum)
    
    if root in [3, 6, 9]:
        return 'A'  # Symbolic / Spiritual
    elif root in [1, 4, 7]:
        return 'B'  # Emotional / Relational
    elif root in [2, 5, 8]:
        return 'C'  # Physical / Action-oriented
    return None

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
