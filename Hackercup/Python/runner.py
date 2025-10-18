import os
import sys
import shutil
import zipfile
import subprocess
from pathlib import Path
import time

HOME = Path.home()
DOWNLOADS = HOME / "Downloads"
CWD = Path.cwd()
HACKER_FILE = CWD / "HackerCup.py"
TARGET_NAME = "input.txt"

def find_latest_zip(downloads_path: Path):
    zips = sorted(downloads_path.glob("*.zip"), key=lambda p: p.stat().st_mtime, reverse=True)
    return zips[0] if zips else None

def extract_with_zipfile(zip_path: Path, pwd: str, dest: Path) -> bool:
    with zipfile.ZipFile(zip_path, 'r') as zf:
        pwd_bytes = pwd.encode() if pwd else None
        zf.extractall(path=dest, pwd=pwd_bytes)
    return True

def extract_with_7zip(zip_path: Path, pwd: str, dest: Path) -> bool:
    exe_candidates = ["7z", "7za", "7zr"]
    for exe in exe_candidates:
        if shutil.which(exe):
            cmd = [exe, "x", str(zip_path), f"-o{str(dest)}", "-y"]
            if pwd:
                cmd.insert(2, f"-p{pwd}")
            proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if proc.returncode == 0:
                return True
    return False

def pick_first_regular_file(search_dir: Path):
    for root, dirs, files in os.walk(search_dir):
        for f in files:
            candidate = Path(root) / f
            if candidate.is_file():
                return candidate
    return None

def main():
    zip_path = find_latest_zip(DOWNLOADS)
    if not zip_path:
        print("No .zip files found in Downloads.")
        sys.exit(1)

    dest_zip = CWD / zip_path.name
    shutil.move(str(zip_path), str(dest_zip))

    pwd = input("Enter password for the zip file (visible): ")

    extract_dir = CWD / (dest_zip.stem + "_extracted_" + str(int(time.time())))
    extract_dir.mkdir(exist_ok=True)

    ok = extract_with_7zip(dest_zip, pwd, extract_dir)
    if not ok:
        ok = extract_with_zipfile(dest_zip, pwd, extract_dir)

    extracted_file = pick_first_regular_file(extract_dir)
    target_path = CWD / TARGET_NAME
    if target_path.exists():
        backup = CWD / (TARGET_NAME + ".bak")
        shutil.move(str(target_path), str(backup))

    os.replace(str(extracted_file), str(target_path))

    if HACKER_FILE.exists():
        subprocess.run([sys.executable, str(HACKER_FILE)])

if __name__ == "__main__":
    main()
