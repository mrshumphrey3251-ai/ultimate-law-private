import os
import urllib.request
import ssl
import shutil

# Bypass strict SSL limits for high-speed automated harvesting
ssl._create_default_https_context = ssl._create_unverified_context

print("⚡ Igniting Sovereign Harvester Engine...")

# Stable academic and public domain endpoints for the Ultimate Law
endpoints = [
    {"url": "https://www.gutenberg.org/cache/epub/10/pg10.txt", "filename": "Ultimate_Law_English_66.txt", "folder": "English_Core"},
    {"url": "https://www.gutenberg.org/cache/epub/4236/pg4236.txt", "filename": "Apocryphal_Texts.txt", "folder": "English_Core"},
    {"url": "https://raw.githubusercontent.com/scrollmapper/bible_databases/master/greek/TextusReceptus.txt", "filename": "Original_Greek_NT.txt", "folder": "Original_Greek"}
]

private_dir = r"C:\HVF_Repos\ultimate-law-private\The_Written_Word"
public_dir = r"C:\HVF_Repos\ultimate-law-public\The_Written_Word"

for item in endpoints:
    priv_folder = os.path.join(private_dir, item["folder"])
    pub_folder = os.path.join(public_dir, item["folder"])
    
    os.makedirs(priv_folder, exist_ok=True)
    os.makedirs(pub_folder, exist_ok=True)
    
    priv_filepath = os.path.join(priv_folder, item["filename"])
    pub_filepath = os.path.join(pub_folder, item["filename"])
    
    print(f"⬇️ Harvesting {item['filename']}...")
    try:
        urllib.request.urlretrieve(item["url"], priv_filepath)
        # Mirror instantly to the public vault
        shutil.copy2(priv_filepath, pub_filepath)
        size_kb = os.path.getsize(priv_filepath) // 1024
        print(f"✅ Secured and Mirrored: {item['filename']} ({size_kb} KB)")
    except Exception as e:
        print(f"❌ Failed to secure {item['filename']}: {e}")

print("✅ MASS DOWNLOAD COMPLETE. The foundational texts are locked in your vaults.")
