import re
from pathlib import Path


def extract():
    chapters_sections = []

    for f in (Path(__file__).parent.parent / "CHAPTER").rglob("*.tex"):
        text = f.read_text(encoding="utf-8")
        for c in re.findall(r"\\chapter\{([^}]*)\}", text):
            chapters_sections.append(f" * {c}")
        for s in re.findall(r"\\section\{([^}]*)\}", text):
            chapters_sections.append(f"    * {s}")

    return "\n".join(chapters_sections).replace("--", "-")


if __name__ == "__main__":
    print(extract())
