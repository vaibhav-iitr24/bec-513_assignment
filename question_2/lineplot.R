# Load necessary libraries
library(ggplot2)

# Capture command-line arguments
args <- commandArgs(trailingOnly = TRUE)

# Assign arguments to variables
output_file <- args[1]               # e.g., "different_clusters.png"
x_label <- args[2]                   # e.g., "Relative from center [bp]"
y_label <- args[3]                   # e.g., "Enrichment over Mean"
plot_title <- args[4]                # e.g., "MNase fragment profile"

# Load data (replace "data.txt" with your actual data file)
data <- read.table("q2_data.tsv", header = FALSE, col.names = c("X", "Y", "Category"))

# Plot using ggplot2 with dark theme
plot <- ggplot(data, aes(x = X, y = Y, color = Category, group = Category)) +
  geom_line(size = 1) +               # Set line size for better visibility
  labs(title = plot_title,            # Use plot title from command-line argument
       x = x_label,                   # Use x-axis label from command-line argument
       y = y_label) +                 # Use y-axis label from command-line argument
  theme_bw()

# Save the plot to file
ggsave(output_file, plot = plot, width = 8, height = 6)

