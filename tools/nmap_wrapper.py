import subprocess

def run_scan(target: str) -> str:
    result = subprocess.run(
        ["nmap", "-sV", "-T4", target],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    return result.stdout.strip()
