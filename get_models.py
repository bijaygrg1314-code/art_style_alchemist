import os
import urllib.request
import zipfile
import shutil

# 1. Define the directory
save_dir = "models"
os.makedirs(save_dir, exist_ok=True)

# 2. URL for the standard PyTorch Style Transfer models
url = "https://www.dropbox.com/s/lrvwfehqdcxoza8/saved_models.zip?dl=1"
zip_path = os.path.join(save_dir, "saved_models.zip")
nested_folder = os.path.join(save_dir, "saved_models")

print(f"Downloading models to '{save_dir}'...")

try:
    # 3. Download (overwrite if exists to ensure clean file)
    urllib.request.urlretrieve(url, zip_path)
    print("Download complete! Unzipping...")

    # 4. Unzip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(save_dir)

    # 5. Move Files & Force Cleanup
    if os.path.exists(nested_folder):
        print("Moving files out of subdirectory...")
        
        # Loop through all files in the nested folder
        for filename in os.listdir(nested_folder):
            if filename.endswith(".pth"):
                source = os.path.join(nested_folder, filename)
                destination = os.path.join(save_dir, filename)
                
                # If the file already exists in 'models', replace it
                if os.path.exists(destination):
                    os.remove(destination)
                
                shutil.move(source, destination)
        
        # FORCE DELETE the 'saved_models' folder (removes .DS_Store and junk)
        shutil.rmtree(nested_folder) 
        print("Removed nested 'saved_models' folder.")

    # 6. Delete the zip file
    if os.path.exists(zip_path):
        os.remove(zip_path)

    print("✅ Success! Your .pth files are ready.")
    print(f"Files found in 'models': {[f for f in os.listdir(save_dir) if not f.startswith('.')]}")

except Exception as e:
    print(f"An error occurred: {e}")