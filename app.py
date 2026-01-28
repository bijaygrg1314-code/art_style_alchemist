import streamlit as st
import torch
import os
import time
from style_network import TransformerNet
from utils import load_image, tensor_to_image, apply_edge_preservation

# --- Configuration ---
MODELS_DIR = "models"
os.makedirs(MODELS_DIR, exist_ok=True)

# --- UI Configuration ---
st.set_page_config(page_title="Art Style Alchemist", layout="wide")

# --- Logic Layer ---
@st.cache_resource
def load_model(style_name):
    """
    Loads the model weights, purposefully filtering out incompatible keys.
    This fixes the 'running_stats' error by manually removing them.
    """
    try:
        device = torch.device("cpu") # Force CPU for local privacy
        model = TransformerNet()     # Initialize architecture
        
        # Construct path
        model_path = os.path.join(MODELS_DIR, f"{style_name}.pth")
        
        if not os.path.exists(model_path):
            st.error(f"❌ File not found: {model_path}")
            return None

        # Load the file
        saved_file = torch.load(model_path, map_location=device)
        
        # 1. Extract the dictionary
        state_dict = None
        if isinstance(saved_file, dict):
            if "state_dict" in saved_file:
                state_dict = saved_file["state_dict"]
            elif "model_state" in saved_file:
                state_dict = saved_file["model_state"]
            else:
                state_dict = saved_file
        elif isinstance(saved_file, torch.nn.Module):
            state_dict = saved_file.state_dict()
        
        # 2. Fix Keys: Remove 'module.' prefix (from multi-GPU training)
        if state_dict:
            new_state_dict = {}
            for k, v in state_dict.items():
                name = k.replace("module.", "")
                new_state_dict[name] = v
            state_dict = new_state_dict

        # 3. NUCLEAR FILTER: Manually remove 'running_mean', 'running_var', etc.
        # This solves the "Unexpected running stats buffer" error.
        current_model_dict = model.state_dict()
        clean_state_dict = {}
        
        for k, v in state_dict.items():
            # Only keep keys that actually exist in our current model architecture
            if k in current_model_dict:
                # OPTIONAL: Check size mismatch here if needed, but usually not required
                if v.size() == current_model_dict[k].size():
                    clean_state_dict[k] = v
        
        # Load the cleaned dictionary
        model.load_state_dict(clean_state_dict)
        model.to(device)
        model.eval()
        return model

    except Exception as e:
        # Catches any other unexpected errors
        st.error(f"🔥 Error loading {style_name}: {str(e)}")
        return None

def run_inference(content_image, style_model):
    """Runs the neural network on the image."""
    with torch.no_grad():
        output = style_model(content_image)
    return tensor_to_image(output)

# --- Main App Layout ---

st.title("🎨 Art Style Alchemist")
st.markdown("""
**Transform your photos into masterpieces.** *Strictly local processing - your images never leave this computer.*
""")

# Sidebar controls
st.sidebar.header("Alchemy Lab")

# 1. Model Selection
available_models = [f.split('.')[0] for f in os.listdir(MODELS_DIR) if f.endswith('.pth')]
if not available_models:
    st.sidebar.warning(f"No models found in '{MODELS_DIR}'! Please run 'get_models.py'.")
    style_choice = None
else:
    style_choice = st.sidebar.selectbox("Choose an Art Style", available_models)

# 2. Parameters
intensity = st.sidebar.slider("Style Intensity / Detail Retention", 0.0, 1.0, 1.0, 
                              help="Lower values preserve more of the original photo details.")

# 3. Image Upload
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "png", "jpeg"])

# --- Main Processing Loop ---
if uploaded_file and style_choice:
    col1, col2 = st.columns(2)
    
    # Load and display original immediately
    image_tensor = load_image(uploaded_file, max_size=512)
    original_image = tensor_to_image(image_tensor)
    
    with col1:
        st.subheader("Original")
        st.image(original_image, use_container_width=True)

    with col2:
        st.subheader("Alchemized")
        
        # The 'Apply' button
        if st.button("Apply Style ✨", type="primary"):
            with st.spinner(f"Brewing {style_choice} potion..."):
                
                # 1. Load Model (Now uses Nuclear Filter)
                model = load_model(style_choice)
                
                if model:
                    # 2. Run Inference
                    start_time = time.time()
                    raw_stylized = run_inference(image_tensor, model)
                    
                    # 3. Post-processing (Blending/Edge Preservation)
                    final_result = apply_edge_preservation(original_image, raw_stylized, intensity)
                    
                    end_time = time.time()
                    
                    # 4. Display Result
                    st.image(final_result, caption=f"Finished in {end_time - start_time:.2f}s", use_container_width=True)
                    
                    # 5. Download Button
                    from io import BytesIO
                    buf = BytesIO()
                    final_result.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    
                    st.download_button(
                        label="Download Masterpiece 📥",
                        data=byte_im,
                        file_name=f"alchemist_{style_choice}.png",
                        mime="image/png"
                    )

# Footer
st.markdown("---")
st.caption("Project: Art Style Alchemist | Local CPU Inference")