Hello!

This is a repository for python applications

1. word_counter:
   
   This program will check if you want to find a specific word in either a predefined list or a list you create yourself. There are two different search options available for finding the word:
   
   - Exact search - This is case-sensitive, meaning the search will look for the word exactly as you type it. For example, if you search for "Banana" (with a capital B), it will only find "Banana" and not "banana".
   - Case-insensitive search - This ignores capitalization, meaning the search will find the word regardless of uppercase or lowercase letters. For example, searching for "banana" will find both "banana" and "Banana".
   
   The predefined list contains the following words: ["apple", "banana", "Apple", "orange", "Banana", "apple"]

   **Example Results:**
   - If you select exact word search and input "Banana", the result will be:
      "The word 'Banana' appears at position(s) [4]."
   - If you select case-insensitive search (answering "no" to exact word search) and input "banana", the result will be:
      "The word 'banana' appears at position(s) [1, 4]."
   
   This is because in the first case, only the capitalized "Banana" at position 4 matches exactly, while in the second case, both "banana" at position 1 and "Banana" at position 4 are considered matches when ignoring capitalization.
