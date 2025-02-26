# 🚀 HackBio_Coding_Internship - #Team Leucine - Stage 2

### 📌 Task Code 2.1: Microbiology

• Given this dataset [dataset](https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv).

• Plot all the growth curves of OD600 vs Time for the different Strains with the following instructions.

• For each strain, plot a growth curve of the the knock out (-) an knock in (+) strain overlaid on top of each other.

• Using your function from last stage, determine the time to reach the carrying capacity for each strain/mutant.

• Generate a scatter plot of the time it takes to reach carrying capacity for the knock out and the knock in strains.

• Generate a box plot of the time it takes to reach carrying capacity for the knock out and the knock in strains.

• Is there a statistical difference in the time it takes the knock out strains to reach their maximum carrying capacity compared to the knock in strains. 

• What do you see? Explain your observations as comments in your code.

### ✅Task Implementation


### 📌 Task Code 2.3: Botany and Plant Science

Have a look at this dataset
Some scientists are trying to engineer mutants for a crop to become resistant to a pesticide
They compared the metabolic response of the engineered mutants to the metabolic response of the wild type plants
The took readings after 8 and 24 hours
Your task
Calculate the difference in metabolic response (ΔM) between the DMSO treatment from the 24 hours treatment for the wild type and mutants
Generate a scatter plot showing the difference for ΔM for WT and Mutants
Fit a line that satifies a y-intercept of 0 and a slope of 1.
Using a residual cut off of your choice (calculated a the difference between the fitted line and each point) calculate the residual of each point on the scatter plot
Color metabolites that fall within +/- n of your residual grey. For example, if you have a cut-off of 0.3, color residual values that are within -0.3 and +0.3 grey
Color metabolites that fall outside this range salmon.
What are these metabolites. How do you explain the trends you see on either direction of the plot?
Pick any 6 metabolites that fall outside this range and generate a line plot that spans from their 0h treatment to their 8h and 24hr.
What can you say about the plots you see?

### ✅Task Implementation

The code analyzes metabolic changes in wild-type (WT) and mutant plants exposed to a pesticide by calculating the difference in metabolic response (AM) between pesticide treatment and the DMSO control after 24 hours. It generates a scatter plot comparing AM_WT vs. AM_Mutant, highlighting metabolites that behave differently in mutants (outliers) using color coding (grey = similar response, salmon = significantly different response). Finally, it selects six key metabolites with the most significant differences and plots their time-series trends (Oh → 8h → 24h) to visualize how pesticide resistance alters metabolism over time. These visual outputs help identify potential biomarkers and metabolic pathways involved in pesticide resistance

### 📌 Task Code 2.4: Biochemistry & Oncology

This project analyzes the impact of non-synonymous mutations on protein structure and function. We use SIFT scores to measure functional effects and FoldX scores to assess structural stability.
Dataset Description
We worked with two datasets:
•	SIFT Dataset: Contains protein IDs, mutations, and SIFT scores.
•	FoldX Dataset: Contains protein IDs, mutations, and FoldX scores (kCal/mol).

#### Objectives

1.	Merge datasets: Create a unique identifier (specific_Protein_aa) for each mutation.
   
2.	Filter deleterious mutations:
o	SIFT Score < 0.05 (Functionally damaging)
o	FoldX Score > 2 (Structurally destabilizing)

3.	Analyze amino acid impact: Identify the most affected amino acids and visualize mutation frequency.
   
#### Project Workflow

1.	Data Preprocessing
o	Load and clean the SIFT and FoldX datasets.
o	Create a new column (specific_Protein_aa) by concatenating Protein ID and Mutation.
o	Merge datasets based on this column.

2.	Deleterious Mutation Identification
o	Filter mutations where SIFT < 0.05 and FoldX > 2.

3.	Amino Acid Frequency Analysis
o	Extract the first amino acid from each mutation.
o	Count occurrences and visualize the distribution using bar plots and pie charts.

#### Results & Findings

•	Most impacted amino acid: Glycine (G) had the highest mutation frequency.
•	Structural & Functional Significance:
o	Amino acids with over 100 mutations play key roles in protein stability.
o	Their mutations can severely disrupt protein folding and function, which may lead to diseases.

### 📌 Task Code 2.6: Transcriptomics

This is a processed RNAseq dataset involving reading in quantitated gene expression data from an RNA-seq experiment, exploring the data using base R functions and then interpretation. The dataset contains an experiment between a diseased cell line and diseased cell lines treated with compound X. The difference in expression change between the two health status is computed as Fold change to log 2 (Log2FC) and the significance of each is computed in p-value.
Access Dataset Here
Task:
Generate a volcano plot. (Hint search for volcano plot online)
Determine the upregulated genes (Genes with Log2FC > 1 and pvalue < 0.01)
Determine the downregulated genes (Genes with Log2FC < -1 and pvalue < 0.01)
What are the functions of the top 5 upregulated genes and top 5 downregulated genes. (Use genecards


Write a function for translating DNA to protein 🧬

📚Key Python concepts we used:


✅Task Implementation

🧬 


📈

📊 T

🔢 
Here's the link to the folder containing our scripts, https://github.com/aloyetunde/HackBio_Coding_Internship/blob/main/STAGE%201/All_codes , feel free to run the codes to replicate what we've done!😊
