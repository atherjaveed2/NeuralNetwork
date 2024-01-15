#Question 1)A

# Initialization of an empty list to store input characters and an empty string.
char_list = []
res_string = ""

# Keep entering characters untill Enter is clicked.
while True:
    input_char = input("Enter character or press Enter to finsih: ")
    if not input_char:
        break
    char_list.append(input_char)

# Checks whether the length of string is atleast two.
if len(char_list) >= 2:

    # Skips the first two characters and reverses the remaining characters.
    output_list = char_list[2:][::-1]

    # Prints the reversed characters as a string.
    print(res_string.join(output_list))
else:
    print("Enter atleast two characters.")

