import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit
from scipy import stats

# Load the dataset
url = "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
df = pd.read_csv(url, sep="\t")

# Ensure 'time' column is numeric
df['time'] = pd.to_numeric(df['time'], errors='coerce')

# Reshape data for plotting
df_melt = df.melt(id_vars=['time'], var_name='Sample', value_name='OD600')

# Define sample classification (Knock-out "-" and Knock-in "+")
sample_mapping = {
    "A1": ("Strain1", "-"), "A2": ("Strain1", "+"), "B1": ("Strain1", "-"), "B2": ("Strain1", "+"), "C1": ("Strain1", "-"), "C2": ("Strain1", "+"),
    "A3": ("Strain1", "-"), "A4": ("Strain1", "+"), "B3": ("Strain1", "-"), "B4": ("Strain1", "+"), "C3": ("Strain1", "-"), "C4": ("Strain1", "+"),
    "A5": ("Strain2", "-"), "A6": ("Strain2", "+"), "B5": ("Strain2", "-"), "B6": ("Strain2", "+"), "C5": ("Strain2", "-"), "C6": ("Strain2", "+"),
    "A7": ("Strain2", "-"), "A8": ("Strain2", "+"), "B7": ("Strain2", "-"), "B8": ("Strain2", "+"), "C7": ("Strain2", "-"), "C8": ("Strain2", "+"),
    "A9": ("Strain3", "-"), "A10": ("Strain3", "+"), "B9": ("Strain3", "-"), "B10": ("Strain3", "+"), "C9": ("Strain3", "-"), "C10": ("Strain3", "+"),
    "A11": ("Strain2", "-"), "A12": ("Strain2", "+"), "B11": ("Strain2", "-"), "B12": ("Strain2", "+"), "C11": ("Strain2", "-"), "C12": ("Strain2", "+"),
}

# Map strain and type (Knock-out/Knock-in)
df_melt['Strain'] = df_melt['Sample'].map(lambda x: sample_mapping.get(x, (None, None))[0])
df_melt['Type'] = df_melt['Sample'].map(lambda x: sample_mapping.get(x, (None, None))[1])
df_melt.dropna(subset=['Strain', 'Type'], inplace=True) # Remove missing values

# Remove negative or extreme OD600 values
df_melt = df_melt[df_melt['OD600'] >= 0]

# Logistic growth function
def logistic_growth(t, K, r, t0):
    return K / (1 + np.exp(-r * (t - t0)))

# Function to fit logistic model and calculate carrying capacity time
def fit_logistic_and_find_capacity(df, strain_col, time_col, od_col):
    capacity_times = {}
    strains = df[strain_col].unique()
    
    for strain in strains:
        subset = df[df[strain_col] == strain]
        
        for stype in subset['Type'].unique():
            strain_subset = subset[subset['Type'] == stype]
            time_values = strain_subset[time_col].values
            od_values = strain_subset[od_col].values
            
            # Skip if insufficient data points
            if len(time_values) < 5:
                capacity_times[f'{strain}_{stype}'] = np.nan
                continue
            
            # Fit logistic model
            try:
                popt, _ = curve_fit(logistic_growth, time_values, od_values, maxfev=10000)
                K, r, t0 = popt
                
                # Calculate time when OD600 reaches 95% of K (carrying capacity time)
                target_OD = 0.95 * K
                capacity_time = (np.log((K / target_OD) - 1) / -r) + t0
                capacity_times[f'{strain}_{stype}'] = capacity_time
            except RuntimeError:
                capacity_times[f'{strain}_{stype}'] = np.nan
    
    return capacity_times

# Fit logistic model and determine carrying capacity times
capacity_times = fit_logistic_and_find_capacity(df_melt, 'Strain', 'time', 'OD600')

# Convert carrying capacity times into DataFrame
capacity_df = pd.DataFrame(list(capacity_times.items()), columns=['Strain_Type', 'Capacity_Time'])
capacity_df[['Strain', 'Type']] = capacity_df['Strain_Type'].str.split('_', expand=True)

# Improved Growth Curves Plotting
def plot_growth_curves(df, strain_col, time_col, od_col):
    strains = df[strain_col].unique()
    fig, axes = plt.subplots(len(strains), 1, figsize=(10, 6 * len(strains)))
    
    for i, strain in enumerate(strains):
        subset = df[df[strain_col] == strain]
        sns.lineplot(data=subset, x=time_col, y=od_col, hue='Type', marker='o', ax=axes[i])
        axes[i].set_title(f'Growth Curve for {strain}')
        axes[i].set_xlabel('Time')
        axes[i].set_ylabel('OD600')
        axes[i].legend(title='Type')

    plt.tight_layout()
    plt.show()

# Plot growth curves
plot_growth_curves(df_melt, 'Strain', 'time', 'OD600')

# Scatter plot of carrying capacity times
plt.figure(figsize=(10, 6))
sns.scatterplot(data=capacity_df, x='Strain', y='Capacity_Time', hue='Type', style='Type', s=100)
plt.title('Carrying Capacity Times for Knock Out (-) and Knock In (+) Strains')
plt.xlabel('Strain')
plt.ylabel('Time to Carrying Capacity')
plt.show()

# Box plot of carrying capacity times
plt.figure(figsize=(10, 6))
sns.boxplot(data=capacity_df, x='Type', y='Capacity_Time', palette='Set2')
plt.title('Box Plot of Carrying Capacity Times for Knock Out (-) and Knock In (+) Strains')
plt.xlabel('Type')
plt.ylabel('Time to Carrying Capacity')
plt.show()

# Statistical test: Knock-out (-) vs. Knock-in (+)
knock_out_times = capacity_df[capacity_df['Type'] == '-']['Capacity_Time'].dropna()
knock_in_times = capacity_df[capacity_df['Type'] == '+']['Capacity_Time'].dropna()

if len(knock_out_times) > 1 and len(knock_in_times) > 1:
    t_stat, p_val = stats.ttest_ind(knock_out_times, knock_in_times)
    print(f'T-test results: t-statistic = {t_stat}, p-value = {p_val}')
    if p_val < 0.05:
        print('Statistically significant difference in carrying capacity time between Knock-out (-) and Knock-in (+).')
    else:
        print('No statistically significant difference in carrying capacity time.')
else:
    print("Not enough data for statistical test.")

