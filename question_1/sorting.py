import pandas as pd
import sys

required_file = sys.argv[1]  # to_select.tsv file contain required pattern, accessed by command line argument
filtered_file = sys.argv[2]  # generate output file for selected lines

# Load the pattern to match from the requirerd file
selection_df = pd.read_csv(required_file, names=['Column'])
pattern = set(selection_df['Column'])  # Set of specific pattern to select

#Open the output file and write lines that match pattern in search_terms
with open(filtered_file, 'w') as output:
    for line in sys.stdin:
        if any(term in line for term in pattern):
            output.write(line)

