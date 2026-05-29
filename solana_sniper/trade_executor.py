import requests
from solders.keypair import Keypair
from solders.transaction import VersionedTransaction
import base64
from config import BUY_AMOUNT_SOL, SLIPPAGE_BPS, RPC_URL

def buy_token(mint: str, private_key: str):
    if not private_key:
        print("🔒 Simulation mode - no real buy")
        return None
    
    keypair = Keypair.from_base58_string(private_key)
    
    # Jupiter quote + swap with priority fee
    quote = requests.get("https://quote-api.jup.ag/v6/quote", params={
        "inputMint": "So11111111111111111111111111111111111111112",
        "outputMint": mint,
        "amount": int(BUY_AMOUNT_SOL * 1_000_000_000),
        "slippageBps": SLIPPAGE_BPS
    }).json()
    
    swap_tx = requests.post("https://quote-api.jup.ag/v6/swap", json={
        "quoteResponse": quote,
        "userPublicKey": str(keypair.pubkey()),
        "wrapAndUnwrapSol": True,
        "computeUnitPriceMicroLamports": 500_000  # High priority fee for speed
    }).json()
    
    tx = VersionedTransaction.from_bytes(base64.b64decode(swap_tx["swapTransaction"]))
    # Sign and send logic (add full client.send in production)
    print(f"🚀 Buying {BUY_AMOUNT_SOL} SOL of {mint} with priority fee")
    return tx
