from collections import Counter

predifinied_list = input("Do you want a predifined list of words to be used? (yes/no): ").strip().lower()
if predifinied_list not in ['yes', 'no']:
    print("Invalid choice. Please enter 'yes' or 'no'.")
    exit()


# Getting the list of words from the user or using a predefined list
if predifinied_list == 'yes':
  words = ["apple", "banana", "Apple", "orange", "Banana", "apple"]
  print(f"Predifined list will be used. This is the list {words}")
else:
  # Getting a list of words from the user
  user_input = input("Enter a list of words separated by commas:")
  words = [word.strip() for word in user_input.split(",")]
  print(f"The list you entered is {words}")
  
  #checking if the user wants to keep the list or re-enter
  keep_list=input("Do you want to keep it like this? (yes/no):").strip().lower()
  if keep_list not in ['yes', 'no']:
    print("Invalid choice. Please enter 'yes' or 'no'.")
  
  if keep_list=='no':
    user_input = input("Re-enter a list of words separated by commas:")
    words = [word.strip() for word in user_input.split(",")]
    print(f"The new list you entered is {words}")
  else:
    print("Great!")

def check_word_existence(word, positions):
    if positions:
        return f"The word '{word}' appears at position/s {positions}."
    else:
        return "The word does not appear"

def find_all_positions_of_exact_word(word, words):
    positions = [i for i, w in enumerate(words) if w == word]
    return check_word_existence(word, positions)
    
    
def find_all_positions_of_word(word, words):
    lower_word = word.lower()
    lowered_words = [w.lower() for w in words]
    positions = [i for i, w in enumerate(lowered_words) if lower_word in w]
    return check_word_existence(word, positions)
  
word_count = Counter(words)



choice = input("Do you want the exact word to be searched? (yes/no): ").strip().lower()
if choice not in ['yes', 'no']:
    print("Invalid choice. Please enter 'yes' or 'no'.")
    exit()


word = input("Enter a word to check if it appears: ").strip()

if choice == 'yes':
  print(find_all_positions_of_exact_word(word, words))
elif choice == 'no':
  print(find_all_positions_of_word(word, words))
else:
  print("Invalid choice. Please enter 'yes' or 'no'.")

  
