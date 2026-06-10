import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
MAIN_TEX = BASE_DIR / "main.tex"

def run_lualatex():
    if not MAIN_TEX.exists():
        print("main.tex was not found.")
        raise SystemExit(1)

    for run_number in range(1, 3):
        print(f"Running LuaLaTeX pass {run_number}...")
        result = subprocess.run(
            ["lualatex", "-interaction=nonstopmode", "main.tex"],
            cwd=BASE_DIR,
            text=True,
            capture_output=True,
        )

        if result.returncode != 0:
            print("LuaLaTeX failed.")
            print(result.stdout)
            print(result.stderr)
            raise SystemExit(result.returncode)

    print("PDF compilation completed successfully.")

if __name__ == "__main__":
    run_lualatex()
