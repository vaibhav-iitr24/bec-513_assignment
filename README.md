# bec-513_assignment
For each question respective folder created and respective data placed in those respective folders. Commands are executed in respective folder.

__Q-1]__  We have two input files. From one file(q1_data.tsv.gz) we pulled lines contain expected pattern and forwaded to script file(sorting.py) as a input. In sorting.py we extracting those line which contain pattern which is present in to_select.tsv file.
Command used for execution: zless q1_data.tsv.gz | awk 'NR==1||/ENSG/' | python sorting.py data/to_select.tsv final_filtered.tsv
Using zless to view the compressed TSV file (q1_data.tsv.gz).
Using awk to filter the file for rows where the first line (NR==1) is included, and also any lines containing the string ENSG.
Passing the filtered output to the Python script (sorting.py) for further processing.
