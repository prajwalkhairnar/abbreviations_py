abbreviations\_py.textes package
================================


Installation
------------
.. code-block:: bash

   pip install abbreviations_py


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

   
