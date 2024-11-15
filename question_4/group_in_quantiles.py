import pandas as pd
import sys

#Read the number of quantiles from the command line
num_quantiles = int(sys.argv[1])

#Read the list of numbers from stdin
numbers = [float(line.strip()) for line in sys.stdin]

#Create a DataFrame from the numbers
df = pd.DataFrame(numbers, columns=["Value"])

#Calculate quantiles and assign labels
df["Quantile_Label"], bins = pd.qcut(df["Value"], q=num_quantiles, labels=[f"q{i+1}" for i in range(num_quantiles)], retbins=True)
df["Quantile_Interval"] = pd.cut(df["Value"], bins=bins)

# Print each value with its quantile label and interval
for _, row in df.iterrows():
    print(f"{row['Value']}\t{row['Quantile_Label']}\t{row['Quantile_Label']} {row['Quantile_Interval']}")

