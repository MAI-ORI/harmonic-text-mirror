import streamlit as st
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models.requests import AccountInfo

# Connect to the XRP Ledger (Testnet for development, Mainnet for production)
# Testnet URL: https://s.altnet.rippletest.net:51234/
# Mainnet URL: https://s1.ripple.com:51234/
XRPL_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(XRPL_URL)

def get_account_info(wallet_address):
    """Fetches account info and balance from the XRP Ledger"""
    try:
        request = AccountInfo(
            account=wallet_address,
            ledger_index="validated"
        )
        response = client.request(request)
        return response.result
    except Exception as e:
        return {"error": str(e)}

def verify_token_holder(wallet_address, token_currency_code, issuer_address):
    """
    Placeholder function to verify if the wallet holds your custom token.
    You would expand this using AccountLines request to check trustlines.
    """
    # Implement trustline check here
    return True
