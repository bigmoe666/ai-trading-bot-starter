from data.fetch_data import fetch_crypto
from models.rl_agent import train_rl_agent

print("🚀 Starting AI Trading Bot...")

# Fetch data
print("📥 Fetching BTC data...")
df = fetch_crypto("BTC/USDT", "1h", limit=2000)

print(f"✅ Loaded {len(df)} candles")

# Train RL Agent
print("🤖 Training Reinforcement Learning Agent...")
model = train_rl_agent(df)

print("✅ Training finished!")
print("\nBot is ready. You can now add live/paper trading or improve the model.")
