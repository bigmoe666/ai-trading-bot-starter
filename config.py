import os
from dotenv import load_dotenv

load_dotenv()

# === RPC & Wallet ===
RPC_URL = os.getenv("RPC_URL", "https://api.mainnet-beta.solana.com")  # Replace with Helius/QuickNode
PRIVATE_KEY = os.getenv("PRIVATE_KEY")  # Base58 encoded

# === Trading Settings ===
BUY_AMOUNT_SOL = 0.05          # How much SOL to buy per sniper
SLIPPAGE_BPS = 1500            # 15% slippage
TAKE_PROFIT_PCT = 3.0          # Sell at +300%
STOP_LOSS_PCT = 0.5            # Sell at -50%
MAX_POSITIONS = 3

# === Telegram ===
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# === Filters ===
MIN_LIQUIDITY_SOL = 5.0
MAX_DEV_HOLD_PCT = 10.0
