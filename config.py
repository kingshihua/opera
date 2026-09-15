"""
Config and API key loading. 
Copy .env.example to .env and fill in your keys before running.
"""

import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")

# Optional data-source keys — plug these in as you wire up real APIs
# for each agent (charts, news, socials, onchain).
BIRDEYE_API_KEY = os.getenv("BIRDEYE_API_KEY")       # charts / price data
NEWS_API_KEY = os.getenv("NEWS_API_KEY")             # news agent
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")  # socials agent
HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")         # onchain holder/liquidity data
