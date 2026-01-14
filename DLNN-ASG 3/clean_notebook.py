import json

# Read the notebook
with open('MNIST.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Create a new cells list
cleaned_cells = []

# Indices of cells to remove (empty cells and duplicates)
skip_indices = {1, 2, 11, 12, 38}  # Empty markdown cells and duplicates

for idx, cell in enumerate(notebook['cells']):
    # Skip empty markdown cells
    if cell['cell_type'] == 'markdown' and not cell['source']:
        continue
    
    # Skip specific duplicate cells
    if idx in skip_indices:
        continue
    
    # Process markdown cells to remove URLs and update language
    if cell['cell_type'] == 'markdown' and cell['source']:
        new_source = []
        for line in cell['source']:
            # Skip lines with URLs in markdown links
            if 'https://' in line or 'http://' in line:
                # Remove URL references but keep text
                import re
                line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
            
            # Replace "we" with "I" (case-sensitive)
            line = line.replace('we will', 'I will')
            line = line.replace('We will', 'I will')
            line = line.replace('we are', 'I am')
            line = line.replace('We are', 'I am')
            line = line.replace('we can', 'I can')
            line = line.replace('We can', 'I can')
            line = line.replace('we would', 'I would')
            line = line.replace('We would', 'I would')
            line = line.replace('we have', 'I have')
            line = line.replace('We have', 'I have')
            line = line.replace(' we ', ' I ')
            line = line.replace('We ', 'I ')
           line = line.replace('our ', 'my ')
            line = line.replace('Our ', 'My ')
            
            new_source.append(line)
        
        cell['source'] = new_source
    
    cleaned_cells.append(cell)

# Update the notebook with cleaned cells
notebook['cells'] = cleaned_cells

# Write the cleaned notebook
with open('MNIST.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"Cleaned notebook saved. Reduced from {len(notebook['cells']) + len(skip_indices)} to {len(cleaned_cells)} cells.")
