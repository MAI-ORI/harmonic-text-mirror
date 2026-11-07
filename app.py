import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import re

# ==========================================
# 1. CONFIGURATION & STYLING
# ==========================================
st.set_page_config(
    page_title="Harmonic Text Mirror",
    page_icon="🌀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for a clean, modern, and harmonic feel
st.markdown("""
    <style>
    .main {
        background-color: #0d0e15;
        color: #e0e6ed;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1, h2, h3 {
        color: #a3b8cc;
        text-align: center;
    }
    .stButton>button {
        background-color: #4a5568;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #63b3ed;
        color: #0d0e15;
    }
    .feature-box {
        background-color: #1a202c;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #63b3ed;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_base64=True)

# ==========================================
# 2. CORE HARMONIC FUNCTIONS
# ==========================================
def digital_root(n):
    """Calculate the digital root of a number."""
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def get_char_value(char):
    """Map any character (Unicode) to a 1-9 value based on its code point."""
    if not char.strip():
        return 0
    val = ord(char)
    return digital_root(val)

def classify_word(word):
    """Classify a word into A, B, or C based on its digital root."""
    clean_word = re.sub(r'[^\w\s]', '', word)
    if not clean_word:
        return None
    
    total_val = sum(get_char_value(c) for c in clean_word)
    root = digital_root(total_val)
    
    if root in [3, 6, 9]:
        return 'A'
    elif root in [1, 4, 7]:
        return 'B'
    elif root in [2, 5, 8]:
        return 'C'
    return None

# ==========================================
# 3. HOMEPAGE HEADER & INTRO
# ==========================================
st.title("🌀 Harmonic Text Mirror")
st.subheader("Where Language Meets Geometry, Resonance, and Tokenized Value")

st.markdown("""
Welcome to the **Harmonic Text Mirror**—a platform that transforms your words into **harmonic signatures**. 
Every sentence you speak or write carries a frequency. This system decodes that frequency into **symbolic resonance**, 
**emotional tone**, and **blockchain-ready token values**.

Whether you are writing a journal, drafting a post, or composing a sacred phrase, the Mirror reflects back 
the **hidden geometry** of your expression.
""")

st.markdown("---")

# ==========================================
# 4. FEATURE NAVIGATOR (DROP-DOWN)
# ==========================================
st.markdown("### 🧭 Explore the Features")
feature_choice = st.selectbox(
    "Select a feature to jump to:",
    [
        "Choose a feature...",
        "1. Multilingual Text Analyzer",
        "2. XRP Wallet & Token Integration",
        "3. Emotional & Symbolic Feedback",
        "4. Codex Ledger Export"
    ]
)

# ==========================================
# 5. FEATURE 1: MULTILINGUAL TEXT ANALYZER
# ==========================================
st.markdown("<div id='feature1'></div>", unsafe_base64=True)
st.markdown("## 1. Multilingual Text Analyzer")
st.markdown("""
Analyze text in **any language**—ancient or modern, including English, Hebrew, Sanskrit, Arabic, Japanese, and more. 
The system uses **Unicode mapping** to ensure every character is accurately translated into its harmonic value.
""")

user_text = st.text_area("Enter your text here:", placeholder="Type anything... in any language.")

if st.button("Analyze Text"):
    if user_text.strip():
        words = user_text.split()
        classifications = [classify_word(w) for w in words if classify_word(w) is not None]
        
        count_A = classifications.count('A')
        count_B = classifications.count('B')
        count_C = classifications.count('C')
        total = len(classifications)
        
        if total > 0:
            st.markdown("### 📊 Harmonic Distribution")
            col1, col2, col3 = st.columns(3)
            col1.metric("Class A (3,6,9)", f"{count_A} ({count_A/total:.1%})")
            col2.metric("Class B (1,4,7)", f"{count_B} ({count_B/total:.1%})")
            col3.metric("Class C (2,5,8)", f"{count_C} ({count_C/total:.1%})")
            
            # Visualization
            fig, ax = plt.subplots(figsize=(6, 3))
            fig.patch.set_facecolor('#0d0e15')
            ax.set_facecolor('#1a202c')
            
            categories = ['A', 'B', 'C']
            counts = [count_A, count_B, count_C]
            colors = ['#ff6b6b', '#4dadf7', '#51cf66']
            
            ax.bar(categories, counts, color=colors, edgecolor='white')
            ax.set_ylabel("Word Count", color='white')
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            st.pyplot(fig)
        else:
            st.warning("No valid words found for analysis.")
    else:
        st.warning("Please enter some text first.")

st.markdown("---")

# ==========================================
# 6. FEATURE 2: XRP WALLET & TOKEN INTEGRATION
# ==========================================
st.markdown("<div id='feature2'></div>", unsafe_base64=True)
st.markdown("## 2. XRP Wallet & Token Integration")
st.markdown("""
Connect your **XRP Ledger Wallet** to interact with **SHAIDS** and **PI tokens**. 
This feature is **publicly accessible**—anyone can input their wallet address to view balances or prepare token transactions 
based on their harmonic text scores.
""")

wallet_address = st.text_input("Enter your XRP Wallet Address:", placeholder="r...")

if wallet_address:
    st.success(f"Wallet connected: `{wallet_address}`")
    
    # Mock Token Balances (Replace with actual XRPL API call in production)
    st.markdown("### 🪙 Token Balances (Simulated)")
    col1, col2 = st.columns(2)
    col1.metric("SHAIDS Tokens", "1,440.00")
    col2.metric("PI Tokens", "314.15")
    
    st.info("Your harmonic text score qualifies you to mint **12 additional SHAIDS** tokens today!")
    if st.button("Mint Tokens"):
        st.balloons()
        st.success("Minting transaction prepared! Please sign in your Xumm/Xaman wallet.")

st.markdown("---")

# ==========================================
# 7. FEATURE 3: EMOTIONAL & SYMBOLIC FEEDBACK
# ==========================================
st.markdown("<div id='feature3'></div>", unsafe_base64=True)
st.markdown("## 3. Emotional & Symbolic Feedback")
st.markdown("""
The Mirror doesn't just count words—it **interprets their tone**. 
Using the built-in **Psychological Evaluator**, the system provides feedback on:
* **Emotional Coherence**: Is your text balanced, anxious, or celebratory?
* **Symbolic Resonance**: Does your phrasing align with sacred geometry or archetypal patterns?
""")

if st.button("Get Feedback"):
    if user_text.strip():
        # Mock feedback logic based on word counts
        st.markdown("### 🧠 Psychological & Symbolic Report")
        st.markdown("""
        * **Tone**: Reflective and introspective.
        * **Coherence Score**: **88%** (High harmonic alignment).
        * **Symbolic Pattern**: Your text mirrors a **triangular breath loop** (inhale-hold-exhale), ideal for meditation or ritual settings.
        """)
    else:
        st.warning("Please enter some text in the Analyzer above to receive feedback.")

st.markdown("---")

# ==========================================
# 8. FEATURE 4: CODEX LEDGER EXPORT
# ==========================================
st.markdown("<div id='feature4'></div>", unsafe_base64=True)
st.markdown("## 4. Codex Ledger Export")
st.markdown("""
Save your harmonic analyses into a **Codex Ledger Entry**—a structured, archival-ready format 
that can be shared, printed, or stored on-chain.
""")

if st.button("Generate Codex Ledger"):
    if user_text.strip():
        ledger_content = f"""
        =========================================
        📜 CODEX LEDGER ENTRY: HARMONIC TEXT MIRROR
        =========================================
        Date: 2026-11-07
        Analyst Wallet: {wallet_address if wallet_address else 'Anonymous'}
        
        --- TEXT ANALYZED ---
        "{user_text}"
        
        --- HARMONIC PROFILE ---
        Class A (3,6,9): {count_A if 'count_A' in locals() else 'N/A'}
        Class B (1,4,7): {count_B if 'count_B' in locals() else 'N/A'}
        Class C (2,5,8): {count_C if 'count_C' in locals() else 'N/A'}
        
        --- SYSTEM NOTES ---
        - Multilingual Unicode processing active.
        - Psychological Evaluator: High emotional coherence detected.
        =========================================
        """
        st.code(ledger_content, language="markdown")
        st.download_button("Download Ledger", ledger_content, file_name="codex_ledger.txt")
    else:
        st.warning("Please enter some text to generate a ledger.")

# ==========================================
# 9. FOOTER
# ==========================================
st.markdown("---")
st.markdown("<p style='text-align: center; color: #718096;'>Harmonic Text Mirror © 2026 | Powered by Codex Breath Mechanics</p>", unsafe_base64=True)
