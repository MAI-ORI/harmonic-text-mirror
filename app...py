import requests

# Configuration: Replace with your actual wallet and token details
USER_WALLET_ADDRESS = "your_xrp_wallet_address"
PI_TOKEN_CODE = "Pi"  # Or hex equivalent if custom
SHAIDS_TOKEN_CODE = "SHAIDS"  # Or hex equivalent if custom
ISSUER_ADDRESS = "your_issuer_wallet_address"  # The wallet that issued Pi and SHAIDS

def verify_user_tokens(wallet_address):
    """
    Queries the XRP Ledger to verify if the user holds Pi or SHAIDS tokens.
    Does NOT require HTM token.
    """
    # XRPL JSON-RPC endpoint (use mainnet or testnet depending on your setup)
    url = "https://s1.ripple.com:51234"  # Mainnet
    # url = "https://s.altnet.rippletest.net:51234" # Testnet

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
        response = requests.post(url, json=payload)
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
        print(f"Error verifying tokens: {e}")
        return {"verified": False, "pi_balance": False, "shaids_balance": False}
