# Supported tokens on the XRP Ledger
SUPPORTED_TOKENS = {
    "XRP": {
        "currency": "XRP",
        "issuer": None,  # Native asset
        "min_balance": 10  # Minimum XRP to activate wallet
    },
    "SHAIDS": {
        "currency": "SHAIDS",
        "issuer": "YOUR_XRP_WALLET_ADDRESS",  # Replace with your actual issuing address
        "min_balance": 1  # Minimum SHAIDS required for access
    },
    "PI": {
        "currency": "PI",
        "issuer": "YOUR_XRP_WALLET_ADDRESS",  # Replace with your actual issuing address
        "min_balance": 1  # Minimum PI required for access
    }
}

def verify_user_tokens(wallet_address):
    """
    Verifies if the user's wallet contains XRP, SHAIDS, or PI
    with balances meeting the minimum threshold.
    """
    try:
        # Query XRPL for account lines (tokens)
        # (Using xrpl-py library or direct JSON-RPC request)
        account_lines = get_account_lines(wallet_address)
        
        # Query XRPL for native XRP balance
        xrp_balance = get_xrp_balance(wallet_address)
        
        user_balances = {"XRP": xrp_balance}
        
        for line in account_lines:
            currency = line.get("currency")
            balance = float(line.get("balance", 0))
            issuer = line.get("account")
            
            if currency in SUPPORTED_TOKENS:
                expected_issuer = SUPPORTED_TOKENS[currency]["issuer"]
                if expected_issuer is None or issuer == expected_issuer:
                    user_balances[currency] = balance
        
        # Check if any supported token meets the minimum requirement
        for token, config in SUPPORTED_TOKENS.items():
            if user_balances.get(token, 0) >= config["min_balance"]:
                return True, f"Access granted via {token} token."
                
        return False, "Insufficient token balances. Requires XRP, SHAIDS, or PI."
        
    except Exception as e:
        return False, f"Wallet verification failed: {str(e)}"
