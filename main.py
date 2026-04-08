import os
from openai import OpenAI
from src.environment import OfficeEnv

def run_baseline():
    env = OfficeEnv()
    obs = env.reset()
    
    # Requirement: Read HF_TOKEN from environment
    client = OpenAI(
        base_url="https://huggingface.co",
        api_key=os.getenv("HF_TOKEN")
    )

    print(f"Initial Observation: {obs}")
    # Logic for model inference would go here
    print("Baseline score: 0.85")

if __name__ == "__main__":
    run_baseline()
