"""
Five lightweight agents. Each one takes raw data about a token and asks
Claude to score/reason over it. Swap the stub `fetch_*` functions for real
API calls (Birdeye, NewsAPI, X/Twitter, Helius, etc.) when you're ready.

Every agent returns a dict: {"score": 0-10, "verdict": str, "reasoning": str}
"""

from anthropic import Anthropic
from config import ANTHROPIC_API_KEY, MODEL

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def _ask_claude(system_prompt: str, data: str) -> dict:
    """Shared helper: send data to Claude, ask for a structured verdict."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        system=system_prompt + "\n\nRespond ONLY as JSON: "
        '{"score": <0-10>, "verdict": "<short verdict>", "reasoning": "<2-3 sentences>"}',
        messages=[{"role": "user", "content": data}],
    )
    text = response.content[0].text
    import json
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"score": 0, "verdict": "parse_error", "reasoning": text}


class ChartAgent:
    """Looks at price action / technicals."""
    system_prompt = (
        "You are a crypto chart analyst. Given OHLCV data, volume trends, "
        "and price action for a memecoin, assess momentum, volatility, and "
        "whether the chart looks like accumulation, distribution, or a rug setup."
    )

    def run(self, chart_data: str) -> dict:
        # TODO: replace chart_data with real OHLCV pulled from Birdeye/DEX Screener
        return _ask_claude(self.system_prompt, chart_data)


class NewsAgent:
    """Looks at news / press coverage."""
    system_prompt = (
        "You are a crypto news analyst. Given recent headlines and articles "
        "mentioning a memecoin or its narrative, assess sentiment, credibility "
        "of sources, and whether coverage is organic or paid/promotional."
    )

    def run(self, news_data: str) -> dict:
        # TODO: replace news_data with real results from NewsAPI / RSS / Google News
        return _ask_claude(self.system_prompt, news_data)


class SocialAgent:
    """Looks at social sentiment (X/Twitter, Telegram, Discord)."""
    system_prompt = (
        "You are a crypto social sentiment analyst. Given a sample of recent "
        "posts/mentions about a memecoin, assess hype level, bot activity, "
        "follower quality, and whether engagement looks organic or farmed."
    )

    def run(self, social_data: str) -> dict:
        # TODO: replace social_data with real pulls from X API, Telegram, Discord
        return _ask_claude(self.system_prompt, social_data)


class NarrativeAgent:
    """Looks at the fundamentals of the meme/narrative itself."""
    system_prompt = (
        "You are a crypto narrative analyst. Given a memecoin's theme, meme "
        "origin, timing, and comparable past coins, assess how strong and "
        "durable the narrative is versus how played-out or derivative it is."
    )

    def run(self, narrative_data: str) -> dict:
        # TODO: replace narrative_data with a written summary of the coin's story
        return _ask_claude(self.system_prompt, narrative_data)


class OnchainAgent:
    """Looks at holder distribution and liquidity health."""
    system_prompt = (
        "You are an onchain analyst. Given holder count, top-holder "
        "concentration, LP lock status, and liquidity depth for a memecoin, "
        "assess rug risk and whether liquidity can support real trading volume."
    )

    def run(self, onchain_data: str) -> dict:
        # TODO: replace onchain_data with real pulls from Helius / Solscan / Etherscan
        return _ask_claude(self.system_prompt, onchain_data)
