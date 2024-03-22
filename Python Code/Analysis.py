import os
import tarfile
import gzip
import pandas as pd

def read_eeg_file(tar_gz_path, trial_file_index=0):
    # Extract the .tar.gz file
    with tarfile.open(tar_gz_path, 'r:gz') as tar:
        # Determine the path to extract files (in the same directory as the tar.gz file)
        extracted_path = os.path.join(os.path.dirname(tar_gz_path), tar.getnames()[0])
        tar.extractall(path=os.path.dirname(extracted_path))
        
    # List the files in the extracted directory
    data_files = os.listdir(extracted_path)
    data_files.sort()  # Sort the files for better readability
    
    # Select the specified trial file index
    trial_file_name = data_files[trial_file_index]
    trial_file_path = os.path.join(extracted_path, trial_file_name)
    
    # Since the trial file is also gzipped, we need to extract it
    with gzip.open(trial_file_path, 'rt') as file:
        # Read the file into a pandas DataFrame
        # Assuming the data is space-separated and columns are ['Trial', 'Sensor', 'Sample', 'Value']
        df = pd.read_csv(file, 
                         delim_whitespace=True,  # Use whitespace as delimiter
                         comment='#',  # Ignore comments (lines starting with #)
                         names=['Trial', 'Sensor', 'Sample', 'Value'])  # Set the column names
    return df

# Example usage:
# Provide the path to the tar.gz file
tar_gz_file_path = 'eeg+database/eeg_full/co2a0000364.tar.gz'  # Replace with your file's path

# Calling the function and passing the index of the trial file (0 for the first file)
df = read_eeg_file(tar_gz_file_path, 0)

# Display the first few rows of the DataFrame
print(len(df))
