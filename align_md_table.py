import sys

def align_markdown_table(input_table):
    # Split the input into lines
    lines = input_table.strip().split('\n')

    # Check if there is at least the header and one row
    if len(lines) < 2:
        return "Invalid table format. A table should have at least a header and one row."

    # Split each line into columns and trim whitespace
    table = [line.split('|')[1:-1] for line in lines]
    table = [[col.strip() for col in row] for row in table]

    # Calculate the maximum width of each column
    max_widths = [max(len(col) for col in column) for column in zip(*table)]

    # Create a format string for each row
    row_format = '| ' + ' | '.join(['{:<%d}' % width for width in max_widths]) + ' |'

    # Use the format string to align the columns
    aligned_table = [row_format.format(*row) for row in table]

    # Return the aligned table as a single string
    return '\n'.join(aligned_table)

# Read input from stdin (pipe)
input_table = sys.stdin.read()

# Process the input table
aligned_table = align_markdown_table(input_table)

# Output the aligned table to stdout
print(aligned_table)

