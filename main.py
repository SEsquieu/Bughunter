from agents.bughunter_agent import BugHunterAgent

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--task", required=True, choices=["summarize", "suggest", "report"])
    parser.add_argument("--input", help="Path to input text file for report formatting")
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
