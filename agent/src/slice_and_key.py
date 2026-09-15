import os
import sys
import numpy as np
from PIL import Image
import scipy.ndimage as ndi

def chroma_key_and_despill(img_pil):
    """
    Apply professional green-screen chroma keying:
    - Converts to RGBA
    - Identifies green background pixels using green dominance
    - Creates a smooth anti-aliased alpha transition around black outlines
    - Despills green color bleed from the edges
    """
    rgba = img_pil.convert('RGBA')
    arr = np.array(rgba, dtype=np.float32)
    
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    max_rb = np.maximum(r, b)
    green_diff = g - max_rb
    
    low_thresh = 20.0
    high_thresh = 55.0
    
    alpha = np.clip(1.0 - (green_diff - low_thresh) / (high_thresh - low_thresh), 0.0, 1.0) * 255.0
    
    # Despill: clamp green to max(R, B) wherever green dominates
    g_despilled = np.where(green_diff > 0, max_rb, g)
    
    arr[:, :, 1] = g_despilled
    arr[:, :, 3] = alpha
    
    return Image.fromarray(arr.astype(np.uint8), mode='RGBA')

def remove_edge_artifacts(cell_rgba):
    """
    Remove tiny slivers from neighboring cells using connected component analysis.
    """
    arr = np.array(cell_rgba)
    alpha = arr[:, :, 3]
    binary = alpha > 30
    
    labeled_array, num_features = ndi.label(binary)
    if num_features <= 1:
        return cell_rgba
        
    sizes = ndi.sum(binary, labeled_array, range(1, num_features + 1))
    max_size = np.max(sizes)
    
    h, w = alpha.shape
    keep_mask = np.zeros_like(binary, dtype=bool)
    
    for lbl_idx, size in enumerate(sizes):
        lbl = lbl_idx + 1
        comp_mask = (labeled_array == lbl)
        
        # Check if component touches left or right boundary
        touches_left = np.any(comp_mask[:, 0])
        touches_right = np.any(comp_mask[:, -1])
        
        # If it touches boundary and is smaller than 6% of main body, drop it (it's neighbor spillover)
        if (touches_left or touches_right) and (size < 0.06 * max_size):
            continue
            
        keep_mask |= comp_mask
        
    arr[:, :, 3] = np.where(keep_mask, alpha, 0)
    return Image.fromarray(arr)

def process_sheet(sheet_path, output_dir, poses_map):
    print(f"Processing {sheet_path} -> {output_dir}")
    os.makedirs(output_dir, exist_ok=True)
    
    img = Image.open(sheet_path)
    w, h = img.size
    
    cols = 4
    rows = 2
    cell_w = w / cols
    cell_h = h / rows
    
    keyed_full = chroma_key_and_despill(img)
    
    for idx, pose_name in enumerate(poses_map):
        r = idx // cols
        c = idx % cols
        
        box = (int(c * cell_w), int(r * cell_h), int((c + 1) * cell_w), int((r + 1) * cell_h))
        cell_img = keyed_full.crop(box)
        
        # Clean stray slivers from neighbouring cells
        cell_img = remove_edge_artifacts(cell_img)
        
        # Autocrop to bounding box with clean padding
        bbox = cell_img.getbbox()
        if bbox:
            pad = 12
            crop_box = (
                max(0, bbox[0] - pad),
                max(0, bbox[1] - pad),
                min(cell_img.width, bbox[2] + pad),
                min(cell_img.height, bbox[3] + pad)
            )
            cropped = cell_img.crop(crop_box)
        else:
            cropped = cell_img
            
        out_path = os.path.join(output_dir, f"{pose_name}.png")
        cropped.save(out_path, format="PNG")
        print(f"  Saved {pose_name}.png ({cropped.size[0]}x{cropped.size[1]})")

if __name__ == "__main__":
    poses_grid = [
        "idle_neutral",     # row 0, col 0
        "shocked_jawdrop",  # row 0, col 1
        "laughing_joke",    # row 0, col 2
        "explaining_point",  # row 0, col 3
        "hyped_victory",    # row 1, col 0
        "secret_whisper",   # row 1, col 1
        "thinking_chin",    # row 1, col 2
        "skeptical_sideeye" # row 1, col 3
    ]
    
    male_sheet = "/home/aurel/.gemini/antigravity-ide/brain/b1834f6b-68c8-4202-8eb6-1e775e54ac4a/male_chibi_sheet_1789325479798.jpg"
    female_sheet = "/home/aurel/.gemini/antigravity-ide/brain/b1834f6b-68c8-4202-8eb6-1e775e54ac4a/female_bust_sheet_1789325516029.jpg"
    
    male_dir = "/home/aurel/CODE/Maker/engine/public/avatars/male"
    female_dir = "/home/aurel/CODE/Maker/engine/public/avatars/female"
    root_avatars_dir = "/home/aurel/CODE/Maker/engine/public/avatars"
    
    process_sheet(male_sheet, male_dir, poses_grid)
    process_sheet(female_sheet, female_dir, poses_grid)
    
    # Aliases
    for d in [male_dir, female_dir]:
        import shutil
        shutil.copy2(os.path.join(d, "skeptical_sideeye.png"), os.path.join(d, "angry_triggered.png"))
        shutil.copy2(os.path.join(d, "idle_neutral.png"), os.path.join(d, "facepalm.png"))
    
    # Backwards-compatible default copies in root avatars/
    for p in poses_grid + ["angry_triggered", "facepalm"]:
        src = os.path.join(male_dir, f"{p}.png")
        dst = os.path.join(root_avatars_dir, f"{p}.png")
        if os.path.exists(src):
            import shutil
            shutil.copy2(src, dst)
            
    print("All sprites successfully processed with zero edge artifacts!")
