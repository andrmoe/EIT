import pandas as pd
import matplotlib.pyplot as plt
from plot import grouped_bar_chart


df = pd.read_excel('averaged_data.xlsx')
df = df.set_index(df.columns[0])
df = df.T

measure = 'LAeq'

df_melted = pd.melt(
    df,
    id_vars=['Sted', 'Før/under VM', 'Målingnummer'],
    value_vars=[f'{measure} nærmest arena', f'{measure} lengst unna arena'],
    var_name='Kanal',
    value_name=measure
)
df_melted.dropna(subset=[measure])

df_melted['Tid Kanal'] = (df_melted['Målingnummer'].astype(str) + df_melted['Før/under VM'] + ', ' + df_melted['Kanal'])

df_pivot = df_melted.pivot_table(index='Sted', columns='Tid Kanal', values=measure)
df_pivot = df_pivot[['1Før VM, LAeq nærmest arena',
                     '1Før VM, LAeq lengst unna arena',
                     '2Før VM, LAeq lengst unna arena',
                     '1Under VM, LAeq nærmest arena',
                     '1Under VM, LAeq lengst unna arena',
                     '2Under VM, LAeq nærmest arena',
                     '2Under VM, LAeq lengst unna arena']]
colors = {f'Før VM, {measure} nærmest arena': 'lightblue', f'Før VM, {measure} lengst unna arena': 'blue', f'Under VM, {measure} nærmest arena': 'lightgreen', f'Under VM, {measure} lengst unna arena': 'green'}

# Plotting the grouped bar chart
ax = df_pivot.plot(kind='bar', figsize=(10, 6),
                   color=[
                       colors[col[1:]]
                       for col in df_pivot.columns]
                    )


legend_labels = [col[1:].replace(f'{measure} ', '') for col in df_pivot.columns]

# Customize the plot
ax.set_title(f'{measure} for alle målinger')
ax.set_xlabel('Sted')
ax.set_ylabel(measure)
ax.legend(handles=ax.containers,
          labels=legend_labels,
          loc='upper center',
          bbox_to_anchor=(0.5, -0.15),
          ncols=3,
          fontsize='small')
plt.xticks(rotation=0)  # Keep x-axis labels horizontal
plt.tight_layout()
plt.savefig(f'{measure}.svg', format='svg', bbox_inches='tight')
# Show the plot
plt.show()
