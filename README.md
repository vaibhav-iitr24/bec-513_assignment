# bec-513_assignment
For each question respective folder created and respective data placed in those respective folders. Commands are executed in respective folder.

__Question 1]__  We have two input files. From one file(q1_data.tsv.gz) we pulled lines contain expected pattern and forwaded to script file(sorting.py) as a input. In sorting.py we extracting those line which contain pattern which is present in to_select.tsv file.
Command used for execution: zless q1_data.tsv.gz | awk 'NR==1||/ENSG/' | python sorting.py data/to_select.tsv final_filtered.tsv

__Question 2]__ We have data file q2_data.tsv and have to generate line plot based on catogories. Using ggplot library plot generted using R scripting. Command line argument used to lable x axis, y axis, name graph title & output file. Command used for execution: cat q2_data.tsv | Rscript lineplot.R "different_clusters.png" "Relative from center [bp]" "Enrichment over Mean" "MNase fragment profile".

__Question 3]__ Here actually we have two files(q3_first.tsv & q3_second.tsv) listed in another file list_q3.tsv  contain different data but one similar key. Rscript contain code which joining the data based on that common key and generate output file join_output.tsv. Command used for execution: Rscript join_list_of_files.R list_q3.tsv  join_output.tsv

__Question 4]__ In this task we divided a numeric dataset into quantiles, labeling each data point according to its quantile group. Python script(group_in_quantiles.py) is executed on data file to achieve the output. Command used for execution:cat first_hundred_numbers.tsv | python group_in_quantiles.py 4

__Question 5]__ Here we have to generate heatmap of big file(not uploaded here because of size issue). First we removed first column from big file and stored in a file-new_data.tsv(not uploaded here because of size issue). Using heatmap.py heatmap achieved. 

Commands used for execution: zcat big_data.tsv.gz | cut --complement -f1 > new_data.tsv

python3 heatmap.py
