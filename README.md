# bec-513_assignment
For each question respective folder created and respective data placed in those respective folders. Commands are executed in respective folder.

__Question 1]__  We have two input files. From one file(q1_data.tsv.gz) we pulled lines contain expected pattern and forwaded to script file(sorting.py) as a input. In sorting.py we extracting those line which contain pattern which is present in to_select.tsv file.
Command used for execution: zless q1_data.tsv.gz | awk 'NR==1||/ENSG/' | python sorting.py data/to_select.tsv final_filtered.tsv

__Question 2]__ We have data file q2_data.tsv and have to generate line plot based on catogories. Using ggplot library plot generted using R scripting. Command line argument used to lable x axis, y axis, name graph title. 
