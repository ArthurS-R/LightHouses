import pandas as pd
import requests
import re
import time
import os
from urllib.parse import urlparse

# Configuration
START_INDEX = 0  # Change this to start from a different row
END_INDEX = 10   # Change this to download only the first 10, or set to None for all
DELAY_SECONDS = 2  # Delay between requests (increase if needed)

# Set headers to avoid 403 errors from Wikimedia
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

df = pd.read_csv("US Lighthouses - FINAL!.csv")

def make_image_filename(id_value, image_url):
    name = str(id_value).strip()
    name = re.sub(r'[\\/*?:"<>|]', "_", name)

    extension = ".jpg"
    parsed_path = urlparse(image_url).path
    if "." in parsed_path.rsplit("/", 1)[-1]:
        extension = "." + parsed_path.rsplit(".", 1)[-1]

    return f"{name}{extension}"



# Select subset of data
df_subset = df.iloc[START_INDEX:END_INDEX] if END_INDEX else df

print(f"Downloading {len(df_subset)} images (from index {START_INDEX})...\n")

successful = 0
failed = 0

for index, row in df_subset.iterrows():
    url = row["image"]
    file_name = make_image_filename(row["ID"], url)
    
    # Skip if file already exists
    if os.path.exists(file_name):
        print(f"Skipping {index + 1}/{len(df)}: {file_name} (already exists)")
        successful += 1
        continue
    
    print(f"Downloading {index + 1}/{len(df)}: {file_name}...")
    
    try:
        # Add delay to respect Wikimedia rate limits
        time.sleep(DELAY_SECONDS)
        
        r = requests.get(url, headers=headers, allow_redirects=True, timeout=30)
        r.raise_for_status()
        
        if len(r.content) > 0:
            with open(file_name, "wb") as f:
                f.write(r.content)
            print(f"  ✓ Saved ({len(r.content)} bytes)")
            successful += 1
        else:
            print(f"  ✗ Empty response")
            failed += 1
    except Exception as e:
        print(f"  ✗ Failed: {e}")
        failed += 1

print(f"\n{'='*50}")
print(f"Download complete: {successful} successful, {failed} failed")
print(f"{'='*50}")