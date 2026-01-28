# AI-4-Creativity-Project-Template (25/26)

## Student name: Bijaya Gurung
## Student number: 2322514
## Project title: Art Style Alchemist
## Link to project video recording: [INSERT LINK HERE]

---

# Project Description

**Art Style Alchemist** is an interactive, local AI application that transforms ordinary photos into artistic masterpieces. Unlike cloud-based generators, this tool runs entirely on your local CPU, ensuring total privacy for your personal images.

Built with **Streamlit** and **PyTorch**, it allows users to apply styles (like Van Gogh or Picasso) to their photos with adjustable intensity, blending the original photo's details with the artistic texture.

---

# Setup instructions:

Follow these steps to set up the environment and run the application on your local machine.

### 1. Prerequisite: Anaconda / Miniconda
Ensure you have Conda installed. Open your terminal (or Anaconda Prompt) and run the following commands to create a clean environment.

```
# Create a new environment named 'art_alchemy' with Python 3.10
conda create -n art_alchemy python=3.10 -y
```
# Activate the environment
```
conda activate art_alchemy
```

2. Install Dependencies
```
Install the required libraries (Streamlit, PyTorch, Pillow, OpenCV).



pip install -r requirements.txt
```
Note: If you do not have a requirements.txt file yet, you can install them manually using the command below:

```

pip install streamlit torch torchvision pillow numpy opencv-python-headless
```
3. Download the AI Models
The application requires pre-trained neural network weights (.pth files). A script is provided to download and organize them automatically.

B```
# Run the automated download script
python get_models.py
```
This command will download the standard style weights (Mosaic, Candy, Rain Princess, Udnie) and place them correctly in the models/ folder.

4. Run the Application
Launch the interface using Streamlit.

```

streamlit run app.py
``` 

## How to Use
# Upload: 
Drag and drop an image (JPG/PNG) into the upload box.

# Select Style: 
Choose a style from the sidebar dropdown (e.g., "mosaic", "candy").

# Adjust Intensity: 
Use the slider to control how much of the original photo's detail is preserved.

# Apply: C
lick the "Apply Style ✨" button to generate your artwork.

# Download: 
Click "Download Masterpiece" to save the result.

## Troubleshooting
"No models found": Ensure you ran python get_models.py and that the .pth files are directly inside the models/ folder, not in a subfolder.

"Unexpected running stats buffer": The application includes a "Nuclear Filter" to handle this specific PyTorch version mismatch automatically. Ensure you are using the latest version of app.py.