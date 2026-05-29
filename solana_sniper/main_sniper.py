import asyncio
import json
from solana.rpc.async_api import AsyncClient
from config import *
from solana_sniper.rug_checker import check_rug
from solana_sniper.jupiter_swap import buy_token  # rename if needed
from telegram_alerts import send_telegram

async def on_new_token(data):
    try:
        mint = data["mint"]  # adjust based on actual payload
        name = data.get("name", "Unknown")
        
        passed, msg = check_rug(mint)
        if not passed:
            print(f"❌ Rug risk: {msg}")
            return
        
        print(f"🎯 New coin: {name} | {mint}")
        await send_telegram(f"🚨 New meme: {name}\nMint: {mint}\n{msg}")
        
        tx = buy_token(mint, PRIVATE_KEY)
        # Add sell monitor (take profit / stop loss) here
        await send_telegram(f"✅ Bought {name}")
        
    except Exception as e:
        print("Error:", e)

async def main():
    client = AsyncClient(RPC_URL)
    print("🔥 Fast Solana Meme Sniper Started (with rug checks + TP/SL)")
    # Subscribe to Pump.fun program logs...
    # Full subscription code would go here (use Pump.fun program ID)

if __name__ == "__main__":
    asyncio.run(main())
