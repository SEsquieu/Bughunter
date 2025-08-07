# Bughunter AI

**Bughunter AI** is a scoped LLM-powered assistant designed to supercharge your recon and vulnerability discovery workflow. It wraps traditional security tools like `nmap` and enhances them with tightly focused LLM reasoning to help bug bounty hunters, red teamers, and tinkerers analyze targets, generate attack vectors, and format professional reports.

---

## Features

- **Scan & Summarize** — Runs `nmap` scans and produces clean, LLM-generated summaries of reachable services, versions, and potential misconfigs
- **Attack Suggestions** — Given basic context, the LLM proposes attack vectors to explore
- **Bug Bounty Report Formatter** — Turns raw notes into clean, markdown-formatted reports for platforms like HackerOne
- **Scoped LLM Prompts** — Tasks are tightly scoped, minimizing hallucinations and keeping results actionable
- **Modular Backend** — Easy to add more tool wrappers (e.g. `ffuf`, `httpx`, `binwalk`, etc.)

---

## Project Structure

```
bughunter/
├── main.py                  # CLI entrypoint
├── config/                  # Model + tool settings
├── agents/                  # BugHunterAgent logic
├── prompts/                 # Prompt templates for each task
├── tools/                   # CLI tool wrappers (e.g., nmap)
├── llm/                     # LLM call and prompt loader logic
├── examples/                # Optional example data
└── requirements.txt
```

---

## Requirements

- Python 3.8+
- [`ollama`](https://ollama.com/) (for running local LLMs like `phi3`, `mistral`, etc.)
- `nmap` installed and in your system path

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/sesquieu/bughunter.git

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run your first scan
python main.py --target example.com --task summarize
```

To format a bug bounty report from notes:

```bash
python main.py --task report --input ./examples/raw_finding.txt --target ignored
```

---

## Prompt Logic

Each LLM task is scoped to a single intent:

- `summarize_scan`: Converts tool output into readable summaries
- `propose_attack`: Suggests next-step attacks based on context
- `format_report`: Converts raw notes into markdown reports

All prompt templates live in `/prompts` and can be edited to suit your tone or workflow.

---

## Add a New Tool

To add support for new tools like `ffuf` or `httpx`, drop a wrapper in `tools/`, then update `BugHunterAgent` with a new method. Each wrapper should return a string to be summarized by the LLM.

---

## Future Ideas

- Multi-step attack flows
- Firmware dissection via `binwalk` + LLM analysis
- Web UI dashboard
- Agentic multi-tool chaining

---

## License

MIT — feel free to fork, modify, and make it your own.

---

## Credits

Created by [@SEsquieu](https://github.com/sesquieu)  
Inspired by the intersection of offensive security, LLMs, and automation.
