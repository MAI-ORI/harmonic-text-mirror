import streamlit as st
from harmonic_text_mapping import classify_word, get_digital_root

# Page Configuration
st.set_page_config(
    page_title="Harmonic Text Mirror",
    page_icon="🌀",
    layout="centered"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .main {
        background-color: #0d0d13;
        color: #e0e0e9;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3 {
        color: #9b5de5;
        text-align: center;
    }
    .stTextInput > div > div > input {
        background-color: #1a1a24;
        color: #00f5d4;
        border: 1px solid #9b5de5;
        border-radius: 8px;
        font-size: 18px;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #161622;
        border-left: 5px solid #00f5d4;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# App Title and Subtitle
st.title("🌀 Harmonic Text Mirror")
st.subheader("Map the vibrational signature of your words")

# User Input
user_input = st.text_input("Enter a word or phrase:", placeholder="Type here...")

if user_input:
    # Process input
    words = user_input.split()
    results = []
    
    for word in words:
        clean_word = "".join([c for c in word if c.isalnum()])
        if clean_word:
            root = get_digital_root(clean_word)
            classification = classify_word(clean_word)
            results.append((word, root, classification))
            
    # Display Results
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.write("### 🔍 Harmonic Analysis:")
    
    for word, root, classification in results:
        st.write(f"**{word}** → Digital Root: `{root}` | Class: `{classification}`")
        
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<br><hr><center><small>Harmonic Text Mirror • Built with Breath and Code</small></center>", unsafe_allow_html=True)
