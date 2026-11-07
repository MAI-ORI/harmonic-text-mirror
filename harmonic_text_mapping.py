import re
import hashlib

# Define alphabet mappings
ALPHABET_MAPPINGS = {
    'english': {char: i % 9 + 1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")},
    'hebrew': {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 1, 'כ': 2, 'ל': 3, 'מ': 4, 'נ': 5, 'ס': 6, 'ע': 7, 'פ': 8, 'צ': 9,
        'ק': 1, 'ר': 2, 'ש': 3, 'ת': 4
    }
}

def get_digital_root(value):
    """Calculate the digital root of a number or string."""
    if isinstance(value, str):
        value = sum(int(char) for char in value if char.isdigit())
    while value > 9:
        value = sum(int(digit) for digit in str(value))
    return value

def classify_word(word, language='english'):
    """Classify a word into A, B, or C based on its digital root."""
    mapping = ALPHABET_MAPPINGS.get(language.lower(), ALPHABET_MAPPINGS['english'])
    word_clean = re.sub(r'[^a-zA-Zא-ת]', '', word).lower()
    if not word_clean:
        return None
    
    total_value = sum(mapping.get(char, 0) for char in word_clean)
    root = get_digital_root(total_value)
    
    if root in [3, 6, 9]:
        return 'A'
    elif root in [1, 4, 7]:
        return 'B'
    elif root in [2, 5, 8]:
        return 'C'
    return None

def process_text(text, language='english'):
    """Process text and return word classifications and counts."""
    words = text.split()
    results = []
    counts = {'A': 0, 'B': 0, 'C': 0}
    
    for word in words:
        category = classify_word(word, language)
        if category:
            results.append((word, category))
            counts[category] += 1
            
    return results, counts

def calculate_token_reward(counts, wallet_address):
    """
    Calculate token rewards based on harmonic counts.
    Accepts any valid wallet address dynamically.
    """
    if not wallet_address:
        return None
        
    total_words = sum(counts.values())
    if total_words == 0:
        return None
        
    # Reward logic based on harmonic balance
    a_ratio = counts['A'] / total_words
    b_ratio = counts['B'] / total_words
    c_ratio = counts['C'] / total_words
    
    # Generate a unique transaction hash using the wallet address and counts
    tx_data = f"{wallet_address}-{counts['A']}-{counts['B']}-{counts['C']}"
    tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()
    
    # Determine token type and amount based on harmonic profile
    if a_ratio > 0.5:
        token_type = "SHAIDS"
        amount = round(counts['A'] * 1.5, 2)
    elif b_ratio > 0.5:
        token_type = "Pi"
        amount = round(counts['B'] * 1.2, 2)
    else:
        token_type = "XRP"
        amount = round(counts['C'] * 1.0, 2)
        
    return {
        "wallet": wallet_address,
        "token": token_type,
        "amount": amount,
        "tx_hash": tx_hash
    }
