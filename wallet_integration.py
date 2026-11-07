import os
from web3 import Web3
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to Web3 provider (e.g., Sepolia testnet)
INFURA_URL = os.getenv("INFURA_URL", "https://sepolia.infura.io/v3/YOUR_PROJECT_ID")
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Smart Contract Details
CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS", "0xYourContractAddressHere")
# Minimal ABI for ERC-20 token (balanceOf and transfer)
CONTRACT_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}],
        "name": "transfer",
        "outputs": [{"name": "success", "type": "bool"}],
        "type": "function"
    }
]

# Initialize Contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

def check_connection():
    """Check if connected to the blockchain network."""
    return w3.is_connected()

def get_token_balance(address):
    """Get the token balance of a specific wallet address."""
    if not w3.is_address(address):
        return "Invalid address"
    balance = contract.functions.balanceOf(address).call()
    # Assuming 18 decimals (standard for ERC-20)
    return w3.from_wei(balance, 'ether')

def send_tokens(private_key, to_address, amount):
    """Send tokens from the wallet associated with the private key."""
    if not w3.is_address(to_address):
        return "Invalid recipient address"
    
    # Get sender address from private key
    account = w3.eth.account.from_key(private_key)
    sender_address = account.address
    
    # Convert amount to Wei
    amount_in_wei = w3.to_wei(amount, 'ether')
    
    # Build transaction
    nonce = w3.eth.get_transaction_count(sender_address)
    tx = contract.functions.transfer(to_address, amount_in_wei).build_transaction({
        'chainId': 11155111,  # Sepolia testnet ID
        'gas': 70000,
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
    })
    
    # Sign and send transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    return w3.to_hex(tx_hash)
