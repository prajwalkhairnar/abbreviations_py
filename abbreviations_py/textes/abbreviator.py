import re
import json
import os

# Get the path of the current directory
package_dir = os.path.dirname(os.path.abspath(__file__))

# Load abbreviation mappings
abbreviation_file_path = os.path.join(package_dir, "abbreviation_mappings.json")
with open(abbreviation_file_path, "r") as json_file:
    abbreviation_mappings = json.load(json_file)

def abbreviate(text):
    # Remove punctuations, emojis and hashtags
    text = re.sub(r'(<3|#\w+|[^\w\s])', '', text)
    
    # Replace abbreviations with their full forms
    words = text.split()

    normalized_words = [word.lower() for word in words]
    
    words_abbr = [abbreviation_mappings.get(word, word) for word in normalized_words]
    
    
    
    return ' '.join(words_abbr)

def update_abbreviations(new_mappings):
    abbreviation_mappings.update(new_mappings)
    # Save the updated mappings back to the file
    with open(abbreviation_file_path, "w") as json_file:
        json.dump(abbreviation_mappings, json_file, indent=4)
