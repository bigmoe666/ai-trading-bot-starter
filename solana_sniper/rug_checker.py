import requests

def check_rug(mint: str):
    try:
        # Using rugcheck.xyz API (free tier)
        r = requests.get(f"https://api.rugcheck.xyz/v1/tokens/{mint}/report", timeout=5)
        data = r.json()
        
        risk_score = data.get("riskScore", 100)
        dev_hold = data.get("devHoldings", 0)
        liquidity = data.get("liquidity", 0)
        
        if risk_score > 50 or dev_hold > 10 or liquidity < 5:
            return False, f"High risk: Score={risk_score}, Dev={dev_hold}%"
        
        return True, "✅ Passed rug check"
    except:
        return True, "⚠️ Could not check rug (using defaults)"
