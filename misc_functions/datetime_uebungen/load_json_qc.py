# 01_ngp_analysis/scripts/extract_presets.py
import os, re, json, base64, binascii, sys

INPUT_FILE = sys.argv[1] if len(sys.argv) > 1 else "backup.json"
OUT_DIR = "extracted_presets"
os.makedirs(OUT_DIR, exist_ok=True)

counter = 0
b64_re = re.compile(r'^[A-Za-z0-9+/=\s]+$')

def safe(name: str) -> str:
    return re.sub(r'[^a-zA-Z0-9._-]+', "_", name)[:80] or "field"

def is_base64(s: str) -> bool:
    if len(s) < 8 or not b64_re.match(s): return False
    try:
        base64.b64decode(s, validate=True)
        return True
    except binascii.Error:
        return False

def save_bytes(data: bytes, path_hint: str) -> str:
    global counter
    counter += 1
    # Grobe Signatur-Erkennung
    ext = ".bin"
    if data[:4] == b"RIFF": ext = ".wav"
    elif data[:4] == b"fLaC": ext = ".flac"
    elif data[:4] == b"OggS": ext = ".ogg"
    elif data[:2] == b"PK":   ext = ".zip"
    out = os.path.join(OUT_DIR, f"{counter}_{safe(path_hint)}{ext}")
    with open(out, "wb") as f: f.write(data)
    return out

def save_text(text: str, path_hint: str) -> str:
    global counter
    counter += 1
    # JSON hübsch machen, falls möglich
    try:
        obj = json.loads(text)
        out = os.path.join(OUT_DIR, f"{counter}_{safe(path_hint)}.json")
        with open(out, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        return out
    except Exception:
        out = os.path.join(OUT_DIR, f"{counter}_{safe(path_hint)}.txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        return out

def handle_string(s: str, path_hint: str):
    if not is_base64(s): return
    decoded = base64.b64decode(s)
    try:
        text = decoded.decode("utf-8")
        # Nur speichern, wenn lesbar/ sinnvoll
        return ("text", save_text(text, path_hint), len(decoded))
    except UnicodeDecodeError:
        return ("bin", save_bytes(decoded, path_hint), len(decoded))

def walk(node, path="root"):
    if isinstance(node, dict):
        for k, v in node.items():
            walk(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{path}[{i}]")
    elif isinstance(node, str):
        res = handle_string(node, path)
        if res:
            kind, out, n = res
            print(f"[{kind.upper():4}] {path} → {out} ({n} bytes)")

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"🔍 Datei geladen: {INPUT_FILE}")
    walk(data)
    print(f"\n✅ Fertig. Dateien liegen in: {OUT_DIR}")

if __name__ == "__main__":
    main()
