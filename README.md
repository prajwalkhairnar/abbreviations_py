

# abbreviations_py

`abbreviations_py` is a Python package that provides a convenient way to abbreviate and normalize text. It offers functionality to clean text by replacing common abbreviations with their full forms, removing punctuations and hashtags.

## Installation

You can install `abbreviations_py` using `pip`:

```bash
pip install abbreviations_py
```

## Usage

```python
from abbreviations_py.textes.abbreviator import abbreviate, update_abbreviations

# Abbreviate text
input_text = "Hello! gr8 to meet you"
result = abbreviate(input_text)
print(result)

# Update abbreviation mappings
new_mappings = {
    "gr8": "great",
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


