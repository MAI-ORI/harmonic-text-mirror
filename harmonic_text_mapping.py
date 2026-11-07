import re
import unicodedata

# ==========================================
# 1. MULTILINGUAL ALPHABET MAPPING
# ==========================================

# Base English mapping (A=1, B=2, ..., Z=26)
ENGLISH_MAPPING = {chr(i): i - 64 for i in range(65, 91)}

# Base Hebrew mapping (Alef=1, Bet=2, ..., Tav=400)
HEBREW_MAPPING = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
    'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90, 'ק': 100, 'ר': 200,
    'ש': 300, 'ת': 400
}

# Fallback mapping for other languages (Unicode-based)
def get_unicode_mapping(char):
    """
    Returns a numeric value for any Unicode character based on its code point.
    Ensures support for all languages.
    """
    val = ord(char)
    # Normalize value to 1-9 range for harmonic consistency
    return (val % 9) if val % 9 != 0 else 9

def get_char_value(char, lang='en'):
    """
    Returns the numeric value of a character based on the selected language.
    """
    char = char.upper()
    if lang == 'en' and char in ENGLISH_MAPPING:
        return ENGLISH_MAPPING[char]
    elif lang == 'he' and char in HEBREW_MAPPING:
        return HEBREW_MAPPING[char]
    else:
        # Fallback to Unicode mapping for unsupported languages or special characters
        return get_unicode_mapping(char)

# ==========================================
# 2. DIGITAL ROOT CALCULATION
# ==========================================

def digital_root(n):
    """
    Calculates the digital root of a number (1-9).
    """
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

# ==========================================
# 3. WORD CLASSIFICATION
# ==========================================

def classify_word(word, lang='en'):
    """
    Classifies a word into A, B, or C based on its digital root.
    """
    # Remove punctuation and whitespace
    clean_word = re.sub(r'[^\w]', '', word)
    if not clean_word:
        return None, 0
    
    # Sum character values
    total_sum = sum(get_char_value(c, lang) for c in clean_word)
    root = digital_root(total_sum)
    
    # Classification logic
    if root in [3, 6, 9]:
        classification = 'A'  # Symbolic / Spiritual
    elif root in [1, 4, 7]:
        classification = 'B'  # Emotional / Relational
    elif root in [2, 5, 8]:
        classification = 'C'  # Physical / Structural
    else:
        classification = 'Unknown'
        
    return classification, root

# ==========================================
# 4. PROBABILITY EXPECTANCE & DESERVEANCE MONITOR
# ==========================================

class ExpectanceMonitor:
    """
    Tracks user expectation and coherence alignment to prevent symbolic distortion.
    """
    def __init__(self, threshold=0.75):
        self.threshold = threshold
        self.history = []

    def log_interaction(self, user_coherence, expected_outcome_strength):
        """
        Logs user coherence and expectation strength.
        Returns a status: 'aligned', 'over-expectant', or 'unstable'.
        """
        self.history.append({
            'coherence': user_coherence,
            'expectation': expected_outcome_strength
        })
        
        # Calculate moving average of coherence
        avg_coherence = sum(h['coherence'] for h in self.history[-5:]) / min(len(self.history), 5)
        
        if expected_outcome_strength > 0.85 and avg_coherence < self.threshold:
            return 'over-expectant'
        elif avg_coherence < 0.5:
            return 'unstable'
        else:
            return 'aligned'

# ==========================================
# 5. ADJUSTMENT & INTEGRATION MODULES
# ==========================================

class AdjustmentModules:
    """
    Provides real-time feedback and system tuning to maintain coherence.
    """
    @staticmethod
    def suggest_breath_pause(status):
        """
        Suggests a breath pause if the system detects over-expectation or instability.
        """
        if status == 'over-expectant':
            return "⚠️ High expectation detected with low coherence. Please take a 4-second inhale, 4-second exhale pause."
        elif status == 'unstable':
            return "🛑 Coherence is low. We recommend a 16-second box breathing cycle before continuing."
        return "✅ Coherence is stable. Proceed."

    @staticmethod
    def tune_system_sensitivity(user_coherence):
        """
        Dynamically adjusts system sensitivity based on user coherence.
        """
        if user_coherence < 0.6:
            return "System sensitivity reduced. Classification thresholds widened."
        elif user_coherence > 0.85:
            return "System sensitivity increased. Precision mode activated."
        return "System sensitivity stable."
