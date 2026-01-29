# AI-4-Creativity-Project (25/26)

## Student name: Bijaya Gurung
## Student number: 2322514
## Project title: art_style_alchemist
## Link to project video recording: https://drive.google.com/file/d/1chvkKxVCTvDh85I1IUeH0WI4XZZQLO15/view?usp=drivesdk

---

## 🚀 Project Overview

**art_style_alchemist** is a local AI-powered application that transforms ordinary digital photographs into stunning artistic masterpieces using **Neural Style Transfer**. Built with a local PyTorch inference engine, it prioritizes **user privacy** and delivers **high-speed processing** — no cloud APIs, no data sharing, just pure creative transformation on your own device.

### ✨ Key Features
- 🖼️ **Transform photos** into various artistic styles
- 🔒 **100% local processing** – your images never leave your computer
- ⚡ **Optimized for CPU** – runs smoothly on standard laptops
- 🎚️ **Style intensity control** – blend between original and stylized results
- 📥 **One-click download** – save your artwork instantly

---

## 🏆 Technical Achievements

### 🔧 **Model Compatibility Engine**
- Developed a **"Nuclear Filter"** logic that resolves PyTorch version conflicts
- Automatically purges incompatible `running_stats` buffers during model loading
- Ensures seamless execution across different computational environments

### 🎨 **Hybrid Post-Processing Pipeline**
- Integrated **OpenCV-based alpha blending** for "Style Intensity" control
- Preserves **structural edges** of the original content while applying artistic styles
- Allows users to fine-tune the balance between preservation and transformation

### ⚡ **CPU Optimization**
- Designed specifically for **efficient local execution**
- Implements a specialized normalization pipeline for smooth performance
- Eliminates dependency on GPU hardware

---

## 🛠️ Setup Instructions

### 1. Environment Setup
```bash
# Create a new conda environment
conda create -n art_style_alchemist python=3.10 -y

# Activate the environment
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
