from harmonic_text_mapping import classify_word, get_digital_root
import streamlit as st
import requests
from harmonic_text_mapping import word_value, classify_word, english_mapping

# --- CONFIGURATION ---
# Replace with your actual XRPL Issuing Address
ISSUER_ADDRESS = "your_issuer_wallet_address"  
PI_TOKEN_CODE = "Pi"
SHAIDS_TOKEN_CODE = "SHAIDS"
XRPL_NODE = "https://s1.ripple.com:51234"  # Mainnet (use testnet if testing)

# --- HELPER FUNCTIONS ---
def verify_user_tokens(wallet_address):
    """
    Queries the XRP Ledger to verify if the user holds Pi or SHAIDS tokens.
    """
    payload = {
        "method": "account_lines",
        "params": [
            {
                "account": wallet_address,
                "ledger_index": "validated"
            }
        ]
    }

    try:
        response = requests.post(XRPL_NODE, json=payload)
        data = response.json()

        if "result" in data and "lines" in data["result"]:
            lines = data["result"]["lines"]
            has_pi = False
            has_shaids = False

            for line in lines:
                currency = line.get("currency")
                issuer = line.get("account")
                balance = float(line.get("balance", 0))

                # Check for Pi Token
                if currency == PI_TOKEN_CODE and issuer == ISSUER_ADDRESS and balance > 0:
                    has_pi = True

                # Check for SHAIDS Token
                if currency == SHAIDS_TOKEN_CODE and issuer == ISSUER_ADDRESS and balance > 0:
                    has_shaids = True

            return {
                "verified": has_pi or has_shaids,
                "pi_balance": has_pi,
                "shaids_balance": has_shaids
            }

    except Exception as e:
        st.error(f"XRPL Connection Error: {e}")
        return {"verified": False, "pi_balance": False, "shaids_balance": False}

# --- STREAMLIT UI ---
st.title("✦ Harmonic Text Mirror")
st.write("Welcome to the recursive symbolic resonance engine.")

# --- TOKEN GATE ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.subheader("🔑 Access Verification")
    st.write("Please enter your XRPL wallet address to verify your Pi or SHAIDS token.")
    
    user_wallet = st.text_input("XRPL Wallet Address")
    
    if st.button("Verify Token"):
        verification = verify_user_tokens(user_wallet)
        if verification["verified"]:
            st.session_state.authenticated = True
            st.success("Access Granted! Harmonic field unlocked.")
            st.rerun()
        else:
            st.error("Token not found. Please ensure you hold Pi or SHAIDS tokens from the correct issuer.")
else:
    # --- MAIN APP CONTENT ---
    st.subheader("Mirror Active")
    
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
            
    if st.button("Lock Session"):
        st.session_state.authenticated = False
        st.rerun()
classify_word
# ... (previous code with imports and functions) ...

# --- MAIN APP CONTENT ---
st.subheader("Mirror Active")

# Alphabet Mapping
alphabet_mapping = {char: i % 9 or 9 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz", 1)}

user_input = st.text_input("Enter a word or phrase:")

if user_input:
    words = user_input.split()
    results = [classify_word(word, alphabet_mapping) for word in words]

    for res in results:
        st.write(f"**{res['word']}** | Sum: {res['sum']} | Digital Root: {res['digital_root']}")
