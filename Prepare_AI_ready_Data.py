import pandas as pd
import numpy as np
import os

# Set paths to the cleaned data
cleaned_data_path = r'data/clean/cleaned_dna_sequences.csv'

# Load the cleaned data
dna_data = pd.read_csv(cleaned_data_path)

# Step 1: Organize data into AI-ready format
# In this example, we'll assume that 'DNA_Sequence' is a feature and 'Label' is the target
# Convert sequences into numerical features for machine learning (e.g., one-hot encoding, k-mer count)
def sequence_to_features(seq):
    # Example: Simple nucleotide one-hot encoding (A, C, G, T)
    one_hot_map = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1]}
    return np.array([one_hot_map.get(nucleotide, [0, 0, 0, 0]) for nucleotide in seq]).flatten()

# Apply the conversion to the DNA sequences
dna_data['Features'] = dna_data['DNA_Sequence'].apply(sequence_to_features)

# Step 2: Prepare final DataFrame for ML
# Example: Split 'Features' and 'Labels' for machine learning
X = np.vstack(dna_data['Features'].values)
y = dna_data['Label'].values  # Assuming 'Label' column has the classification

# Save the AI-ready data in a folder
ai_ready_data_dir = os.path.join('data', 'ai_ready')
os.makedirs(ai_ready_data_dir, exist_ok=True)

# Save X (features) and y (labels) as separate files or in a single CSV
ai_ready_path = os.path.join(ai_ready_data_dir, 'ai_ready_data.npz')
np.savez(ai_ready_path, X=X, y=y)

print(f"AI-ready data saved to: {ai_ready_path}")
