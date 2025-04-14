import os
import tarfile
import urllib.request

url = "https://s3.eu-west-1.amazonaws.com/repo-doc-onlyoffice-com/builder/linux/generic/onlyoffice-documentbuilder-8.3.3-17-x86_64.tar.xz"
archive_path = "onlyoffice-documentbuilder.tar.xz"
extract_path = "./app"

# Download the file
print("Downloading...")
urllib.request.urlretrieve(url, archive_path)

# Create target folder if not exists
os.makedirs(extract_path, exist_ok=True)

# Extract the archive
print("Extracting...")
with tarfile.open(archive_path, "r:xz") as tar:
    tar.extractall(path=extract_path)

print(f"✅ Done! Extracted to: {extract_path}")
