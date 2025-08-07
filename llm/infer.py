from llm.prompt_loader import load_prompt
from config.settings import MODEL_NAME
import subprocess

def llm_infer(model_name: str, prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", model_name, prompt],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def run_llm_task(intent: str, input_data: str) -> str:
    prompt = load_prompt(intent).replace("{{input}}", input_data)
    return llm_infer(MODEL_NAME, prompt)
