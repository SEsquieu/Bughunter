from config.settings import PROMPT_DIR
from pathlib import Path

def load_prompt(intent: str) -> str:
    path = Path(PROMPT_DIR) / f"{intent}.txt"
    return path.read_text()
