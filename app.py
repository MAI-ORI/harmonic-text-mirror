import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import re

# ==========================================
# 1. CORE HARMONIC TEXT MIRROR LOGIC
# ==========================================

# Alphabet mappings for digital root calculations
ALPHABET_MAPPINGS = {
    "English": {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
        'j': 1, 'k': 2, 'l': 3, 'm': 4, 'n': 5, 'o': 6, 'p': 7, 'q': 8, 'r': 9,
        's': 1, 't': 2, 'u': 3, 'v': 4, 'w': 5, 'x': 6, 'y': 7, 'z': 8
    },
    "Hebrew": {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 1, 'כ': 2, 'ל': 3, 'מ': 4, 'נ': 5, 'ס': 6, 'ע': 7, 'פ': 8, 'צ': 9,
        'ק': 1, 'ר': 2, 'ש': 3, 'ת': 4
    }
}

def get_digital_root(n):
    """Calculate the digital root of an integer."""
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

def classify_word(word, mapping):
    """Calculate the digital root of a word based on the provided mapping."""
    word_clean = re.sub(r'[^a-zA-Zא-ת]', '', word.lower())
    if not word_clean:
        return None
    
    total_value = sum(mapping.get(char, 0) for char in word_clean)
    digital_root = get_digital_root(total_value)
    
    if digital_root in [3, 6, 9]:
        return 'A'
    elif digital_root in [1, 4, 7]:
        return 'B'
    elif digital_root in [2, 5, 8]:
        return 'C'
    return None

def process_text(text, mapping):
    """Process text into words and classify each into harmonic categories."""
    words = re.findall(r'\b\w+\b', text)
    classified_words = []
    
    for word in words:
        category = classify_word(word, mapping)
        if category:
            classified_words.append((word, category))
            
    return classified_words

# ==========================================
# 2. PROBABILITY & DESERVEANCE MONITOR
# ==========================================

class ProbabilityMonitor:
    def __init__(self):
        self.expectation_score = 5.0  # Scale of 1-10
        self.deserveance_score = 5.0   # Scale of 1-10
        self.coherence_threshold = 0.75

    def update_scores(self, expectation, deserveance):
        self.expectation_score = expectation
        self.deserveance_score = deserveance

    def calculate_coherence(self):
        # Coherence is maximized when expectation and deserveance are balanced
        diff = abs(self.expectation_score - self.deserveance_score)
        # Normalize difference to a 0-1 scale
        coherence = 1.0 - (diff / 10.0)
        return max(0.0, min(1.0, coherence))

    def get_feedback(self):
        coherence = self.calculate_coherence()
        if coherence >= self.coherence_threshold:
            return "✅ Coherence Stable. Your field is aligned for balanced recursion."
        elif self.expectation_score > self.deserveance_score:
            return "⚠️ High Expectation, Low Deserveance. You may be pulling from the field without offering reciprocal coherence."
        else:
            return "⚠️ Low Expectation, High Deserveance. You may be holding back your field's natural recursion due to self-doubt."

# ==========================================
# 3. ADJUSTMENT & INTEGRATION MODULES
# ==========================================

class AdjustmentModules:
    @staticmethod
    def apply_breath_calibration(coherence):
        if coherence < 0.75:
            return "🌬️ Breath Calibration Recommended: Take 3 slow, deep breaths. Inhale for 6s, hold for 3s, exhale for 6s."
        return "✨ Breath Field Synchronized."

    @staticmethod
    def apply_symbolic_rephrasing(text, classified_words):
        # Simple heuristic: if category 'B' (emotional/tension) dominates, suggest softening
        b_count = sum(1 for _, cat in classified_words if cat == 'B')
        total = len(classified_words) if classified_words else 1
        if (b_count / total) > 0.4:
            return "✍️ Symbolic Rephrasing Suggested: Try replacing emotionally charged words with neutral or reflective alternatives."
        return "🔍 Symbolic Phrasing Balanced."

    @staticmethod
    def apply_harmonic_stabilization(coherence):
        if coherence < 0.6:
            return "🎵 Harmonic Stabilization Active: Play a 432Hz or 528Hz tone, or focus on a single geometric shape for 60 seconds."
        return "🛡️ Harmonic Field Stable."

