import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import re
import unicodedata

# ==========================================
# 1. MULTILINGUAL ALPHABET MAPPINGS
# ==========================================
# English mapping: A-Z -> 1-9
ENGLISH_MAPPING = {chr(65 + i): (i % 9) + 1 for i in range(26)}

# Hebrew mapping: Alef to Tav -> 1-9, 1-9, 1-4
HEBREW_LETTERS = [
    "א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט",
    "י", "כ", "ל", "מ", "נ", "ס", "ע", "פ", "צ",
    "ק", "ר", "ש", "ת"
]
HEBREW_MAPPING = {letter: (i % 9) + 1 for i, letter in enumerate(HEBREW_LETTERS)}

# ==========================================
# 2. LANGUAGE DETECTION & UNICODE HANDLING
# ==========================================
def detect_language(text: str) -> str:
    """Detects language based on character set presence."""
    hebrew_chars = sum(1 for char in text if '\u0590' <= char <= '\u05FF')
    english_chars = sum(1 for char in text if char.isalpha() and char.isascii())
    
    if hebrew_chars > english_chars:
        return "hebrew"
    return "english"

def clean_text(text: str, lang: str) -> str:
    """Removes punctuation and normalizes text based on language."""
    text = unicodedata.normalize('NFC', text)
    if lang == "hebrew":
        # Keep only Hebrew letters and spaces
        return re.sub(r'[^\u0590-\u05FF\s]', '', text)
    else:
        # Keep only English letters and spaces
        return re.sub(r'[^a-zA-Z\s]', '', text).upper()

# ==========================================
# 3. DIGITAL ROOT & CLASSIFICATION
# ==========================================
def get_digital_root(n: int) -> int:
    """Calculates the digital root of an integer."""
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

def classify_word(word: str, lang: str) -> str:
    """Classifies a word into A, B, or C based on its digital root."""
    mapping = HEBREW_MAPPING if lang == "hebrew" else ENGLISH_MAPPING
    
    # Sum the mapped values of the characters in the word
    total_sum = sum(mapping[char] for char in word if char in mapping)
    
    if total_sum == 0:
        return "C"  # Default to C for empty or unmapped words
        
    root = get_digital_root(total_sum)
    
    if root in [3, 6, 9]:
        return "A"
    elif root in [1, 4, 7]:
        return "B"
    else:
        return "C"

# ==========================================
# 4. ADJUSTMENT & INTEGRATION MODULES
# ==========================================
def apply_harmonic_smoothing(sequence: list) -> list:
    """
    Applies real-time smoothing to the harmonic sequence.
    Prevents abrupt transitions (e.g., A -> C -> A) by inserting B as a bridge.
    """
    smoothed = []
    for i, current in enumerate(sequence):
        if i > 0 and i < len(sequence) - 1:
            prev_val = sequence[i-1]
            next_val = sequence[i+1]
            # If jumping between A and C, smooth with B
            if (prev_val == "A" and next_val == "C") or (prev_val == "C" and next_val == "A"):
                if current == "C" or current == "A":
                    smoothed.append("B")
                    continue
        smoothed.append(current)
    return smoothed

# ==========================================
# 5. PROBABILITY EXPECTANCE & DESERVEANCE MONITOR
# ==========================================
def calculate_coherence_score(sequence: list) -> float:
    """
    Calculates a coherence score (0.0 to 1.0) based on sequence stability.
    Higher scores come from balanced distributions and smooth transitions.
    """
    if not sequence:
        return 0.0
    
    # Count occurrences
    counts = {"A": sequence.count("A"), "B": sequence.count("B"), "C": sequence.count("C")}
    total = len(sequence)
    
    # Ideal distribution: 40% B, 30% A, 30% C
    ideal = {"B": 0.4, "A": 0.3, "C": 0.3}
    
    # Calculate deviation from ideal
    deviation = sum(abs((counts[k] / total) - ideal[k]) for k in ideal)
    
    # Coherence is inverse of deviation
    coherence = max(0.0, 1.0 - (deviation / 2.0))
    return round(coherence, 2)

