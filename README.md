# Opera - A Memetic Decoder & Trader Assistant 

A 5-part multi-agent system that helps you sanity-check a memecoin before you ape in.
Five specialized agents each look at one slice of the picture, then get combined
into a single buy/avoid lean.

> ⚠️ **Not financial advice.** This is a decision-support toy, not a trading bot.
> Memecoins are extremely high-risk and can go to zero fast. Do your own research.

## The 5 Agents

| Agent | File | What it looks at |
|---|---|---|
| 📊 **Chart** | `agents.py` → `ChartAgent` | Price action, volume, momentum, candle patterns |
| 📰 **News** | `agents.py` → `NewsAgent` | Press coverage, sentiment, source credibility |
| 🐦 **Social** | `agents.py` → `SocialAgent` | X/Twitter & Telegram hype, bot activity, engagement quality |
| 🧠 **Narrative** | `agents.py` → `NarrativeAgent` | Strength & durability of the meme/story itself |
| ⛓️ **Onchain** | `agents.py` → `OnchainAgent` | Holder concentration, LP lock status, liquidity depth |

Each agent returns a simple structured verdict:
 
```json
{"score": 7, "verdict": "cautiously bullish", "reasoning": "..."}
```

`main.py` runs all five and averages their scores into an overall lean:
**BUY / MIXED / AVOID**.

## How it works

Each agent is just a focused system prompt sent to Claude along with whatever
data you feed it. There's no real data-fetching wired up yet — the goal of
this repo is the **agent structure**, not a finished trading bot. Swap the
`TODO` stubs in `agents.py` and `main.py` for real API calls when you're ready
(see below).

## Setup

```bash
git clone <this-repo>
cd memecoin-agents
pip install -r requirements.txt
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
python main.py
```

## Files

- **`README.md`** — you are here
- **`agents.py`** — the 5 agent classes (system prompts + Claude call)
- **`main.py`** — orchestrator that runs all agents and prints a combined report
- **`config.py`** — loads API keys from environment variables
- **`requirements.txt`** — dependencies

## Wiring up real data

Right now `main.py` uses a hardcoded `SAMPLE_INPUT` dict so you can see the
pipeline run end-to-end. To make it real, replace each field with live data:

- **Chart** → [Birdeye](https://birdeye.so) / DEX Screener OHLCV + volume
- **News** → NewsAPI, Google News RSS, or a crypto news aggregator
- **Social** → X API v2 search, Telegram/Discord scraping
- **Narrative** → your own writeup, or scrape a coin's launch story / comparable coins
- **Onchain** → [Helius](https://helius.dev) (Solana) or Etherscan/BscScan (EVM) for holder + LP data

Each agent's `.run()` method just takes a string of context — feed it whatever
format your data source gives you.

## Extending

- Add a 6th agent (e.g. a **team/dev-wallet tracker**) by copying the pattern in `agents.py`
- Change scoring weights in `main.py::summarize` if you want some agents to matter more
- Swap `MODEL` in `.env` to try different Claude models for cost/speed tradeoffs

## License

MIT — do whatever you want with it, just don't blame this repo when a coin rugs.
