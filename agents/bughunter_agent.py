from llm.infer import run_llm_task
from tools import nmap_wrapper

class BugHunterAgent:
    def scan_and_summarize(self, target):
        result = nmap_wrapper.run_scan(target)
        return run_llm_task("summarize_scan", result)

    def suggest_attacks(self, context):
        return run_llm_task("propose_attack", context)

    def format_report(self, raw_notes):
        return run_llm_task("format_report", raw_notes)