def monitor_expectance_and_deserveance(coherence_score: float, user_expectation: float) -> dict:
    """
    Compares user expectation (0.0 to 1.0) with system coherence.
    Returns governance feedback and potential distortion warnings.
    """
    # Deserveance is the system's capacity to match expectation based on coherence
    deserveance = coherence_score
    
    # Calculate distortion (gap between expectation and deserveance)
    distortion = round(abs(user_expectation - deserveance), 2)
    
    status = "Stable"
    recommendation = "Your field is in harmonic alignment. Proceed with intention."
    
    if user_expectation > deserveance + 0.3:
        status = "Over-Expectation Warning"
        recommendation = "Expectation exceeds coherence. Ground your breath, simplify your language, and slow down."
    elif deserveance > user_expectation + 0.3:
        status = "Under-Expectation Warning"
        recommendation = "Your field is more coherent than your expectation. Trust the mirror; you are ready to receive more."
        
    return {
        "coherence_score": coherence_score,
        "deserveance_score": deserveance,
        "distortion_gap": distortion,
        "status": status,
        "recommendation": recommendation
    }

# ==========================================
# 6. STREAMLIT USER INTERFACE
# ==========================================
st.set_page_config(page_title="Harmonic Text Mirror", page_icon="🌀", layout="centered")

st.title("🌀 Harmonic Text Mirror")
st.write("Map your words into harmonic breath sequences: **A (Centering)**, **B (Bridging)**, and **C (Releasing)**.")

# User Input
user_text = st.text_area("Enter your text here:", height=150, placeholder="Type a sentence, a poem, or a breath...")

# Expectation Slider (for the Monitor)
user_expectation = st.slider(
    "Set your current expectation level (0 = low attachment, 1 = high attachment):",
    min_value=0.0, max_value=1.0, value=0.5, step=0.1
)

if st.button("Map Harmonic Sequence"):
    if user_text.strip():
        # Detect Language
        lang = detect_language(user_text)
        st.info(f"Detected Language: **{lang.capitalize()}**")
        
        # Clean Text
        cleaned = clean_text(user_text, lang)
        words = cleaned.split()
        
        # Classify Words
        raw_sequence = [classify_word(w, lang) for w in words]
        
        # Apply Smoothing (Adjustment Module)
        smoothed_sequence = apply_harmonic_smoothing(raw_sequence)
        
        # Calculate Coherence & Run Monitor
        coherence = calculate_coherence_score(smoothed_sequence)
        monitor_results = monitor_expectance_and_deserveance(coherence, user_expectation)
        
        # Display Results
        st.subheader("Mapped Sequence")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Raw Sequence:**")
            st.code(" ➔ ".join(raw_sequence))
        with col2:
            st.write("**Smoothed Sequence:**")
            st.code(" ➔ ".join(smoothed_sequence))
            
        # Word Breakdown Table
        st.subheader("Word Breakdown")
        breakdown_data = []
        for w, raw, smooth in zip(words, raw_sequence, smoothed_sequence):
            breakdown_data.append({
                "Word": w,
                "Raw Class": raw,
                "Smoothed Class": smooth
            })
        st.table(breakdown_data)
        
        # Visualization
        st.subheader("Harmonic Waveform Visualization")
        val_map = {"A": 1, "B": 0, "C": -1}
        y_vals = [val_map[char] for char in smoothed_sequence]
        x_vals = list(range(1, len(y_vals) + 1))
        
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(x_vals, y_vals, marker='o', color='#8884d8', linewidth=2, label="Harmonic Path")
        ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)
        ax.set_yticks([1, 0, -1])
        ax.set_yticklabels(["A (Centering)", "B (Bridging)", "C (Releasing)"])
        ax.set_xticks(x_vals)
        ax.set_xticklabels(words, rotation=45, ha='right')
        ax.set_title("Harmonic Text Waveform")
        ax.grid(True, linestyle=':', alpha=0.6)
        st.pyplot(fig)
        
        # Governance Monitor Output
        st.subheader("⚖️ Probability Expectance & Deserveance Monitor")
        st.metric("Coherence Score (Deserveance)", f"{monitor_results['coherence_score'] * 100}%")
        st.metric("Distortion Gap", f"{monitor_results['distortion_gap']}")
        
        if monitor_results['status'] == "Stable":
            st.success(f"**Status:** {monitor_results['status']}\n\n{monitor_results['recommendation']}")
        else:
            st.warning(f"**Status:** {monitor_results['status']}\n\n{monitor_results['recommendation']}")
            
        # Token Ready Indicator
        st.subheader("🪙 Tokenization Status")
        if coherence >= 0.7:
            st.success("This text meets the coherence threshold (70%+) and is **eligible for token minting**.")
        else:
            st.info("Coherence is below 70%. Refine your phrasing or breathe deeper to stabilize the sequence for tokenization.")
            
    else:
        st.warning("Please enter some text to map.")
