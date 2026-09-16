"""
Orchestrator: runs all 5 agents on a memecoin and prints a combined verdict.

Usage:
    python main.py
"""

from agents import ChartAgent, NewsAgent, SocialAgent, NarrativeAgent, OnchainAgent

# --- Replace these stubs with real fetched data before running for real ---
SAMPLE_INPUT = {
    "chart": "24h volume up 340%, price +85%, 3 green candles in a row, "
             "low sell pressure on dips.",
    "news": "One small crypto blog post mentioning the coin, no major "
            "outlet coverage yet.",
    "social": "Twitter mentions up 12x in 24h, mix of real accounts and "
              "clearly new/bot-like accounts, Telegram group growing fast.",
    "narrative": "Riffs on a trending internet meme from this week, similar "
                 "coins in this micro-narrative have pumped and dumped within days.",
    "onchain": "Top 10 wallets hold 61% of supply, LP locked for 30 days, "
               "liquidity is $45k on a $2M market cap.",
}

AGENTS = {
    "Chart": ChartAgent(),
    "News": NewsAgent(),
    "Social": SocialAgent(),
    "Narrative": NarrativeAgent(),
    "Onchain": OnchainAgent(),
}


def run_all(inputs: dict) -> dict:
    results = {}
    for name, agent in AGENTS.items():
        key = name.lower()
        results[name] = agent.run(inputs[key])
    return results


def summarize(results: dict) -> None:
    total = sum(r.get("score", 0) for r in results.values())
    avg = total / len(results)

    print("\n=== Memecoin Agent Report ===\n")
    for name, r in results.items():
        print(f"[{name}] score={r.get('score')} — {r.get('verdict')}")
        print(f"  {r.get('reasoning')}\n")

    print(f"Average score: {avg:.1f}/10")
    if avg >= 7:
        print("Overall lean: BUY signal is strong")
    elif avg >= 4:
        print("Overall lean: MIXED — proceed with caution / small size")
    else:
        print("Overall lean: AVOID")


if __name__ == "__main__":
    results = run_all(SAMPLE_INPUT)
    summarize(results)
