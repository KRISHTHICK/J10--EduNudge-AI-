import subprocess

def ask_ai_agent(prompt):
    formatted = f"Explain like I’m a student: {prompt}"
    result = subprocess.run(["ollama", "run", "phi3", formatted], capture_output=True, text=True)
    return result.stdout.strip()
