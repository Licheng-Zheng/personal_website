import os
import glob
from PIL import Image

def convert_pngs_to_webp(directory):
    """
    Recursively finds all .png files in the given directory,
    converts them to highly optimized .webp format, and deletes the original .png.
    """
    search_pattern = os.path.join(directory, "**", "*.png")
    png_files = glob.glob(search_pattern, recursive=True)
    
    if not png_files:
        print("No PNG files found to convert.")
        return

    count = 0
    for png_path in png_files:
        # Create the new filename with .webp extension
        webp_path = png_path.rsplit(".", 1)[0] + ".webp"
        
        try:
            with Image.open(png_path) as img:
                # Save as webp. quality=85 is a great balance of size/quality. 
                # method=6 uses the slowest/best compression algorithm.
                img.save(webp_path, "webp", quality=85, method=6)
            
            # Delete the original PNG to keep the directory clean
            os.remove(png_path)
            
            print(f"Converted: {os.path.basename(png_path)} -> {os.path.basename(webp_path)}")
            count += 1
        except Exception as e:
            print(f"Failed to convert {os.path.basename(png_path)}: {e}")

    print(f"\nSuccessfully converted {count} files to WebP.")

if __name__ == "__main__":
    # Target the assets/images directory relative to where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(current_dir, "assets", "images")
    
    if not os.path.exists(assets_dir):
        print(f"Error: Could not find directory {assets_dir}")
    else:
        print(f"Scanning {assets_dir} for PNG files...\n")
        convert_pngs_to_webp(assets_dir)
