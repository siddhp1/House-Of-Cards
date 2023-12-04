import matplotlib.pyplot as plt
import pandas as pd

# Get data from results file
df = pd.read_csv('results.csv')

# Plotting a histogram for the 'Number of winning cards' column with density=True
counts, bins, _ = plt.hist(
    df['Number of winning cards'],
    bins=range(0, df['Number of winning cards'].max() + 2),
    align='left',
    edgecolor='black',
    density=True
)

# Grouping the data by 'Number of winning cards' and then summing the occurrences
winning_cards_count = df.groupby('Number of winning cards').size()

# Add labels to bars
for (i, wc_count) in enumerate(winning_cards_count):
    plt.text(
        bins[i] + 0.01, 
        counts[i],
        f'{counts[i]:.4f} ({wc_count})', # Output percentages to 4 decimal places
        ha='center',
        va='bottom',
        fontsize=6
    )

# Chart labels
plt.xlabel('Number of Winning Cards')
plt.ylabel('Frequency')
plt.title('Frequency of Number of Winning Cards')

# Save the plotted histogram as an image
plt.savefig('histogram.png', dpi=600)

