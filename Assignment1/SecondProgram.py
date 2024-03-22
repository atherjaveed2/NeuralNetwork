# Get input sentence from the user.
input_str = input("Please enter the sentence: ") 

# Split method is used to convert the input sentence into array of strings
array_of_strings = input_str.split()

# Initialization of empty string.
output_str = ""  

# For loop is used to iterate over the array of strings
for i in range(0,len(array_of_strings)):  
     # To check if the word `python` is or not.
    if(array_of_strings[i]=="python"):    
        # To replace `python` with `pythons`.
        array_of_strings[i]="pythons"   

     # Append the current word to the output string.
    output_str += array_of_strings[i]+" " 
# Print the resultant output.
print(output_str)