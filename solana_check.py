import asyncio
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey

# Define the Solana RPC endpoint (Devnet for testing)
SOLANA_RPC_URL = "https://api.devnet.solana.com"

# Define a test wallet address (replace with your own if desired)
# This is a known public Solana address for testing purposes
TEST_WALLET_ADDRESS = "6ZMF3v8v8v8v8v8v8v8v8v8v8v8v8v8v8v8v8v8v8v8v"

async def check_solana_connection():
    print("Connecting to Solana network...")
    
    # Initialize the async client
    async with AsyncClient(SOLANA_RPC_URL) as client:
        # 1. Check connection status
        try:
            is_connected = await client.is_connected()
            if is_connected:
                print(f"✅ Successfully connected to Solana RPC: {SOLANA_RPC_URL}")
            else:
                print("❌ Connection failed: RPC endpoint did not respond.")
                return
        except Exception as e:
            print(f"❌ Connection error: {e}")
            return

        # 2. Check wallet balance
        try:
            # Convert string address to Pubkey object
            pubkey = Pubkey.from_string(TEST_WALLET_ADDRESS)
            print(f"Checking balance for wallet: {TEST_WALLET_ADDRESS}")
            
            # Fetch balance (returned in lamports: 1 SOL = 1,000,000,000 lamports)
            response = await client.get_balance(pubkey)
            balance_lamports = response.value
            balance_sol = balance_lamports / 1_000_000_000
            
            print(f"💰 Wallet Balance: {balance_sol} SOL ({balance_lamports} lamports)")
        except Exception as e:
            print(f"❌ Failed to retrieve balance: {e}")

if __name__ == "__main__":
    # Run the async function
    asyncio.run(check_solana_connection())
