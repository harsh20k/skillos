---
creation date: 2024-12-25 18:49
modification date: Wednesday 25th December 2024 18:49:38
tags:
  - "#inbox/fleetingNotes/scripts"
  - "#slipbox/permaNotes/python"
description: As the title says
dg-publish: true
---
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
---

# Heading Substitution

## Problem:
The headings under Related topics section in the notes had the subheadings with ##. This resulted in the topics under related topics taking a lot of space and looking too big for my taste. 

---
## Solution:
Update the sub-headings under related topics with ### instead of ## using python script which was written by [[ChatGPT]].

---
## Script:

![[Pasted image 20241225190436.jpg]]

```python
import os  
  
# Define the path to the directory containing Markdown files  
VAULT_PATH = "/Users/harsh/Library/Mobile Documents/iCloud~md~obsidian/Documents/Notes"  
  
# Walk through the directory structure starting from VAULT_PATH  
for root, subFolders, files in os.walk(VAULT_PATH):  
    # Loop through each file in the current directory  
    for file in files:  
        # Process only Markdown files  
        if file.endswith('.md'):  
            # Construct the full file path  
            file_path = os.path.join(root, file)  
  
            # Read all lines of the file  
            with open(file_path, "r") as f:  
                lines = f.readlines()  
  
            # Initialize flags and containers  
            updated_lines = []  
            related_topics_found = False  
  
            # Process each line in the file  
            for line in lines:  
                # Check for the "# Related Topics" heading  
                if line.strip() == "# Related Topics":  
                    related_topics_found = True  
                    updated_lines.append(line)  # Keep the heading as is  
                # If under the "Related Topics" section and it's a subheading                elif related_topics_found and line.startswith("## "):  
                    updated_lines.append(line.replace("## ", "### ", 1))  # Convert to "###"  
                # Stop conversion if a non-subheading or unrelated line appears                elif related_topics_found and not line.startswith("## "):  
                    related_topics_found = False  
                    updated_lines.append(line)  # Add the unrelated line as is  
                else:  
                    updated_lines.append(line)  # Add other lines as is  
  
            # Write the updated content back to the file            with open(file_path, "w") as f:  
                f.writelines(updated_lines)  
  
            print(f"Updated subheadings under 'Related Topics' in file: {file}")
```

---
# Related Topics
### [[Python]]

---