import ccxt
import pandas as pd

def fetch_crypto(symbol="BTC/USDT", timeframe="1h", limit=2000):
    """Fetch cryptocurrency data from Binance"""
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df.set_index('timestamp')
