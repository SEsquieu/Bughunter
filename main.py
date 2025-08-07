from agents.bughunter_agent import BugHunterAgent

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--task", required=True, choices=["summarize", "suggest", "report"])
    parser.add_argument("--input", help="Path to input text file for report formatting")
    parser.add_argument("--output", help="Path to save the result")
    parser.add_argument("--format", choices=["txt", "md", "json"], default="txt")

    args = parser.parse_args()

    agent = BugHunterAgent()

    if args.task == "summarize":
        result = agent.scan_and_summarize(args.target)
    elif args.task == "suggest":
        result = agent.suggest_attacks(args.target)
    elif args.task == "report":
        if not args.input:
            raise ValueError("Must provide --input for report formatting")
        with open(args.input, "r") as f:
            raw_notes = f.read()
        result = agent.format_report(raw_notes)

    print("\n=== LLM Output ===\n")
    print(result)

    from pathlib import Path
    from datetime import datetime

    if not args.output:
        Path("reports").mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output = f"reports/bughunter_report_{timestamp}.{args.format}"

    with open(args.output, "w", encoding="utf-8") as f:
        if args.format == "md":
            f.write(f"# Bughunter Report — {timestamp}\n\n```\n{result}\n```")
        elif args.format == "json":
            import json
            f.write(json.dumps({"result": result}, indent=2))
        else:
            f.write(result)

    print(f"\n📁 Report saved to {args.output}")

