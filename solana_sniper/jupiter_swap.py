import requests
from solders.keypair import Keypair
from solders.transaction import VersionedTransaction
import base64

def buy_token(mint_address: str, sol_amount: float, slippage_bps: int = 1000, private_key: str = None):
    """Buy meme coin using Jupiter (fastest aggregator)"""
    if not private_key:
        print("⚠️  No private key provided - simulation mode")
        return None

    keypair = Keypair.from_base58_string(private_key)
    
    # Get quote
    quote_url = "https://quote-api.jup.ag/v6/quote"
    params = {
        "inputMint": "So11111111111111111111111111111111111111112",  # SOL
        "outputMint": mint_address,
        "amount": int(sol_amount * 1_000_000_000),  # lamports
        "slippageBps": slippage_bps
    }
    
    quote = requests.get(quote_url, params=params).json()
    
    # Get swap transaction
    swap_url = "https://quote-api.jup.ag/v6/swap"
    swap_data = {
        "quoteResponse": quote,
        "userPublicKey": str(keypair.pubkey()),
        "wrapAndUnwrapSol": True
    }
    
    tx_response = requests.post(swap_url, json=swap_data).json()
    tx = VersionedTransaction.from_bytes(base64.b64decode(tx_response["swapTransaction"]))
    
    # Sign & send (add priority fees in production)
    signed_tx = VersionedTransaction.populate(tx.message, [keypair])
    print(f"✅ Buying {sol_amount} SOL of {mint_address}")
    # client.send_raw_transaction(...)  # Implement sending logic
    return tx
