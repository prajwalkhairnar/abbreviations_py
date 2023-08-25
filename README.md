

# abbreviations_py

`abbreviations_py` is a Python package that provides a convenient way to abbreviate and normalize text. It offers functionality to clean text by replacing common abbreviations with their full forms, removing punctuations and hashtags.

## Installation

You can install `abbreviations_py` using `pip`:

```bash
pip install git+https://github.com/prajwalkhairnar/abbreviations_py.git
```

## Usage

```python
from abbreviations_py.textes.abbreviator import fix, update_abbreviations

# Fix abbreviated text
input_text = "I'll txt you when you're back, ttyl! #BonVoyage"
result = fix(input_text)
print(result)
# Output: I will text you when you are back talk to you later

# Update abbreviation mappings
new_mappings = {
    "ttyl": "talk to you later",
    "txt": "text",
    # Add more mappings here
}

update_abbreviations(new_mappings)
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Created by [Prajwal Khairnar](https://github.com/prajwalkhairnar)


