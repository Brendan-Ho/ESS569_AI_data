import csv
# Define the phrase you're searching for
target_phrase = "stool"
file_path = r'c:\Users\kathe\Documents\GitHub\ESS569_AI_data\HMP_Data_Links\healthy_human_subjects_links.tsv'

# Step 1: Read the TSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file, delimiter='\t')
    # Filter rows that contain the target phrase
    filtered_data = [row for row in reader if target_phrase in ' '.join(row)]

# Step 2: Write only the matching rows back to the TSV file
with open('filtered_hhs_links.tsv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(filtered_data)
