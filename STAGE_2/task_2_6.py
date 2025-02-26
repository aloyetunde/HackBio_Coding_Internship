# -*- coding: utf-8 -*-
"""Task 2.6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lPIoEzAkIW0GVDGgE4Qt4d2Xx5it1coW
"""

"""
Transcriptomics
This is a processed RNAseq dataset involving reading in quantitated gene expression data from an RNA-seq experiment, exploring the data using base Python functions and then interpretation. The dataset contains an experiment between a diseased cell line and diseased cell lines treated with compound X. The difference in expression change between the two health status is computed as Fold change to log 2 (Log2FC) and the significance of each is computed in p-value.

Task:
Generate a volcano plot. (Hint search for volcano plot online)

Determine the upregulated genes (Genes with Log2FC > 1 and pvalue < 0.01)

Determine the downregulated genes (Genes with Log2FC < -1 and pvalue < 0.01)

What are the functions of the top 5 upregulated genes and top 5 downregulated genes. (Use genecards)
"""
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from URL
url = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"
df = pd.read_csv(url, sep= r'\s+') # Reads the data from the URL and splits it into columns based on one or more spaces/tabs.

df.head() #print the first few rows of the dataset

#Get information about the dataset
df.info
df.shape

#Checking the datatype of each column
print(df.dtypes)

# Summary statistics
print(df.describe())

#Checking for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

#Checking for duplicates
num_duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {num_duplicates}")

"""
1. Generate a Volcano Plot visualizing the relationship between log2FoldChange (x-axis) and -log10(pvalue) (y-axis).
"""
# Calculate -log10(pvalue) for the y-axis
df['neg_log10_pvalue'] = -np.log10(df['pvalue'])
df.head(5)

# Create the volcano plot
plt.figure(figsize=(8, 6))  # Set the figure size
plt.scatter(df['log2FoldChange'], df['neg_log10_pvalue'], alpha=0.5)  # Create scatter plot
plt.xlabel('log2 Fold Change')  # Label for x-axis
plt.ylabel('-log10 p-value')  # Label for y-axis
plt.title('Volcano Plot')  # Title of the plot

# Add threshold lines
plt.axvline(x=1, color='red', linestyle='--', linewidth=1)  # Threshold for upregulated genes
plt.axvline(x=-1, color='red', linestyle='--', linewidth=1)  # Threshold for downregulated genes
plt.axhline(y=-np.log10(0.01), color='blue', linestyle='--', linewidth=1)  # Threshold for significance

# Show the plot
plt.show()

#2. Upregulated genes (Genes with Log2FC > 1 and pvalue < 0.01)
upregulated_genes = df[(df['log2FoldChange'] > 1) & (df['pvalue'] < 0.01)]
print("\nUpregulated genes:")
print(upregulated_genes)

# 3. Downregulated genes (Genes with Log2FC < -1 and pvalue < 0.01)
downregulated_genes = df[(df['log2FoldChange'] < -1) & (df['pvalue'] < 0.01)]
print("\nDownregulated genes:")
print(downregulated_genes)

# Top 5 upregulated genes
top5_upregulated = upregulated_genes.nlargest(5, 'log2FoldChange')
print("\nTop 5 upregulated genes:")
print(top5_upregulated[['Gene', 'log2FoldChange', 'pvalue']])
# Corrected nested dictionary to store gene functions
upregulated_gene_functions = {
    'Upreg_gene1': {
        'gene': 'DTHD1',
        'Function': 'Encodes a protein which contains a death domain. Death domain-containing proteins function in signaling pathways and formation of signaling complexes, as well as the apoptosis pathway. Alternative splicing results in multiple transcript variants.',
    },
    'Upreg_gene2': {
        'gene': 'EMILIN2',
        'Function': 'Involved in extracellular matrix organization and angiogenesis. Plays a role in positive regulation of defense response to bacterium and platelet aggregation. Located in the extracellular region.',
    },
    'Upreg_gene3': {
        'gene': 'PI16',
        'Function': 'Encodes a peptidase inhibitor involved in extracellular matrix organization. Predicted to be located in the extracellular region and active in extracellular space.',
    },
    'Upreg_gene4': {
        'gene': 'C4orf45',
        'Function': 'Encodes a protein with currently unknown function. Expressed in various tissues, including the brain and testes.',
    },
    'Upreg_gene5': {
        'gene': 'FAM180B',
        'Function': 'Predicted to be located in the extracellular region. Function is largely unknown.',
    }
}

# Display the functions of top 5 upregulated genes
print("Upregulated Gene Functions:")
print(upregulated_gene_functions)

# Top 5 downregulated genes
top5_downregulated = downregulated_genes.nsmallest(5, 'log2FoldChange')
print("\nTop 5 downregulated genes:")
print(top5_downregulated[['Gene', 'log2FoldChange', 'pvalue']])

# Create a nested dictionary to store gene functions
downregulated_gene_functions = {
    'Downreg_gene1': {
        'gene': 'TNFRSF10B',
        'Function': 'Encodes a member of the TNF-receptor superfamily. This receptor is involved in apoptosis and can activate NF-kappaB and MAPK8/JNK signaling pathways.',
    },
    'Downreg_gene2': {
        'gene': 'CDKN1A',
        'Function': 'Encodes a cyclin-dependent kinase inhibitor that regulates cell cycle progression. It is involved in cell cycle arrest and apoptosis.',
    },
    'Downreg_gene3': {
        'gene': 'GADD45A',
        'Function': 'Encodes a protein involved in DNA repair, cell cycle arrest, and apoptosis. It is induced by stress signals such as DNA damage.',
    },
    'Downreg_gene4': {
        'gene': 'TP53I3',
        'Function': 'Encodes a protein that is induced by TP53 and involved in oxidative stress response and apoptosis.',
    },
    'Downreg_gene5': {
        'gene': 'FAS',
        'Function': 'Encodes a cell surface receptor that mediates apoptosis when bound to its ligand. It is involved in immune system regulation.',
    }
}

# Display the functions of top 5 downregulated genes
print("Downregulated Gene Functions:")
print(downregulated_gene_functions)

"""
Results & Findings
Functions of top 10 Differntially Expressed Genes

o The functions of the top upregulated genes suggests that compound X may induce significant changes in the cellular environment, particularly affecting apoptosis and Extracellular Matrix organization.
o These alterations could either promote a beneficial reprogramming of diseased cells towards a more normal state or modulate the tissue microenvironment to better support repair and defense mechanisms.
o The changes in gene expression might therefore be part of the treatment's mechanism of action. o Compound X might be beneficial in reducing apostosis (which is commonly found in neurogenerative and inflammatory conditions) as genes that mediate cell apostosis were downregulated.

#GitHub Link:
#LinkedIn Link: https://www.linkedin.com/posts/omojuwa-iyinoluwa-5a0249242_bioinformatics-phyton-hackbio-activity-7300504327775768577-uu6-?utm_source=social_share_send&utm_medium=android_app&rcm=ACoAADwxPAgBbnOT4_7yhFfQOdqRfEafIUZwkc4&utm_campaign=whatsapp