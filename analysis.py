import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('averaged_data.xlsx')
df = df.set_index(df.columns[0])
df = df.T
print(df.keys())
print(df['Målingnummer'])

measure = 'LAFmax'

df_melted = pd.melt(
    df,
    id_vars=['Sted', 'Før/under VM', 'Målingnummer'],
    value_vars=[f'{measure} mot arena', f'{measure} mot annet område'],
    var_name='Kanal',
    value_name=measure
)
df_melted.dropna(subset=[measure])

df_melted['Tid Kanal'] = (df_melted['Målingnummer'].astype(str) + df_melted['Før/under VM'] + ', ' + df_melted['Kanal'])

df_pivot = df_melted.pivot_table(index='Sted', columns='Tid Kanal', values=measure)

colors = {f'Før VM, {measure} mot arena': 'blue', f'Før VM, {measure} mot annet område': 'lightblue', f'Under VM, {measure} mot arena': 'green', f'Under VM, {measure} mot annet område': 'lightgreen'}

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
