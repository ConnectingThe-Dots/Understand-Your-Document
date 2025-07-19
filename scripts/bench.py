import time
import glob
from src.cli import main


def benchmark(input_pattern="input/*.pdf", runs=3):
    files = glob.glob(input_pattern)
    total = 0.0
    for _ in range(runs):
        start = time.time()
        for pdf in files:
            main.callback(
                config_path="config/default.yaml",
                input_dir=os.path.dirname(pdf),
                output_dir="output",
                log_level="ERROR",
            )
        total += time.time() - start
    avg = total / runs
    print(f"Average runtime over {runs} runs: {avg:.2f}s")

if __name__ == "__main__":
    benchmark()