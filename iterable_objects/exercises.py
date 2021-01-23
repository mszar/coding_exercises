# all below exercises are prepared by datacamp team


# exercise 1 

# define the function that create a dictionary from a string where
# each key # represents a unique # character and the value is list 
# containg the indices of this letter

def retrieve_character_indices(string):
    character_indices = dict()
    for index, character in enumerate(string):
        if character in character_indices:
           character_indices[character].append(index)
        if character not in character_indices:
            character_indices[character] = [index]
    return character_indices

print(retrieve_character_indices('eaeaeaebbbb'))