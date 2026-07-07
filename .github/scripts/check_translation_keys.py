import json
import sys
from pathlib import Path

LANG_DIR = Path("langs")
REFERENCE_FILE = LANG_DIR / "en_US.json"


def flatten_keys(data, prefix=""):
    keys = set()

    for key, value in data.items():
        current_key = f"{prefix}.{key}" if prefix else key

        if isinstance(value, dict):
            keys.update(flatten_keys(value, current_key))
        else:
            keys.add(current_key)

    return keys


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main():
    if not REFERENCE_FILE.exists():
        print(f"Reference file not found: {REFERENCE_FILE}")
        sys.exit(1)

    reference_keys = flatten_keys(load_json(REFERENCE_FILE))
    has_errors = False

    for lang_file in sorted(LANG_DIR.glob("*.json")):
        if lang_file.name == "en_US.json":
            continue

        lang_keys = flatten_keys(load_json(lang_file))
        missing_keys = sorted(reference_keys - lang_keys)

        if missing_keys:
            has_errors = True
            print(f"\n❌ Missing keys in {lang_file}:")
            for key in missing_keys:
                print(f"  - {key}")
        else:
            print(f"✅ {lang_file} contains all required keys.")

    if has_errors:
        sys.exit(1)

    print("\n✅ All translation files are valid.")


if __name__ == "__main__":
    main()