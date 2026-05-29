from stable_baselines3 import PPO
from env.trading_env import TradingEnv

def train_rl_agent(df):
    env = TradingEnv(df)
    model = PPO("MlpPolicy", env, verbose=1, learning_rate=0.001)
    model.learn(total_timesteps=50000)   # You can increase this later
    model.save("ppo_trading_bot")
    return model
