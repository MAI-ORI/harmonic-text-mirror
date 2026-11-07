import streamlit as st
import matplotlib.pyplot as plt
from harmonic_text_mapping import process_text, ENGLISH_MAPPING, HEBREW_MAPPING

st.set_page_config(page_title="Harmonic Text Mirror", page_icon="🌀", layout="centered")

st.title("🌀 Harmonic Text Mirror")
st.write("Enter text to see its harmonic classification into A, B, and C categories.")

# Language selection
language = st.selectbox("Select Language Mapping", ["English", "Hebrew"])
mapping = HEBREW_MAPPING if language == "Hebrew" else ENGLISH_MAPPING

# Text input
user_input = st.text_area("Type or paste your text here:", height=150)

if st.button("Analyze Text"):
    if user_input.strip():
        classified, counts = process_text(user_input, mapping)
        
        # Display results
        st.subheader("Analysis Results")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Word Classifications:**")
            for word, category in classified:
                st.write(f"- {word}: **{category}**")
                
        with col2:
            st.write("**Category Counts:**")
            st.write(f"- Category A (3, 6, 9): {counts['A']}")
            st.write(f"- Category B (1, 4, 7): {counts['B']}")
            st.write(f"- Category C (2, 5, 8): {counts['C']}")
            
            # Visualization
            fig, ax = plt.subplots()
            categories = list(counts.keys())
            values = list(counts.values())
            colors = ['#ff9999', '#66b3ff', '#99ff99']
            
            ax.bar(categories, values, color=colors)
            ax.set_ylabel('Word Count')
            ax.set_title('Harmonic Distribution')
            
            st.pyplot(fig)
    else:
        st.warning("Please enter some text to analyze.")
