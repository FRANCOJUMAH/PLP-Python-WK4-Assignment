def file_read_write():
    try:
        # Ask the user for the input filename
        input_file = input("Enter the name of the file to read from: ")

        # Attempt to open the file for reading
        with open(input_file, 'r') as file:
            content = file.read()

        # Modify the content (for example, convert it to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
            file.write(modified_content)

        print(f"Modified content has been written to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
file_read_write()