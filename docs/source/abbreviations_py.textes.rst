abbreviations\_py.textes package
================================

Installation
------------
.. code-block:: bash

   pip install git+https://github.com/prajwalkhairnar/abbreviations_py.git


abbreviations\_py.textes.abbreviator module
-------------------------------------------

.. automodule:: abbreviations_py.textes.abbreviator
   :members:
   :undoc-members:
   :show-inheritance:




Usage Example
-------------

.. code-block:: python

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

   


