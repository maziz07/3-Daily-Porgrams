import os

def batch_rename_files(directory, prefix):
    for filename in os.listdir(directory):
        new_name = prefix + filename
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"Renamed {filename} to {new_name}")

# Example usage
batch_rename_files('path/to/your/directory', 'prefix_')
