import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Convert the table to a Pandas DataFrame for easier visualisation
data = []
for format, scores in table.items():
    for file, score in scores.items():
        data.append({'Format': format, 'File': file, 'Score': score})

df = pd.DataFrame(data)


# Split the file names to extract model type and format
df['Model'] = df['File'].apply(lambda x: x.split('_')[2])  # Extract model type
df['Prompt Style'] = df['Format'].str.split('_').str[-1]  # Extract format number

# Create a grouped bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='Prompt Style', y='Score', hue='Model', data=df, palette='tab10')

# Add titles and labels
plt.title('Scores Grouped by Prompt Style and Colored by Model Type')
plt.ylabel('Percentage Score')
plt.xlabel('Prompt Style')
plt.legend(title='Model', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save and display the plot
plt.savefig('grouped_barplot_scores_by_prompt_style_and_model.png')
plt.show()

# Create a heatmap for scores
heatmap_data = df.pivot(index='File', columns='Format', values='Score')
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={'label': 'Score'})
plt.title('Heatmap of Scores by Format and File')
plt.ylabel('File')
plt.xlabel('Format')
plt.tight_layout()
plt.savefig('heatmap_scores_by_format_and_file.png')
plt.show() 
