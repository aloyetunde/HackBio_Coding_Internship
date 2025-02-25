# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns



# Load dataset from URL
dataset_url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt"
df = pd.read_csv(dataset_url, sep='\t')

# Rename the first column to 'Sample'
df.rename(columns={'Unnamed: 0': 'Sample'}, inplace=True)

# Extract metadata from 'Sample' column
df['Plant_Type'] = df['Sample'].apply(lambda x: 'WT' if 'WT' in x else 'Mutant')
df['Treatment'] = df['Sample'].apply(lambda x: 'DMSO' if 'DMSO' in x else 'Pesticide')
df['Time_Point'] = df['Sample'].apply(lambda x: '0h' if '_0_' in x else ('8h' if '8h' in x else '24h'))

# Compute ΔM (Metabolic Response Difference) for WT and Mutant
deltaM_df = pd.DataFrame({
    "Metabolite": df.columns[1:-3],  # Extract metabolite names
    "ΔM_WT": (df[df["Time_Point"] == "24h"][df["Plant_Type"] == "WT"].iloc[:, 1:-3].mean()
               - df[df["Treatment"] == "DMSO"][df["Plant_Type"] == "WT"].iloc[:, 1:-3].mean()),
    "ΔM_Mutant": (df[df["Time_Point"] == "24h"][df["Plant_Type"] == "Mutant"].iloc[:, 1:-3].mean()
                  - df[df["Treatment"] == "DMSO"][df["Plant_Type"] == "Mutant"].iloc[:, 1:-3].mean())
})

# Scatter plot of ΔM_WT vs. ΔM_Mutant
plt.figure(figsize=(10, 6))
plt.scatter(deltaM_df['ΔM_WT'], deltaM_df['ΔM_Mutant'], label='Metabolites')

# Plot y=x reference line
x = np.linspace(deltaM_df['ΔM_WT'].min(), deltaM_df['ΔM_WT'].max(), 100)
plt.plot(x, x, color='red', linestyle='--', label='y = x')

# Calculate residuals
deltaM_df['Residual'] = deltaM_df['ΔM_Mutant'] - deltaM_df['ΔM_WT']

# Define residual cutoff
residual_cutoff = 0.3

# Identify significant outliers
outliers = deltaM_df[abs(deltaM_df['Residual']) > residual_cutoff]
print("Metabolites outside the residual cutoff:")
print(outliers[['Metabolite', 'Residual']])

# Color points based on residuals
colors = ['salmon' if abs(res) > residual_cutoff else 'grey' for res in deltaM_df['Residual']]
plt.scatter(deltaM_df['ΔM_WT'], deltaM_df['ΔM_Mutant'], c=colors)

# Labels and title
plt.xlabel('ΔM WT')
plt.ylabel('ΔM Mutant')
plt.title('Scatter Plot of ΔM: WT vs. Mutant')
plt.legend()
plt.grid(True)
plt.show()

# Select 6 key outliers for time-series analysis
selected_metabolites = outliers.head(6)['Metabolite'].tolist()

# Time-series line plot for selected metabolites
plt.figure(figsize=(10, 6))

time_order = ['0h', '8h', '24h']  # Corrected time sequence

for metabolite in selected_metabolites:
    if metabolite in df.columns:
        wt_values = df[df["Plant_Type"] == "WT"].groupby("Time_Point")[metabolite].mean().reindex(time_order)
        mutant_values = df[df["Plant_Type"] == "Mutant"].groupby("Time_Point")[metabolite].mean().reindex(time_order)

        # Plot WT and Mutant trends
        plt.plot(time_order, wt_values.values, marker='o', linestyle='-', label=f'WT - {metabolite}')
        plt.plot(time_order, mutant_values.values, marker='s', linestyle='--', label=f'Mutant - {metabolite}')

# Formatting the plot
plt.xlabel('Time (h)')
plt.ylabel('Metabolic Response')
plt.title('Metabolic Response Over Time for Selected Metabolites')
plt.legend()
plt.grid(True)
plt.show()