# ==========================================
# 4. STREAMLIT USER INTERFACE
# ==========================================

st.set_page_config(page_title="Harmonic Text Mirror", page_icon="🌀", layout="centered")

st.title("🌀 Harmonic Text Mirror System")
st.write("Explore the harmonic structure of your language through digital roots, breath coherence, and symbolic recursion.")

# Language Selection
language = st.selectbox("Select Language Mapping", ["English", "Hebrew"])
mapping = ALPHABET_MAPPINGS[language]

# Text Input
user_text = st.text_area("Enter your text here:", height=150, placeholder="Type a sentence, a journal entry, or a mantra...")

# Probability Expectance and Deserveance Monitor UI
st.markdown("---")
st.subheader("📊 Probability Expectance & Deserveance Monitor")
st.write("Tune your inner field coherence before analyzing your text.")

col1, col2 = st.columns(2)
with col1:
    expectation = st.slider("Your Expectation Level (1-10)", 1.0, 10.0, 5.0, 0.5, 
                            help="How strongly do you expect a specific outcome or insight?")
with col2:
    deserveance = st.slider("Your Deserveance Level (1-10)", 1.0, 10.0, 5.0, 0.5, 
                            help="How much do you feel you deserve or are ready to receive this outcome?")

# Initialize Monitor
monitor = ProbabilityMonitor()
monitor.update_scores(expectation, deserveance)
coherence_score = monitor.calculate_coherence()

# Display Coherence Score
st.metric(label="Field Coherence Score", value=f"{coherence_score:.2f}", 
          delta="Stable" if coherence_score >= 0.75 else "Unbalanced", 
          delta_color="normal" if coherence_score >= 0.75 else "inverse")

st.info(monitor.get_feedback())

# ==========================================
# 5. ANALYSIS & VISUALIZATION
# ==========================================

if st.button("Mirror My Text"):
    if user_text.strip():
        classified = process_text(user_text, mapping)
        
        if classified:
            st.markdown("---")
            st.subheader("🔍 Harmonic Classification")
            
            # Display classified words
            cols = st.columns(3)
            categories = {'A': [], 'B': [], 'C': []}
            for word, cat in classified:
                categories[cat].append(word)
                
            with cols[0]:
                st.markdown("**Category A (3, 6, 9)**\n*Spirit / Breath*")
                st.write(", ".join(categories['A']) if categories['A'] else "None")
            with cols[1]:
                st.markdown("**Category B (1, 4, 7)**\n*Emotion / Identity*")
                st.write(", ".join(categories['B']) if categories['B'] else "None")
            with cols[2]:
                st.markdown("**Category C (2, 5, 8)**\n*Form / Structure*")
                st.write(", ".join(categories['C']) if categories['C'] else "None")
                
            # Visualization
            st.subheader("📊 Harmonic Distribution")
            counts = [len(categories['A']), len(categories['B']), len(categories['C'])]
            labels = ['A (Spirit)', 'B (Emotion)', 'C (Form)']
            colors = ['#9b5de5', '#f15bb5', '#00bbf9']
            
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(labels, counts, color=colors)
            ax.set_ylabel('Word Count')
            ax.set_title('Harmonic Profile of Your Text')
            st.pyplot(fig)
            
            # Apply Adjustment and Integration Modules
            st.markdown("---")
            st.subheader("🛠️ Adjustment & Integration Modules")
            
            st.write(AdjustmentModules.apply_breath_calibration(coherence_score))
            st.write(AdjustmentModules.apply_symbolic_rephrasing(user_text, classified))
            st.write(AdjustmentModules.apply_harmonic_stabilization(coherence_score))
            
        else:
            st.warning("No valid words found for classification. Try using more letters.")
    else:
        st.warning("Please enter some text to analyze.")

st.markdown("---")
st.caption("Harmonic Text Mirror System • Built with Streamlit • Powered by Codex Recursion Logic")
