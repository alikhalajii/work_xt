"""
Program: process_log_file.py
Description: This program reads a log file and processes the contents to extract and display table data. 
It expects a log file as input and outputs the column names followed by the corresponding table data. 
The table data is sorted based on the first column. Each table is separated by an empty line.

"""
import sys

def process_log_file(file_path):
    column_names = None
    table_lines = []

    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            line = line.strip()

            if line.startswith('AP Name'):
                # Store column names and output them
                column_names = line.split(',')
                print(','.join(column_names))

                # Output the following line
                next_line = next(file).strip()
                print(next_line)

                break  # Stop reading further lines

        # Read the remaining lines until the next empty line and store them in a list
        for line in file:
            line = line.strip()
            if not line:
                if table_lines:
                    # Sort and output the table lines
                    sorted_table_lines = sorted(table_lines, key=lambda x: x.split(',')[0])
                    for sorted_line in sorted_table_lines:
                        print(sorted_line)
                    print()  # Add an empty line between tables

                column_names = None
                table_lines = []  # Clear the table lines list

            elif line.startswith('AP Name'):
                # Store column names and output them
                column_names = line.split(',')
                print(','.join(column_names))

                # Output the following line
                next_line = next(file).strip()
                print(next_line)

            else:
                if column_names is not None:
                    table_lines.append(line)

    # Sort and output the final set of table lines
    if table_lines:
        sorted_table_lines = sorted(table_lines, key=lambda x: x.split(',')[0])
        for sorted_line in sorted_table_lines:
            print(sorted_line)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <log_file_path>")
    else:
        log_file_path = sys.argv[1]
        process_log_file(log_file_path)
