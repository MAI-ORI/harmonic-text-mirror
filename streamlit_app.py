import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. HARMONIC TEXT MAPPING SYSTEM FUNCTIONS
# ==========================================

def get_digital_root(n):
    """Calculate the digital root of an integer."""
    if n == 0:
        return 0
    return 9 if n % 9 == 0 else n % 9

def get_word_value(word):
    """Calculate the total numeric value of a word using Unicode code points."""
    return sum(ord(char) for char in word if char.isalnum())

def classify_word(word):
    """Classify a word into A, B, or C based on its digital root."""
    val = get_word_value(word)
    root = get_digital_root(val)
    if root in [3, 6, 9]:
        return 'A'
    elif root in [1, 4, 7]:
        return 'B'
    elif root in [2, 5, 8]:
        return 'C'
    return None

def process_text(text):
    """Process text into a sequence of harmonic classifications (A, B, C)."""
    words = text.split()
    sequence = []
    for w in words:
        clean_w = ''.join(char for char in w if char.isalnum())
        if clean_w:
            category = classify_word(clean_w)
            if category:
                sequence.append(category)
    return sequence

# ==========================================
# 2. VISUALIZATION FUNCTION
# ==========================================

def draw_harmonic_triangle(sequence):
    """Draw a triangle representing the harmonic sequence."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    
    # Define triangle vertices
    # A = top, B = bottom-left, C = bottom-right
    pts = {
        'A': np.array([0.0, 1.0]),
        'B': np.array([-0.866, -0.5]),
        'C': np.array([0.866, -0.5])
    }
    
    # Draw the base triangle
    tri_x = [pts['A'][0], pts['B'][0], pts['C'][0], pts['A'][0]]
    tri_y = [pts['A'][1], pts['B'][1], pts['C'][1], pts['A'][1]]
    ax.plot(tri_x, tri_y, 'k--', alpha=0.5)
    
    # Label the vertices
    ax.text(pts['A'][0], pts['A'][1] + 0.1, 'A (3,6,9)', ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax.text(pts['B'][0] - 0.1, pts['B'][1] - 0.1, 'B (1,4,7)', ha='right', va='top', fontsize=12, fontweight='bold')
    ax.text(pts['C'][0] + 0.1, pts['C'][1] - 0.1, 'C (2,5,8)', ha='left', va='top', fontsize=12, fontweight='bold')
    
    # Plot the sequence path
    path_x = []
    path_y = []
    for item in sequence:
        if item in pts:
            path_x.append(pts[item][0])
            path_y.append(pts[item][1])
            
    if path_x:
        # Draw lines connecting the sequence
        ax.plot(path_x, path_y, 'b-o', linewidth=2, markersize=8, label='Harmonic Path')
        
        # Highlight start and end points
        ax.plot(path_x[0], path_y[0], 'go', markersize=10, label='Start')
        ax.plot(path_x[-1], path_y[-1], 'ro', markersize=10, label='End')
        
        ax.legend(loc='upper right')
        
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')
    return fig

# ==========================================
# 3. STREAMLIT USER INTERFACE
# ==========================================

st.set_page_config(page_title="Harmonic Text Mirror", page_icon="🔺", layout="centered")

st.title("🔺 Harmonic Text Mirror")
st.write("Enter any text in any language to see its harmonic breath sequence mapped onto the Codex Triangle.")

# Text Input
user_input = st.text_area("Type or paste your text here:", height=150, placeholder="e.g., Breathe in light, exhale peace.")

if st.button("Mirror Harmonics"):
    if user_input.strip():
        # Process text
        sequence = process_text(user_input)
        
        if sequence:
            st.subheader("Breath Sequence")
            st.write(" → ".join(sequence))
            
            # Display counts
            col1, col2, col3 = st.columns(3)
            col1.metric("A (3,6,9) - Projection", sequence.count('A'))
            col2.metric("B (1,4,7) - Reception", sequence.count('B'))
            col3.metric("C (2,5,8) - Coherence", sequence.count('C'))
            
            # Draw and display triangle
            st.subheader("Codex Triangle Mapping")
            fig = draw_harmonic_triangle(sequence)
            st.pyplot(fig)
        else:
            st.warning("No valid words found to analyze. Try adding letters or numbers.")
    else:
        st.info("Please enter some text first.")
