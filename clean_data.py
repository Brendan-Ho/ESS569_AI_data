import pandas as pd
import os

# Set the paths to the raw files
dna_sequences_path = r'C:\Users\m1lfslay3r6000\Downloads\RDPClassifier_16S_trainsetNo19_QiimeFormat\dna_sequences.txt'
otu_sequences_path = r'C:\Users\m1lfslay3r6000\Downloads\RDPClassifier_16S_trainsetNo19_QiimeFormat\otu_sequences.fa'

# Create directory for cleaned data if it doesn't exist
cleaned_data_dir = os.path.join('data', 'clean')
os.makedirs(cleaned_data_dir, exist_ok=True)

# Load the text and FASTA files (example for the text file)
# For demonstration, let's assume it's a tab-delimited file
dna_data = pd.read_csv(dna_sequences_path, sep='\t')

# Step 1: Handling missing values
# You can choose to drop rows or fill missing values with some logic
dna_data.dropna(inplace=True)  # Example: Drop rows with missing data

# Step 2: Handling outliers (example for numeric data)
# Assume we have a numerical column to filter outliers
numeric_cols = ['Sequence_Length']  # Example of a column
for col in numeric_cols:
    # Remove outliers using standard deviation (or other methods)
    dna_data = dna_data[(dna_data[col] > dna_data[col].mean() - 3 * dna_data[col].std()) &
                        (dna_data[col] < dna_data[col].mean() + 3 * dna_data[col].std())]

# Step 3: Ensuring data consistency (uniform formatting)
# Example: Convert all sequences to uppercase for consistency
dna_data['DNA_Sequence'] = dna_data['DNA_Sequence'].str.upper()

# Save the cleaned data to a new file
cleaned_dna_sequences_path = os.path.join(cleaned_data_dir, 'cleaned_dna_sequences.csv')
dna_data.to_csv(cleaned_dna_sequences_path, index=False)

print(f"Cleaned data saved to: {cleaned_dna_sequences_path}")
