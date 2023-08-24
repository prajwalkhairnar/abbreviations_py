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

   from abbreviations_py.textes.abbreviator import fix, update_abbreviations

   # Fix abbreviated text
   input_text = "Hello! gr8 to meet you"
   result = fix(input_text)
   print(result)

   # Update abbreviation mappings
   new_mappings = {
       "gr8": "great",
       "txt": "text",
       # Add more mappings here
   }

   update_abbreviations(new_mappings)

   
