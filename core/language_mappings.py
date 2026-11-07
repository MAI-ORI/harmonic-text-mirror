import unicodedata
from core.utils import digital_root

def char_to_value(char):
    """
    Map a character to a 1-9 value.
    Uses traditional 1-9 mapping for English letters,
    and Unicode code point digital roots for all other languages.
    """
    normalized = unicodedata.normalize('NFD', char)
    clean_char = "".join([c for c in normalized if unicodedata.category(c) != 'Mn'])
    
    if not clean_char:
        return 0
        
    if clean_char.lower() in 'abcdefghijklmnopqrstuvwxyz':
        val = ord(clean_char.lower()) - 96
        return (val - 1) % 9 + 1
        
    return digital_root(ord(clean_char))
