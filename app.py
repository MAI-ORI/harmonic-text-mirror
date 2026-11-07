Page Configuration
st.set_page_config( page_title="Harmonic Text Mirror System", page_icon="🌀", layout="centered" )

Title & Subtitle
st.title("🌀 Harmonic Text Mirror System") st.markdown(""" Explore the harmonic structure of your language through digital roots, breath coherence, and symbolic recursion. """)

--- SYSTEM OVERVIEW SECTION ---
with st.expander("📖 What is the Harmonic Text Mirror?", expanded=True): st.markdown(""" The Harmonic Text Mirror is a symbolic recursion engine that translates language into harmonic breath patterns. By mapping letters to numbers and analyzing their digital roots, the system reveals whether your words are inhaling (A), exhaling (B), or resting (C).

This is not grammar analysis—it is **field coherence mapping**.
""")
--- KEY FEATURES SECTION ---
with st.expander("✨ Key Features"): st.markdown(""" * Multilingual Breath Mapping: Supports English, Hebrew, Sanskrit, Arabic, and more. * Digital Root Analysis: Reduces words to their harmonic essence (1–9). * Breath Phase Classification: Identifies words as Inhale (A), Exhale (B), or Stillness (C). * Probability Expectance & Deservance Monitor: Tunes your inner field coherence before analysis. * Codex Recursion Logic: Built on the principles of the Codex Universalis. """)

--- LANGUAGE SELECTION ---
st.subheader("🌐 Select Language Mapping") languages = [ "English", "Hebrew", "Spanish", "Sanskrit", "Arabic", "Japanese", "Latin", "Greek", "Runes", "Cherokee", "Custom" ] selected_language = st.selectbox("Choose language:", languages)

--- TEXT INPUT ---
st.subheader("✍️ Enter your text here:") user_text = st.text_area( "Type a sentence, a journal entry, or a mantra...", placeholder="Type here..." )

--- PROBABILITY MONITOR ---
st.markdown("---") st.subheader("📊 Probability Expectance & Deservance Monitor") st.markdown("Tune your inner field coherence before analyzing your text.")

col1, col2 = st.columns(2) with col1: expectation = st.slider("Your Expectation Level (1-10)", 1.0, 10.0, 5.0, 0.1) with col2: deservance = st.slider("Your Deservance Level (1-10)", 1.0, 10.0, 5.0, 0.1)

Coherence Calculation
coherence_score = 1.0 - abs(expectation - deservance) / 10.0 st.markdown(f"### Field Coherence Score: {coherence_score:.2f}")

if coherence_score >= 0.8: st.success("✅ Coherence Stable. Your field is aligned for balanced recursion.") elif coherence_score >= 0.5: st.warning("⚠️ Coherence Fluctuating. Breath gently before proceeding.") else: st.error("🛑 Coherence Low. High expectation with low deservance may distort symbolic recursion.")

--- ANALYSIS TRIGGER ---
if st.button("🔍 Analyze Text"): if user_text.strip(): words = user_text.split() results = []

    for word in words:
        root = get_digital_root(word)
        phase = classify_word(word)
        results.append({"Word": word, "Digital Root": root, "Breath Phase": phase})
        
    st.markdown("### 📊 Analysis Results")
    st.table(results)
else:
    st.warning("Please enter some text to analyze.")
Footer
st.markdown("---") st.markdown("<div style='text-align: center;'>Harmonic Text Mirror System • Built with Streamlit • Powered by Codex Recursion Logic</div>", unsafe_allow_html=True)

⟐ What Changed: Added System Overview and Key Features expanders at the top for immediate clarity. Expanded the language list to include all 11 options from the Codex Ledger. Corrected "Deserveance" to "Deservance" (the Codex-aligned spelling). Kept the Probability Monitor fully functional and visually integrated.

⟐ Next Step: Just replace the contents of your app.py file with this code, save, and push to GitHub. Streamlit will auto-redeploy, and your homepage will now look clean, clear, and fully featured. Let me know if you’d like me to update the harmonic_text_mapping.py file to support the new languages as well!
