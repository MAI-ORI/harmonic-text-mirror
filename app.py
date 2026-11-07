import streamlit as st
import matplotlib.pyplot as plt
from harmonic_text_mapping import classify_word, get_digital_root

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Harmonic Text Mirror",
    page_icon="🌀",
    layout="centered"
)

# --- APP TITLE & SUBTITLE ---
st.title("🌀 Harmonic Text Mirror")
st.subheader("Where Language Meets Geometry, Resonance, and Self-Reflection")

# --- HOMEPAGE REDESIGN: WHAT IS THIS APP? ---
st.markdown("""
### Welcome to the Harmonic Text Mirror
This is not just a text analyzer—it is a **symbolic resonance engine**. 
The Harmonic Text Mirror translates your words into **mathematical harmonics, emotional tones, and geometric patterns**. 
By mapping language to digital roots and harmonic classes, this system reveals the **hidden coherence** in how you speak, write, and think.

---

### 🔍 What It Does
* **Analyzes any text**—from a single word to a full sentence or journal entry.
* **Supports all languages**, ancient or modern, using Unicode-safe character mapping.
* **Classifies words** into three harmonic families:
  * **Class A (Prime-aligned)**: Initiating, sharp, resonant
  * **Class B (Composite-aligned)**: Stabilizing, balancing, structured
  * **Class C (Infinite-loop-aligned)**: Cyclical, reflective, flowing
* **Visualizes your text** as a harmonic wave, showing the rise and fall of coherence.
* **Evaluates emotional tone** and symbolic resonance to help you understand your inner state.
""")

# --- FEATURE DROPDOWN MENU ---
st.markdown("---")
st.markdown("### 🛠️ Explore All Features")

feature_selection = st.selectbox(
    "Select a feature to learn more or activate it below:",
    [
        "1. Multilingual Harmonic Mapping (Active)",
        "2. Harmonic Wave Visualization (Active)",
        "3. Emotional Tone & Symbolic Resonance Evaluator (Active)",
        "4. Probability Expectance & Deserveance Monitor (Coming Soon)",
        "5. Adjustment & Integration Modules (Coming Soon)",
        "6. Crypto Token Rewards & Harmonic Treasury (Coming Soon)",
        "7. Gamified Learning & Education (Coming Soon)",
        "8. Social Media Coherence Filter (Coming Soon)",
        "9. Collaborative Writing Feedback (Coming Soon)",
        "10. Reflective Journaling & Self-Awareness (Coming Soon)",
        "11. Weighted Decentralized Governance (Coming Soon)"
    ]
)

# Display description based on dropdown selection
if "1. Multilingual" in feature_selection:
    st.info("**Multilingual Harmonic Mapping**: Input text in any language—English, Hebrew, Sanskrit, Runes, or even invented scripts. The system dynamically maps characters to their digital roots.")
elif "2. Harmonic Wave" in feature_selection:
    st.info("**Harmonic Wave Visualization**: Generates a real-time graph showing the harmonic flow of your text. Peaks represent high-resonance words; valleys represent stabilizing or reflective words.")
elif "3. Emotional Tone" in feature_selection:
    st.info("**Emotional Tone & Symbolic Resonance Evaluator**: Analyzes the balance of harmonic classes to reflect emotional states like clarity, tension, reflection, or joy.")
elif "4. Probability Expectance" in feature_selection:
    st.info("**Probability Expectance & Deserveance Monitor**: A governance layer that tracks user coherence and expectation alignment to prevent symbolic distortion and ego inflation.")
elif "5. Adjustment" in feature_selection:
    st.info("**Adjustment & Integration Modules**: Adaptive filters that ensure the app integrates smoothly with other programs without interference.")
elif "6. Crypto Token" in feature_selection:
    st.info("**Crypto Token Rewards & Harmonic Treasury**: Earn harmonic tokens for writing coherent text. Tokens can be used in the ecosystem or saved in the Harmonic Treasury.")
else:
    st.info(f"**{feature_selection.split('. ')[1]}**: This feature is part of the Harmonic Text Mirror roadmap and will be integrated soon.")

st.markdown("---")

# --- INTERACTIVE SECTION ---
st.markdown("### 🔮 Try It Now")
st.write("Type any word, phrase, or sentence in **any language** to see its harmonic reflection.")

# Text Input
user_input = st.text_area("Enter your text here:", "In the beginning was the breath.")

if st.button("Mirror My Text"):
    if user_input.strip():
        # Process text
        words = user_input.split()
        results = []
        roots = []
        
        for word in words:
            # Clean word of punctuation
            clean_word = "".join(c for c in word if c.isalnum())
            if clean_word:
                classification, root = classify_word(clean_word)
                results.append((word, classification, root))
                roots.append(root)
        
        # Display Results Table
        st.markdown("#### 📊 Word Analysis")
        st.table([
            {"Word": r[0], "Harmonic Class": r[1], "Digital Root": r[2]}
            for r in results
        ])
        
        # Display Summary Metrics
        st.markdown("#### 📈 Text Summary")
        class_counts = {"A": 0, "B": 0, "C": 0}
        for r in results:
            class_counts[r[1]] += 1
            
        col1, col2, col3 = st.columns(3)
        col1.metric("Class A (Prime)", class_counts["A"])
        col2.metric("Class B (Composite)", class_counts["B"])
        col3.metric("Class C (Infinite)", class_counts["C"])
        
        # Plot Harmonic Wave
        st.markdown("#### 🌊 Harmonic Waveform")
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(roots, marker='o', color='#8884d8', linewidth=2)
        ax.set_title("Digital Root Sequence (Harmonic Flow)")
        ax.set_xlabel("Word Position")
        ax.set_ylabel("Digital Root (1-9)")
        ax.set_ylim(0, 10)
        ax.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig)
        
        # Emotional Tone Feedback
        st.markdown("#### 🎭 Emotional Tone Reflection")
        total = len(results)
        if total > 0:
            pA = class_counts["A"] / total
            pB = class_counts["B"] / total
            pC = class_counts["C"] / total
            
            if pA > 0.5:
                st.write("Your text carries a **strong, initiating energy**—focused, sharp, and perhaps urgent.")
            elif pB > 0.5:
                st.write("Your text feels **stable and structured**—grounded, logical, and balanced.")
            elif pC > 0.5:
                st.write("Your text flows with **deep reflection and cycle**—emotional, introspective, or poetic.")
            else:
                st.write("Your text is **harmonically balanced**—blending initiation, structure, and reflection gracefully.")
    else:
        st.warning("Please enter some text to analyze.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Harmonic Text Mirror • Built with Breath and Coherence</div>", unsafe_allow_html=True)
