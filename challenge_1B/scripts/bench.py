import time
import glob
from src.cli import main

def benchmark(runs=3):
    total = 0.0
    for _ in range(runs):
        start = time.time()
        main.callback(
            config="config/default.yaml",
            input_dir="input",
            output_dir="output",
            persona_desc="",
            job_to_be_done="",
            log_level="ERROR"
        )
        total += time.time() - start
    print(f"Avg runtime: {total/runs:.2f}s")

if __name__ == "__main__":
    benchmark()
