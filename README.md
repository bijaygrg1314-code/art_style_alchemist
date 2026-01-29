# AI-4-Creativity-Project (25/26)

## Student name: Bijaya Gurung
## Student number: 2322514
## Project title: art_style_alchemist
## Link to project video recording: [INSERT LINK HERE]

---

# Project Description
**art_style_alchemist** is a local AI application designed to transform digital photography into artistic masterpieces using Neural Style Transfer. By utilizing a local PyTorch inference engine, the project prioritizes user privacy and high-speed processing without the need for external cloud APIs.

---

# Technical Achievements
* **Model State Dictionary Filtering**: Developed a "Nuclear Filter" logic in the loading sequence to resolve PyTorch versioning conflicts. This manually purges incompatible `running_stats` buffers, allowing the app to run seamlessly across different environments.
* **Hybrid Post-Processing**: Integrated OpenCV-based alpha blending to provide a "Style Intensity" control, allowing for structural edge preservation of the original content.
* **CPU Optimization**: Designed for efficient local execution, utilizing a specialized normalization pipeline to ensure smooth performance on standard laptop hardware.



---

# Setup instructions

### 1. Environment Setup
```
# Create a new environment named after the project
conda create -n art_style_alchemist python=3.10 -y
```
# Activate the environment
```
conda activate art_style_alchemist
```

## 2. Install Dependencies
```
pip install streamlit torch torchvision pillow numpy opencv-python-headless
```
## 3. Initialize Models
```
# Downloads and organizes the .pth files
python get_models.py
```
## 4. Run Application
```
streamlit run app.py
```
## How to Use
# Upload: Drag and drop an image (JPG/PNG).

# Select Style: Choose a style (e.g., Mosaic, Udnie) from the sidebar.

# Adjust Intensity: Use the slider to keep more or less of your original photo's detail.

# Apply: Click the "Apply Style" button.

# Download: Save your artwork to your computer.

📂 Project File Structure
```
art_style_alchemist/
├── app.py                # Main Streamlit UI and model loading logic
├── style_network.py      # TransformerNet architecture (the AI brain)
├── utils.py              # Image processing and edge preservation tools
├── get_models.py         # Automation script to download .pth files
├── requirements.txt      # List of necessary Python libraries
├── README.md             # Project documentation and setup guide
├── .gitignore            # Tells Git which files to ignore (like __pycache__)
└── models/               # Folder containing the neural network weights
    ├── candy.pth
    ├── mosaic.pth
    ├── rain_princess.pth
    └── udnie.pth
```
