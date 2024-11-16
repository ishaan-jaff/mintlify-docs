import os

def rename_md_to_mdx(directory):
    # Walk through all directories and files
    for root, dirs, files in os.walk(directory):
        # Find all .md files in current directory
        md_files = [f for f in files if f.endswith('.md')]
        
        # Rename each .md file to .mdx
        for md_file in md_files:
            old_path = os.path.join(root, md_file)
            new_path = os.path.join(root, md_file[:-3] + '.mdx')
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} → {new_path}")
            except Exception as e:
                print(f"Error renaming {old_path}: {e}")

if __name__ == "__main__":
    # Use current directory as starting point
    current_dir = os.getcwd()
    rename_md_to_mdx(current_dir)
    print("Finished renaming files")