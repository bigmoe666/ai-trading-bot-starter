import gymnasium as gym
import numpy as np

class TradingEnv(gym.Env):
    def __init__(self, df):
        super().__init__()
        self.df = df.reset_index()
        self.current_step = 0
        self.balance = 10000.0
        self.position = 0.0
        
        self.action_space = gym.spaces.Discrete(3)  # 0=Hold, 1=Buy, 2=Sell
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(8,), dtype=np.float32)
    
    def reset(self, seed=None):
        self.current_step = 0
        self.balance = 10000.0
        self.position = 0.0
        return self._get_obs(), {}
    
    def step(self, action):
        price = self.df.loc[self.current_step, 'close']
        
        if action == 1 and self.position == 0:      # Buy
            self.position = self.balance / price
            self.balance = 0
        elif action == 2 and self.position > 0:     # Sell
            self.balance = self.position * price
            self.position = 0
        
        self.current_step += 1
        done = self.current_step >= len(self.df) - 1
        reward = self.balance + (self.position * price) - 10000
        
        return self._get_obs(), reward, done, False, {}
    
    def _get_obs(self):
        row = self.df.iloc[self.current_step]
        return np.array([row['close'], self.balance, self.position, 0,0,0,0,0], dtype=np.float32)
