# 🚀 HackBio_Coding_Internship - #Team Leucine
#Stage 1 Task

📌Task Instructions:
1. Write a function for translating DNA to protein 🧬
2. Write a function that simulates and generates a logistic population growth curve. Your function should include 2 extra parameters that randomize the length of the lag phase and the exponential phase. Most living populations follow a logistic population growth. Therefore, your growth curve can be: #Population Size vs Time, Cell density vs Time, OD vs Time, CFU vs Time, etc#
3. Using your function, generate a dataframe with 100 different growth curves. Write a function for determining the time to reach 80% of the maximum growth; usually the carrying capacity
4. Finally, write a function for calculating the hamming distance between your Slack username and twitter/X handle.

📚Key Python concepts we used:

- #Conditionals# - (if, elif and else statements).
- #Loops# - which aid iteration of codes (For Loop).
- #Functions# - which are needed to pass data and can be called anytime it is needed while scripting.
- #String Manipulation# - Essential for our Hamming distance calculations.

✅Task Implementation 
🧬 Task 1: DNA to Protein Translation
We defined a function (dna_translation) that:
•	Takes a DNA sequence as input.
•	Splits it into codons (triplets of bases).
•	Uses a standard genetic code dictionary with full amino acid names (codon_table) to translate each triplet into an amino acid.
•Stops transalation at stop codon
•	Returns the protein sequence! 

📈 Step 2: Logistic Growth Curve
We created a function that:
•	Simulates logistic population growth.
•	Includes randomized lag and exponential phases.
•	Uses mathematical modeling to reflect real-life population dynamics.

📊 Step 3: Generating 100 Growth Curves & Finding 80% Max Growth
•	Our function generates 100 unique growth curves and stores them in a dataframe.
•	Another function then analyzes the data and determines the time to reach 80% of carrying capacity.

🔢 Step 4: Hamming Distance Calculation
•	This function takes in two strings (our Slack username and X handle).
•	Compares them character by character to count the differences.
•	Returns the Hamming distance (i.e., how “different” they are).

Here's the link to our script, , feel free to run the codes to replicate what we've done!😊
