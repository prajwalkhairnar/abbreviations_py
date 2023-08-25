import re
import json
import os

# Get the path of the current directory
package_dir = os.path.dirname(os.path.abspath(__file__))

# Load abbreviation mappings
abbreviation_file_path = os.path.join(package_dir, "abbreviation_mappings.json")
with open(abbreviation_file_path, "r") as json_file:
    abbreviation_mappings = json.load(json_file)

def fix(text):
    
    """
    Fixes the abbreviated input text by replacing abbreviations, removing punctuations and hashtag terms.

    Parameters:
    text (str): The input abbreviated text to be fixed.
    
    Returns:
    str: The fixed text.

	
    """


    # Remove punctuations, emojis and hashtags
    text_punc = re.sub(r' *[<3#][^ ]* *', '', text)
    text_punc = re.sub(r'[^a-zA-Z0-9\']+', ' ', text_punc).strip()


    # Split text into words    
    words = text_punc.split()

    # Convert words to lowercase
    normalized_words = [word.lower() for word in words]
    
    # Replace abbreviations with their full forms
    words_fixed = [abbreviation_mappings.get(word, word) for word in normalized_words]
    
    text_fixed = ' '.join(words_fixed)

    
    # Return processes string
    return text_fixed

def update_abbreviations(new_mappings):

    """
    Updates the abbreviation mappings dictionary with new key-value pairs.

    Parameters:
    new_mappings (dict): The new key-value pairs to add to the abbreviation mappings.

    Returns:
    None
    """

    # Update mappings	
    abbreviation_mappings.update(new_mappings)

    # Save the updated mappings back to the file
    with open(abbreviation_file_path, "w") as json_file:
        json.dump(abbreviation_mappings, json_file, indent=4)
