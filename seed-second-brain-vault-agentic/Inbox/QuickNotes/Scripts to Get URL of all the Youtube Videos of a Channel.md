---
creation date: 2024-12-26 15:03
modification date: Thursday 26th December 2024 15:03:49
tags:
  - slipbox/permaNotes/python
  - inbox/fleetingNotes/scripts
  - inbox/mediaNotes/Satsanga
  - inbox/mediaNotes/Satsanga/PremanandjiMaharaj
description: A method to import the list of URLS of videos of a youtube channel.
source: https://www.youtube.com/watch?v=PxbRBqWmqas&ab_channel=Koolac
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

# Problem

**To get all the URLs of the videos in a youtube channel.**

---
# Solution:

## Script to scroll to the bottom of the page:

> [!Script]
> var scroll = setInterval(function(){ window.scrollBy(0, 1000)}, 1000);

---
## Script to scroll to the get the URLS 

```js
window.clearInterval(scroll); console.clear(); urls = $$('a'); urls.forEach(function(v,i,a){if (v.id=="video-title-link" && v.href){console.log('\t'+new Date().toLocaleDateString()+'\t'+v.title+'\t'+v.href+'\t'+v.__shady_native_innerHTML.match(/aria-label=\"(.+?)\"/g)?.[0].match(/[\d,]+ views/g)[0]+'\t')}});
```

## Script to properly format the text into markdown table. 

![[Pasted image 20241226154330.jpg]]

```python
import re  
  
# Define the input file and output Markdown file paths  
input_file = "/Users/harsh/Desktop/URLS.txt"  # Replace with your input file name  
output_file = "/Users/harsh/Desktop/output.md"  # Replace with your desired output Markdown file name  
  
# Regular expression to detect URLs starting with "https://www."  
url_pattern = re.compile(r"https://www\.[^\s]+")  
  
# Open the input file for reading  
with open(input_file, "r", encoding="utf-8") as infile:  
    lines = infile.readlines()  
  
# Create and write to the output Markdown file  
with open(output_file, "w", encoding="utf-8") as outfile:  
    # Write the table header  
    outfile.write("| publishDate | title | source |\n")  
    outfile.write("|-------------|-------|--------|\n")  
  
    # Process each line and format as a table row  
    for line in lines:  
        line = line.strip()  
        if not line:  
            continue  # Skip empty lines  
  
        # Find the URL in the line        match = url_pattern.search(line)  
        if match:  
            url = match.group()  
            # Split the line into parts before and after the URL  
            parts = line.split(url)  
            if len(parts) == 2:  
                # Extract the publishDate and title  
                publish_date = parts[0].strip().split("\t")[0]  
                title = parts[0].strip()[len(publish_date):].strip()  
                # Replace "|" in the title with "-"  
                title = title.replace("|", "-")  
                # Write the table row in Markdown format  
                outfile.write(f"| {publish_date} | {title} | [Link]({url}) |\n")  
  
print(f"Markdown table has been saved to {output_file}.")
```


## Issues Faced:

- The copied url list has | symbols in the title so it interferes in the columns in markdown format.
- The multiple spaces in the titles also interfered with URL detection. 
- URL's are being detected using regex.
- The published Date was imported all the entries had 2024-12-26 i.e. today. 
- There were undefined in many places and something like "V501" text somewhere which I removed manually. It was easy with a simple find and replace.


---

# Related Topics
###

---