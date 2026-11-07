import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import re

# ==========================================
# 1. CONFIGURATION & CONSTANTS
# ==========================================

# Default English alphabet mapping (A-Z -> 1-9)
DEFAULT_MAPPING = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
    'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
}

# Hebrew alphabet mapping (Alef-Tav -> 1-9)
HEBREW_MAPPING = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 1, 'כ': 2, 'ל': 3, 'מ': 4, 'נ': 5, 'ס': 6, 'ע': 7, 'פ': 8, 'צ': 9,
    'ק': 1, 'ר': 2, 'ש': 3, 'ת': 4
}

# ==========================================
# 2. CORE FUNCTIONS
# ==========================================

def get_digital_root(n):
    """Calculate the digital root of a number (1-9)."""
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

def clean_text(text):
    """Remove punctuation and convert to uppercase."""
    text = re.sub(r'[^\w\s\u0590-\u05FF]', '', text)  # Keep Hebrew characters
    return text.upper()

def classify_word(word, mapping):
    """Classify a word into A, B, or C based on its digital root."""
    total = 0
    for char in word:
        # Use mapping if character exists, otherwise default to 0
        total += mapping.get(char, 0)
    
    root = get_digital_root(total)
    
    if root in [3, 6, 9]:
        return 'A', root
    elif root in [1, 4, 7]:
        return 'B', root
    elif root in [2, 5, 8]:
        return 'C', root
    return 'Unknown', root

def analyze_text(text, mapping):
    """Analyze a block of text and return word classifications and roots."""
    cleaned = clean_text(text)
    words = cleaned.split()
    results = []
    
    for word in words:
        if not word.strip():
            continue
        category, root = classify_word(word, mapping)
        results.append({
            'word': word,
            'category': category,
            'root': root
        })
    return results

# ==========================================
# 3. EMOTIONAL & PROBABILITY MONITORS
# ==========================================

def analyze_emotional_tone(results):
    """Analyze emotional tone based on harmonic category distribution."""
    counts = {'A': 0, 'B': 0, 'C': 0}
    for r in results:
        if r['category'] in counts:
            counts[r['category']] += 1
            
    total = sum(counts.values())
    if total == 0:
        return "Neutral", "No words analyzed yet."
        
    p_a = counts['A'] / total
    p_b = counts['B'] / total
    p_c = counts['C'] / total
    
    if p_a > 0.5:
        return "Reflective / Spiritual", "High concentration of 3, 6, 9 roots suggests introspective or meditative tone."
    elif p_b > 0.5:
        return "Action-Oriented / Grounded", "High concentration of 1, 4, 7 roots suggests practical, physical, or structured tone."
    elif p_c > 0.5:
        return "Emotional / Expressive", "High concentration of 2, 5, 8 roots suggests relational, emotional, or creative tone."
    else:
        return "Balanced", "Even distribution across harmonic categories suggests a balanced emotional field."

def monitor_probability_expectance(results, user_expectance):
    """
    Monitor probability expectance and deserveance.
    Compares user expectance (0-100) with text coherence (percentage of A/B/C alignment).
    """
    counts = {'A': 0, 'B': 0, 'C': 0}
    for r in results:
        if r['category'] in counts:
            counts[r['category']] += 1
            
    total = sum(counts.values())
    if total == 0:
        return 0, "No text analyzed yet."
        
    # Coherence is defined as the dominance of the primary category
    max_count = max(counts.values())
    coherence = (max_count / total) * 100
    
    # Deserveance is the harmonic average of expectance and coherence
    deserveance = (user_expectance + coherence) / 2
    
    if deserveance > 80:
        status = "High Alignment: Your field is coherent and open to receive."
    elif deserveance > 50:
        status = "Moderate Alignment: Some distortion, but stable enough for integration."
    else:
        status = "Low Alignment: High expectation with low coherence may cause symbolic collapse."
        
    return deserveance, status

# ==========================================
# 4. STREAMLIT USER INTERFACE
# ==========================================

st.set_page_config(page_title="Harmonic Text Mirror", layout="centered")

st.title("🌀 Harmonic Text Mirror")
st.write("Map your words into harmonic recursion fields (A, B, C) and monitor your emotional and probability coherence.")

# Language Selection
language = st.selectbox("Select Language Mapping", ["English", "Hebrew"])
mapping = HEBREW_MAPPING if language == "Hebrew" else DEFAULT_MAPPING

# Text Input
user_text = st.text_area("Enter your text here:", height=150, placeholder="Type a sentence, a journal entry, or a mantra...")

# Expectance Slider (Probability Monitor)
st.subheader("💭 Probability Expectance Monitor")
user_expectance = st.slider(
    "How strongly do you expect your intention to manifest? (0 = None, 100 = Absolute)",
    min_value=0, max_value=100, value=50
)

if st.button("Analyze Text"):
    if user_text.strip():
        # Run Analysis
        results = analyze_text(user_text, mapping)
        
        # Display Results Table
        st.subheader("📊 Word Classification")
        table_data = []
        for r in results:
            table_data.append([r['word'], r['category'], r['root']])
        st.table(table_data)
        
        # Category Counts
        counts = {'A': 0, 'B': 0, 'C': 0}
        for r in results:
            if r['category'] in counts:
                counts[r['category']] += 1
                
        # Display Summary Metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Category A (3,6,9)", counts['A'])
        col2.metric("Category B (1,4,7)", counts['B'])
        col3.metric("Category C (2,5,8)", counts['C'])
        
        # Emotional Tone Analysis
        tone, tone_desc = analyze_emotional_tone(results)
        st.subheader("🎭 Emotional Tone")
        st.info(f"**{tone}**: {tone_desc}")
        
        # Probability Expectance Analysis
        deserveance, deserve_desc = monitor_probability_expectance(results, user_expectance)
        st.subheader("⚖️ Deserveance Score")
        st.success(f"**Score: {deserveance:.1f}%**\n\n{deserve_desc}")
        
        # Visualization (Bar Chart)
        st.subheader("📈 Harmonic Distribution")
        fig, ax = plt.subplots()
        categories = list(counts.keys())
        values = list(counts.values())
        colors = ['#ff9999', '#66b3ff', '#99ff99']
        
        ax.bar(categories, values, color=colors)
        ax.set_ylabel('Word Count')
        ax.set_title('Distribution of Harmonic Categories')
        st.pyplot(fig)
        
    else:
        st.warning("Please enter some text to analyze.")
      
