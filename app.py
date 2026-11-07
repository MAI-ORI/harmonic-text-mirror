import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import re

# --- HARMONIC TEXT MIRROR CORE LOGIC ---

def digital_root(n):
    """Calculates the digital root of an integer."""
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def letter_to_value(char):
    """Maps a character to its numerological value (1-9) using Unicode-aware fallback."""
    char = char.lower()
    if 'a' <= char <= 'z':
        return (ord(char) - ord('a')) % 9 + 1
    elif '\u05d0' <= char <= '\u05ea':  # Hebrew Unicode range
        hebrew_values = {
            'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
            'י': 1, 'כ': 2, 'ל': 3, 'מ': 4, 'נ': 5, 'ס': 6, 'ע': 7, 'פ': 8, 'צ': 9,
            'ק': 1, 'ר': 2, 'ש': 3, 'ת': 4, 'ך': 2, 'ם': 4, 'ן': 5, 'ף': 8, 'ץ': 9
        }
        return hebrew_values.get(char, 0)
    else:
        # Unicode fallback: sum the bytes of the character and reduce to digital root
        byte_sum = sum(char.encode('utf-8'))
        return digital_root(byte_sum) if byte_sum > 0 else 0

def word_to_digital_root(word):
    """Calculates the digital root of a word based on its letters."""
    clean_word = re.sub(r'[^\w]', '', word)  # Remove punctuation
    total = sum(letter_to_value(char) for char in clean_word)
    return digital_root(total)

def classify_word(root):
    """Classifies a digital root into A, B, or C harmonic categories."""
    if root in [3, 6, 9]:
        return 'A'  # Triadic / Spiritual
    elif root in [1, 4, 7]:
        return 'B'  # Grounding / Structure
    elif root in [2, 5, 8]:
        return 'C'  # Emotional / Relational
    return 'Unknown'

def analyze_text(text):
    """Analyzes a block of text and returns word-level harmonic classifications."""
    words = text.split()
    analysis = []
    for word in words:
        root = word_to_digital_root(word)
        category = classify_word(root)
        analysis.append({
            'word': word,
            'root': root,
            'category': category
        })
    return analysis

# --- SYSTEM MODULES ---

class ProbabilityMonitor:
    """Probability Expectance and Deserveance Monitor"""
    def __init__(self):
        self.expectation_score = 5.0
        self.deserveance_score = 5.0

    def update_scores(self, text_length, coherence_score):
        # Simple heuristic: longer, more coherent text increases scores
        self.expectation_score = min(10.0, self.expectation_score + (text_length * 0.05))
        self.deserveance_score = min(10.0, self.deserveance_score + (coherence_score * 0.1))

    def get_status(self):
        combined = (self.expectation_score + self.deserveance_score) / 2
        if combined > 7.5:
            return "High Coherence Alignment — Manifestation Field Active"
        elif combined > 4.5:
            return "Stable Field — Keep Refining Intent"
        else:
            return "Low Coherence — Re-center Breath and Language"

class IntegrationModule:
    """Adjustment and Integration Module"""
    def apply_feedback(self, analysis):
        categories = [item['category'] for item in analysis]
        count_a = categories.count('A')
        count_b = categories.count('B')
        count_c = categories.count('C')
        
        suggestions = []
        if count_a > count_b + count_c:
            suggestions.append("Your text is highly abstract. Add more grounding words (B-class: roots 1, 4, 7).")
        elif count_b > count_a + count_c:
            suggestions.append("Your text is very structured. Add more emotional or spiritual words (A or C-class).")
        elif count_c > count_a + count_b:
            suggestions.append("Your text is highly emotional. Balance with structured logic or spiritual framing.")
        else:
            suggestions.append("Your text is harmonically balanced. No immediate adjustment needed.")
        return suggestions

# --- STREAMLIT INTERFACE ---

st.set_page_config(page_title="Harmonic Text Mirror", page_icon="🪞", layout="centered")

st.title("🪞 Harmonic Text Mirror")
st.write("Enter text to view its harmonic signature, emotional tone, and coherence alignment.")

# Initialize session state for modules
if 'monitor' not in st.session_state:
    st.session_state.monitor = ProbabilityMonitor()
if 'integrator' not in st.session_state:
    st.session_state.integrator = IntegrationModule()

# Text Input
user_text = st.text_area("Type or paste your text here:", height=150)

if st.button("Analyze"):
    if user_text.strip():
        analysis = analyze_text(user_text)
        
        # Display Results Table
        st.subheader("🔍 Word-by-Word Analysis")
        results_data = [{"Word": item['word'], "Digital Root": item['root'], "Category": item['category']} for item in analysis]
        st.table(results_data)
        
        # Category Counts
        categories = [item['category'] for item in analysis]
        count_a = categories.count('A')
        count_b = categories.count('B')
        count_c = categories.count('C')
        
        # Display Summary Metrics
        st.subheader("📊 Harmonic Distribution")
        col1, col2, col3 = st.columns(3)
        col1.metric("A (Spiritual/Triadic)", count_a)
        col2.metric("B (Grounding/Structure)", count_b)
        col3.metric("C (Emotional/Relational)", count_c)
        
        # Visualization
        fig, ax = plt.subplots()
        ax.bar(['A', 'B', 'C'], [count_a, count_b, count_c], color=['#88d4d6', '#f3b05a', '#f06c9b'])
        ax.set_ylabel('Word Count')
        ax.set_title('Text Harmonic Signature')
        st.pyplot(fig)
        
        # Update and Display Probability Monitor
        coherence_score = (count_a * 1.5 + count_b * 1.0 + count_c * 1.2) / max(1, len(analysis))
        st.session_state.monitor.update_scores(len(analysis), coherence_score)
        
        st.subheader("⚖️ Probability & Deserveance Monitor")
        st.info(st.session_state.monitor.get_status())
        
        # Display Integration Suggestions
        st.subheader("🔄 Adjustment & Integration Module")
        suggestions = st.session_state.integrator.apply_feedback(analysis)
        for suggestion in suggestions:
            st.warning(suggestion)
            
    else:
        st.error("Please enter some text to analyze.")
