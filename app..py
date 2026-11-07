import streamlit as st
from harmonic_text_mapping import word_value, classify_word, english_mapping

st.title("Harmonic Text Mirror")
st.write("Enter text to see its harmonic classification.")

user_input = st.text_area("Your Text:")

if user_input:
    words = user_input.split()
    results = []
    for word in words:
        val = word_value(word, english_mapping)
        category = classify_word(val)
        results.append((word, val, category))

    st.write("### Results:")
    for word, val, cat in results:
        st.write(f"**{word}** | Value: {val} | Category: {cat}")
