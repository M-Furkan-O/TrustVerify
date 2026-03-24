import os
import json
from hash_utils import get_file_hash

# Manifest oluşturma
def create_manifest(directory):
    manifest = {}

    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)

            # metadata.json'u dahil etme
            if "metadata.json" in path:
                continue

            manifest[path] = get_file_hash(path)

    with open("metadata.json", "w") as f:
        json.dump(manifest, f, indent=4)

    print("Manifest oluşturuldu!")


# Dosya bütünlüğü kontrolü
def check_integrity():
    with open("metadata.json", "r") as f:
        manifest = json.load(f)

    tampered = False

    for path, old_hash in manifest.items():
        # Dosya silinmiş mi?
        if not os.path.exists(path):
            print(f"Dosya Silinmiş: {path}")
            tampered = True
            continue

        new_hash = get_file_hash(path)

        # Hash değişmiş mi?
        if new_hash != old_hash:
            print(f"Hash Değiştirilmiş: {path}")
            tampered = True

    if not tampered:
        print("Tüm dosyalar Sağlam!")