# 代码生成时间: 2025-09-21 07:18:11
import os
import zipfile
import tarfile

"""
A utility to decompress zip and tar files using Python.

This script provides a simple interface to extract files from zip and tar archives.
It checks the type of the file and uses the appropriate method to decompress it.
"""

def decompress_file(file_path, output_dir):
    """Decompresses a file to the specified output directory.

    Args:
        file_path (str): The path to the file to be decompressed.
        output_dir (str): The directory where the decompressed files will be placed.

    Raises:
        ValueError: If the file is not a zip or tar file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if file_path.endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
    elif file_path.endswith(('.tar', '.gz', '.tgz', '.tar.gz', '.bz2')):
        with tarfile.TarFile(file_path, 'r') as tar_ref:
            tar_ref.extractall(output_dir)
    else:
        raise ValueError(f"Unsupported file type: {file_path}. Only zip and tar files are supported.")

    print(f"Decompression of {file_path} completed successfully.")


def main():
    """Main function to run the decompression tool."""
    file_path = input("Enter the path to the file to decompress: ")
    output_dir = input("Enter the output directory path: ")
    try:
        decompress_file(file_path, output_dir)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()