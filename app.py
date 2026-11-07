import streamlit as st
import matplotlib.pyplot as plt
from harmonic_text_mapping import process_sentence

# Page configuration
st.set_page_config(
    page_title="Harmonic Text Mirror",
    page_icon="🌀",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #0f0f1a;
        color: #e0e0ff;
    }
    h1, h2, h3 {
        color: #a080ff;
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        background-color: #4b0082;
        color: white;
        border-radius: 8px;
        border: 1px solid #a080ff;
    }
    .stButton>button:hover {
        background-color: #6a0dad;
        border-color: #d8b4fe;
    }
    .card {
        background-color: #1a1a2e;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #333355;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_index=True)

# Title and Subtitle
st.title("🌀 Harmonic Text Mirror")
st.subheader("A Codex-aligned language resonance interface")

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Mirror Tool", "Harmonic Charter", "Treasury & Tokenomics", "Applications"])

# ================= TAB 1: MIRROR TOOL =================
with tab1:
    st.markdown("### Enter text to view its harmonic signature:")
    user_input = st.text_area("Supports all languages (English, Hebrew, Spanish, Arabic, Japanese, etc.)", "")

    if st.button("Reflect"):
        if user_input.strip():
            results, details = process_sentence(user_input)
            
            # Display Results
            st.markdown("#### 📊 Harmonic Signature:")
            col1, col2, col3 = st.columns(3)
            col1.metric("Category A (Symbolic)", results['A'])
            col2.metric("Category B (Emotional)", results['B'])
            col3.metric("Category C (Physical)", results['C'])
            
            # Visualization
            fig, ax = plt.subplots(figsize=(6, 4))
            fig.patch.set_facecolor('#1a1a2e')
            ax.set_facecolor('#1a1a2e')
            
            categories = ['A (Symbolic)', 'B (Emotional)', 'C (Physical)']
            counts = [results['A'], results['B'], results['C']]
            colors = ['#a080ff', '#ff80a0', '#80ffc0']
            
            bars = ax.bar(categories, counts, color=colors, edgecolor='#ffffff', linewidth=0.5)
            ax.tick_params(colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.set_title("Resonance Distribution", color='white', fontsize=12)
            
            # Add value labels on top of bars
            for bar in bars:
                yval = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, str(yval), ha='center', va='bottom', color='white')
            
            st.pyplot(fig)
            
            # Word Breakdown
            st.markdown("#### 🔍 Word-by-Word Breakdown:")
            breakdown_text = ""
            for word, cat in details:
                color = "#a080ff" if cat == 'A' else "#ff80a0" if cat == 'B' else "#80ffc0"
                breakdown_text += f"<span style='color:{color}; font-weight:bold;'>{word}</span> ({cat}) &nbsp;&nbsp;"
            st.markdown(breakdown_text, unsafe_allow_index=True)
        else:
            st.warning("Please enter some text first.")

# ================= TAB 2: HARMONIC CHARTER =================
with tab2:
    st.markdown("""
    <div class='card'>
    <h2>📜 The Harmonic Charter</h2>
    <p><strong>1. Sovereignty of Expression:</strong> Every user owns their harmonic signature. No central authority may alter or suppress it.</p>
    <p><strong>2. Privacy of Resonance:</strong> Text inputs and harmonic profiles are processed locally or ephemerally. No data is stored without explicit consent.</p>
    <p><strong>3. Coherence Over Control:</strong> The system rewards balanced, coherent communication rather than engagement-driven noise.</p>
    <p><strong>4. Open Access:</strong> The Harmonic Text Mirror is a public good. Its core algorithms and logic remain open-source and accessible to all.</p>
    <p><strong>5. Interoperability:</strong> The system is designed to integrate seamlessly with decentralized identity, finance, and governance networks.</p>
    </div>
    """, unsafe_allow_index=True)

# ================= TAB 3: TREASURY & TOKENOMICS =================
with tab3:
    st.markdown("""
    <div class='card'>
    <h2>💎 Harmonic Treasury & Tokenomics</h2>
    <p>The <strong>Harmonic Treasury</strong> is a decentralized reserve that governs the distribution and utility of the ecosystem's native token.</p>
    <h3>Token Functions:</h3>
    <ul>
        <li><strong>Reward:</strong> Earned by contributing coherent, balanced text to the ecosystem.</li>
        <li><strong>Access:</strong> Used to unlock advanced harmonic analysis, premium content, or voting rights.</li>
        <li><strong>Governance:</strong> Tokens represent voting power in the decentralized decision-making process.</li>
    </ul>
    <h3>Treasury Rules:</h3>
    <ul>
        <li>A fixed percentage of all transaction fees is routed to the Treasury.</li>
        <li>Treasury funds are allocated via community-voted proposals.</li>
        <li>No single entity holds administrative control over Treasury assets.</li>
    </ul>
    </div>
    """, unsafe_allow_index=True)

# ================= TAB 4: APPLICATIONS =================
with tab4:
    st.markdown("### 🚀 Functional Applications of the System")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='card'>
        <h4>🎓 Education</h4>
        <p>Gamified learning where students earn tokens for writing essays that demonstrate high harmonic coherence and balanced expression.</p>
        </div>
        <div class='card'>
        <h4>💬 Social Media</h4>
        <p>A platform that analyzes the emotional tone and harmonic balance of posts, rewarding constructive communication and discouraging toxicity.</p>
        </div>
        <div class='card'>
        <h4>🛍️ Content Marketplace</h4>
        <p>A decentralized store where creators price their work in tokens, and users pay to access articles, videos, or courses.</p>
        </div>
        """, unsafe_allow_index=True)
        
    with col2:
        st.markdown("""
        <div class='card'>
        <h4>✍️ Collaborative Writing</h4>
        <p>Real-time feedback for writers, suggesting adjustments to improve the symbolic, emotional, or physical balance of their text.</p>
        </div>
        <div class='card'>
        <h4>🧘 Personal Development</h4>
        <p>A journaling app that tracks the harmonic signature of daily entries, offering insights into emotional patterns and growth over time.</p>
        </div>
        <div class='card'>
        <h4>🏛️ Decentralized Governance</h4>
        <p>A voting system where voting weight is influenced by the historical coherence and harmonic contributions of the participant.</p>
        </div>
        """, unsafe_allow_index=True)
