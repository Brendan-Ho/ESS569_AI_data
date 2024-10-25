import pandas as pd
import numpy as np
import os
from collections import Counter

# Set paths to the cleaned data
cleaned_data_path = r'data/clean/cleaned_dna_sequences.csv'

# Load the cleaned data
dna_data = pd.read_csv(cleaned_data_path)

# Step 1: Define a function to count k-mers
def kmer_count(sequence, k):
    """Counts k-mers in a given DNA sequence and returns a count vector."""
    kmer_counts = Counter(sequence[i:i + k] for i in range(len(sequence) - k + 1))
    return kmer_counts

# Step 2: Generate a unique list of k-mers (could be dynamic based on all sequences)
k = 3  # Example: Set k to 3 for tri-nucleotides
all_kmers = set()

# Generate k-mers from all sequences
for seq in dna_data['DNA_Sequence']:
    all_kmers.update(kmer_count(seq, k).keys())

# Create a DataFrame for k-mer features
kmer_features = pd.DataFrame(columns=sorted(all_kmers))

# Step 3: Fill in the k-mer counts for each sequence
for index, row in dna_data.iterrows():
    counts = kmer_count(row['DNA_Sequence'], k)
    kmer_features.loc[index] = [counts.get(kmer, 0) for kmer in sorted(all_kmers)]

# Step 4: Combine the k-mer features with labels
final_data = pd.concat([kmer_features, dna_data['Label']], axis=1)

# Save the AI-ready data in a folder
ai_ready_data_dir = os.path.join('data', 'ai_ready')
os.makedirs(ai_ready_data_dir, exist_ok=True)

# Save the final DataFrame as a CSV file
ai_ready_path = os.path.join(ai_ready_data_dir, 'ai_ready_data_with_kmers.csv')
final_data.to_csv(ai_ready_path, index=False)

print(f"AI-ready data with k-mer counts saved to: {ai_ready_path}")

# Display the shape and feature description
print(f"Final data shape: {final_data.shape}")
print("Feature description:")
print(final_data.describe())
