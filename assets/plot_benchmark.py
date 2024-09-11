import pandas as pd
import matplotlib.pyplot as plt

import matplotlib

matplotlib.rc('font', size=16)

df = pd.read_csv("benchmark_dense_mnist.csv")

# Sort the dataframe by Elapsed time in ascending order
df_sorted = df.sort_values('Elapsed')

# Create the bar plot
plt.figure(figsize=(12, 6))
bars = plt.bar(df_sorted['Compiler'], df_sorted['Elapsed'])

# Customize the plot
plt.title('Time to train a dense MNIST model on Intel Core Ultra 7 155H')
plt.ylabel('Elapsed Time (seconds)')
plt.xticks(rotation=30, ha='right')
plt.grid()
plt.tight_layout()
plt.ylim(0, 12)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom')

plt.savefig("benchmark_dense_mnist.png", dpi=200)
plt.close()
