import time, glob
from src.cli import main
from click.testing import CliRunner

def benchmark(runs=3):
    files = glob.glob("input/*.pdf")
    total=0
    runner = CliRunner()
    for _ in range(runs):
        start = time.time()
        runner.invoke(
            main,
            [
                "--config", "config/default.yaml",
                "--input-dir", "input",
                "--output-dir", "output",
                "--persona-desc", "",
                "--job", "",
                "--log-level", "ERROR"
            ]
        )
        total += time.time()-start
    print(f"Avg runtime: {total/runs:.2f}s")

if __name__=="__main__":
    benchmark()
