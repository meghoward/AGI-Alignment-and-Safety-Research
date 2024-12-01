import os

# Define the directory path
directory = '/Users/meghoward/Documents/Imperial MSc/Term_2/Fairness/AGI/Coding'

# Initialize the table dictionary
table = {}

# Iterate over the directories in the main directory
for folder in os.listdir(directory):
    folder_path = os.path.join(directory, folder)
    
    # Check if the item is a directory and starts with 'format_'
    if os.path.isdir(folder_path) and folder.startswith("format_"):
        # Initialize the row for the current format
        table[folder] = {}
        
        # Iterate over the txt files in the current format folder
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            
            # Check if the item is a file
            if os.path.isfile(file_path):
                # Read the file and calculate the percentage score
                with open(file_path, 'r') as f:
                    lines = [line.strip() for line in f.readlines() if line.strip().isdigit()]
                    total_lines = len(lines)
                    percentage_score = sum(float(line) for line in lines) / total_lines
                    
                    # Store the score in the table
                    table[folder][file] = percentage_score

# Print the table
for format, scores in table.items():
    print(f"Format: {format}")
    for file, score in scores.items():
        print(f"File: {file}, Score: {score}")
    print()