#Residual Distribution Histogram

plt.figure(figsize=(8,5))
sns.histplot(deltaM_df['Residual'], bins=20, kde=True, color='steelblue', edgecolor='black')
plt.axvline(0, color='red', linestyle='--', label='Zero Residual')
plt.xlabel('Residual (ΔM_Mutant - ΔM_WT)')
plt.ylabel('Frequency')
plt.title('Residual Distribution')
plt.legend()
plt.show()


#volcano plots
from scipy.stats import ttest_ind

# Compute p-values (t-test comparing WT and Mutant ΔM values)
p_values = [ttest_ind(df[df['Plant_Type'] == 'WT'][metabolite], 
                       df[df['Plant_Type'] == 'Mutant'][metabolite], 
                       nan_policy='omit')[1] for metabolite in deltaM_df['Metabolite']]

# Add to dataframe
deltaM_df['p-value'] = p_values
deltaM_df['-log10(p)'] = -np.log10(deltaM_df['p-value'])

# Scatter plot (volcano)
plt.figure(figsize=(8,6))
sns.scatterplot(x=deltaM_df['Residual'], y=deltaM_df['-log10(p)'], color='grey')

# Highlight significant outliers
significant = deltaM_df[abs(deltaM_df['Residual']) > residual_cutoff]
sns.scatterplot(x=significant['Residual'], y=significant['-log10(p)'], color='salmon')

plt.axvline(x=-residual_cutoff, color='black', linestyle='--')
plt.axvline(x=residual_cutoff, color='black', linestyle='--')
plt.xlabel('Residual (ΔM_Mutant - ΔM_WT)')
plt.ylabel('-log10(p-value)')
plt.title('Volcano Plot: Residual vs. Significance')
plt.show()


#Boxplot
plt.figure(figsize=(12, 6))
for i, metabolite in enumerate(selected_metabolites):
    plt.subplot(2, 3, i + 1)
    sns.boxplot(x='Time_Point', y=metabolite, hue='Plant_Type', data=df)
    plt.title(metabolite)
plt.tight_layout()
plt.show()


#heatmap


# Select only metabolite columns (excluding metadata)
metabolite_data = df.set_index("Sample").iloc[:, :-3]  # Exclude metadata columns

# Normalize data (z-score)
normalized_data = (metabolite_data - metabolite_data.mean()) / metabolite_data.std()

# Create metadata for annotations (WT vs. Mutant, Time Points)
row_metadata = df.set_index("Sample")[['Plant_Type', 'Time_Point']]

# Convert categorical metadata to numerical categories for visualization
row_metadata['Plant_Type'] = row_metadata['Plant_Type'].map({'WT': 0, 'Mutant': 1})
row_metadata['Time_Point'] = row_metadata['Time_Point'].map({'0h': 0, '8h': 1, '24h': 2})

# Define color palettes for annotations
plant_colors = {0: "blue", 1: "green"}   # WT = blue, Mutant = green
time_colors = {0: "black", 1: "orange", 2: "red"}  # 0h = black, 8h = orange, 24h = red

# Convert metadata to color labels
row_colors = pd.DataFrame({
    "Plant_Type": row_metadata["Plant_Type"].map(plant_colors),
    "Time_Point": row_metadata["Time_Point"].map(time_colors)
}, index=row_metadata.index)

# Create the heatmap with hierarchical clustering
sns.clustermap(
    normalized_data.T,  # Transpose to get metabolites as rows
    cmap="coolwarm", 
    linewidths=0.5, 
    center=0, 
    row_cluster=True,  # Cluster metabolites
    col_cluster=True,  # Cluster samples
    col_colors=row_colors,  # Add sample annotations
    figsize=(12, 10)
)

plt.title("Hierarchical Clustering Heatmap of Metabolic Response")
plt.show()
