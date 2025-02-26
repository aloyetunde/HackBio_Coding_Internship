
# 🚀 HackBio_Coding_Internship - #Team Leucine - Stage 2

## Exploring Microbiology, Plant Science, Biochemistry & Transcriptomics Through Bioinformatics using Python! 😉😎💃

✅ Microbiology 🦠: Analyzed bacterial growth curves, compared knockout vs. knock-in strains, and assessed statistical significance in carrying capacity.

✅ Plant Science 🌱🌾: Investigated metabolic responses in genetically engineered crops to pesticide resistance, identifying key metabolites driving differences.

✅ Biochemistry & Oncology 🏥: Mapped protein mutations using SIFT and FoldX scores, identifying amino acids with the highest impact on structure and function.

✅ Transcriptomics 🧬: Generated volcano plots to detect differentially expressed genes, uncovering key upregulated and downregulated genes in a diseased cell line.

Below are more details on each task:

### 📌 Task Code 2.1: Microbiology

• Given this dataset [dataset](https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv).

• Plot all the growth curves of OD600 vs Time for the different Strains with the following instructions.

• For each strain, plot a growth curve of the the knock out (-) an knock in (+) strain overlaid on top of each other.

• Using your function from last stage, determine the time to reach the carrying capacity for each strain/mutant.

• Generate a scatter plot of the time it takes to reach carrying capacity for the knock out and the knock in strains.

• Generate a box plot of the time it takes to reach carrying capacity for the knock out and the knock in strains.

• Is there a statistical difference in the time it takes the knock out strains to reach their maximum carrying capacity compared to the knock in strains. What do you see? Explain your observations as comments in your code.

##### ✅Task Implementation
This project investigates metabolic differences between wild-type (WT) and mutant strains, focusing on metabolic activity and growth patterns. It examines whether knock-out and knock-in strains reach their maximum carrying capacity at different rates. We analyzed metabolic response data across multiple strains and time points.  

#### Objectives  
1. Compute ΔM (Metabolic Response Difference) between WT and mutant strains.  
2. Visualize metabolic trends using scatter plots and residual analysis.  
3. Identify outlier metabolites with significant deviations.  
4. Compare knock-out vs. knock-in strains to assess growth rate differences.  

#### Project Workflow  
1. Data Processing: Extract metabolic response values, compute means, and analyze residuals.  
2. Metabolic Response Analysis: Generate scatter plots and highlight metabolic shifts.  
3. Outlier Identification: Detect and visualize extreme metabolic deviations.  
4. Knock-out vs. Knock-in Comparison: Evaluate statistical differences in time to maximum capacity.  

#### Results & Findings  
- Some mutants exhibit significant metabolic shifts.  
- Knock-out vs. Knock-in Growth Differences:
  - Slower knock-out growth suggests metabolic impairment.  
  - Slower knock-in growth may indicate an added metabolic burden.  
  - Statistical tests confirm significance.  

This study helps understand metabolic adaptations in genetically modified strains.


### 📌 Task Code 2.3: Botany and Plant Science

[Dataset](https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/Pesticide_treatment_data.txt)
Some scientists are trying to engineer mutants for a crop to become resistant to a pesticide. They compared the metabolic response of the engineered mutants to the metabolic response of the wild type plants. Then took readings after 8 and 24 hours

Questions:

• Calculate the difference in metabolic response (ΔM) between the DMSO treatment from the 24 hours treatment for the wild type and mutants.

• Generate a scatter plot showing the difference for ΔM for WT and Mutants📊.

• Fit a line that satifies a y-intercept of 0 and a slope of 1.

• Using a residual cut off of your choice (calculated a the difference between the fitted line and each point) calculate the residual of each point on the scatter plot.

• Color metabolites that fall within +/- n of your residual grey. For example, if you have a cut-off of 0.3, color residual values that are within -0.3 and +0.3 grey.

• Color metabolites that fall outside this range salmon. What are these metabolites. How do you explain the trends you see on either direction of the plot?

• Pick any 6 metabolites that fall outside this range and generate a line plot that spans from their 0h treatment to their 8h and 24hr.

##### ✅Task Implementation
- The code analyzes metabolic changes in wild-type (WT) and mutant plants exposed to a pesticide by calculating the difference in metabolic response (AM) between pesticide treatment and the DMSO control after 24 hours. It generates a scatter plot comparing AM_WT vs. AM_Mutant, highlighting metabolites that behave differently in mutants (outliers) using color coding (grey = similar response, salmon = significantly different response). 
- Finally, it selects six key metabolites with the most significant differences and plots their time-series trends (Oh → 8h → 24h) to visualize how pesticide resistance alters metabolism over time.
- These visual outputs help identify potential biomarkers and metabolic pathways involved in pesticide resistance

### 📌 Task Code 2.4: Biochemistry & Oncology

This project analyzes the impact of non-synonymous mutations on protein structure and function. We use SIFT scores to measure functional effects and FoldX scores to assess structural stability.

#### Dataset Description:

•	[SIFT Dataset](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv): Contains protein IDs, mutations, and SIFT scores.
•	[FoldX Dataset](https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv): Contains protein IDs, mutations, and FoldX scores (kCal/mol).

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

### 📌 Task Code 2.6: Transcriptomics🧬

This is a processed RNAseq dataset involving reading in quantitated gene expression data from an RNA-seq experiment, exploring the data using base R functions and then interpretation. The dataset contains an experiment between a diseased cell line and diseased cell lines treated with compound X. The difference in expression change between the two health status is computed as Fold change to log 2 (Log2FC) and the significance of each is computed in p-value.

[Dataset](https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt)

Task:
- Generate a volcano plot 📈.
- Determine the upregulated genes (Genes with Log2FC > 1 and pvalue < 0.01)
- Determine the downregulated genes (Genes with Log2FC < -1 and pvalue < 0.01)
- What are the functions of the top 5 upregulated genes and top 5 downregulated genes. (Use genecards)
- 
#### Project Workflow

1.	Data Cleaning and Exploration
o	Load and clean [Dataset](https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt) 
o	Check for duplicates and null values.
o Create new column for negative log10 of p-values.

2.	Generating volcano plot
o  The plot of gene Log2FC against negative p-value 
o	Thresholds were set for upregulated and downregulated genes which were significantly differentially expressed.

3.	Identification of Differntially Expressed Genes (DEGs)
o  Upregulated genes (Genes with Log2FC > 1 and pvalue < 0.01)
o  Downregulated genes (Genes with Log2FC < -1 and pvalue < 0.01)

#### Results & Findings

Functions of top 10 Differntially Expressed Genes

o  The functions of the top upregulated genes suggests that compound X may induce significant changes in the cellular environment, particularly affecting apoptosis and Extracellular Matrix organization.
o  These alterations could either promote a beneficial reprogramming of diseased cells towards a more normal state or modulate the tissue microenvironment to better support repair and defense mechanisms.
o  The changes in gene expression might therefore be part of the treatment's mechanism of action.
o  Compound X might be beneficial in reducing apostosis (which is commonly found in neurogenerative and inflammatory conditions) as genes that mediate cell apostosis were downregulated.


Here's the link to the [folder](https://github.com/aloyetunde/HackBio_Coding_Internship/tree/main/STAGE_2) containing our scripts , feel free to run the codes to replicate what we've done!😊
