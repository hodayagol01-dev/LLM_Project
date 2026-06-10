from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "PRD.md",
    "PLAN.md",
    "TODO.md",
    "main.tex",
    "custom-academic-template.cls",
    "references.bib",
    "skills/orchestrator_skill.md",
    "skills/content_writer_skill.md",
    "skills/latex_builder_skill.md",
    "skills/qa_structure_skill.md",
    "skills/qa_bidi_skill.md",
    "skills/qa_references_skill.md",
    "logs/generation_log.md",
    "logs/qa_report.md",
    "assets/images",
    "assets/graphs",
    "screenshots",
]

def main():
    print("Assignment 04 QA Check")
    print("======================")

    missing = []

    for relative_path in REQUIRED_PATHS:
        path = BASE_DIR / relative_path
        if path.exists():
            print(f"[OK] {relative_path}")
        else:
            print(f"[MISSING] {relative_path}")
            missing.append(relative_path)

    print()

    if missing:
        print("QA result: FAILED")
        print("Missing items:")
        for item in missing:
            print(f"- {item}")
        raise SystemExit(1)

    print("QA result: PASSED")
    print("All required files and folders exist.")

if __name__ == "__main__":
    main()
