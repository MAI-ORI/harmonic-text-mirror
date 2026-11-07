import streamlit as st
from harmonic_text_mapping import classify_word
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.requests import AccountLines

# --- CONFIGURATION ---
# Replace with your actual XRPL Issuing Address and Token Code
ISSUER_ADDRESS = "rYourIssuingAddressHere"
TOKEN_CODE = "HTM"  # Harmonic Text Mirror Token
XRPL_NODE = "https://s.altnet.rippletest.net:51234"  # Testnet

# --- HELPER FUNCTIONS ---
def check_token_balance(user_address):
    """Checks if the user holds the required HTM token on XRPL."""
    try:
        client = JsonRpcClient(XRPL_NODE)
        request = AccountLines(account=user_address)
        response = client.request(request)
        
        lines = response.result.get("lines", [])
        for line in lines:
            if line["account"] == ISSUER_ADDRESS and line["currency"] == TOKEN_CODE:
                return float(line["balance"]) > 0
    except Exception as e:
        st.error(f"XRPL Connection Error: {e}")
    return False

# --- STREAMLIT UI ---
st.title("✦ Harmonic Text Mirror")
st.write("Welcome to the recursive symbolic resonance engine.")

# --- TOKEN GATE ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.subheader("🔑 Access Verification")
    st.write("Please enter your XRPL wallet address to verify your HTM token.")
    
    user_wallet = st.text_input("XRPL Wallet Address")
    
    if st.button("Verify Token"):
        if check_token_balance(user_wallet):
            st.session_state.authenticated = True
            st.success("Access Granted! Harmonic field unlocked.")
            st.rerun()
        else:
            st.error("Token not found. Please ensure you hold HTM tokens from the correct issuer.")
else:
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
            
    if st.button("Lock Session"):
        st.session_state.authenticated = False
        st.rerun()
import streamlit as st
from xrpl_integration import get_account_info

st.title("Harmonic Text Mirror")

# --- XRP Token Integration Section ---
st.sidebar.header("✦ XRP Wallet Connection")
wallet_address = st.sidebar.text_input("Enter your XRP Wallet Address:")

if wallet_address:
    st.sidebar.write("Connecting to XRP Ledger...")
    account_data = get_account_info(wallet_address)
    
    if "error" in account_data:
        st.sidebar.error("Invalid address or account not found.")
    else:
        balance_drops = int(account_data["account_data"]["Balance"])
        balance_xrp = balance_drops / 1,000,000  # Convert drops to XRP
        st.sidebar.success(f"Connected!")
        st.sidebar.write(f"**Balance:** {balance_xrp:.2f} XRP")
        
        # Optional: Check for your custom token
        # is_holder = verify_token_holder(wallet_address, "YOUR_TOKEN_CODE", "ISSUER_ADDRESS")
        # if is_holder:
        #     st.sidebar.write("✅ Harmonic Token Verified")
