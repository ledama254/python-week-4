# complete_file_handler.py

def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
            modified = content.upper()  # You can change this to any transformation

        with open(output_file, 'w') as outfile:
            outfile.write(modified)

        print(f"\n✅ Success: Modified content written to '{output_file}'.")

    except FileNotFoundError:
        print(f"❌ Error: '{input_file}' not found.")
    except IOError:
        print("❌ Error: Failed to read or write files.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def main():
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")
    modify_file(input_file, output_file)

if __name__ == "__main__":
    main()
