Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def read_and_modify_file(input_filename, output_filename):
...     try:
...         #  Open and read the input file
...         with open(input_filename, 'r') as file:
...             content = file.read()
... 
...         #  Modify the content ( convert to uppercase)
...         modified_content = content.upper()
... 
...         # Write the modified content to a new file
...         with open(output_filename, 'w') as file:
...             file.write(modified_content)
... 
...         print(f"File '{input_filename}' has been modified and saved as '{output_filename}'.")
... 
...     except FileNotFoundError:
...         print(f"Error: The file '{input_filename}' does not exist.")
...     except PermissionError:
...         print(f"Error: You do not have permission to read the file '{input_filename}'.")
...     except Exception as e:
...         print(f"An unexpected error occurred: {e}")
... 
... def main():
...     # Ask the user for the input filename
...     input_filename = input("Enter the filename to read: ")
...     
...     # Ask the user for the output filename
...     output_filename = input("Enter the filename to save the modified content: ")
...     
...     # Call the function to read, modify, and write the file
...     read_and_modify_file(input_filename, output_filename)
... 
... if __name__ == "__main__":
