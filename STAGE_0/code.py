# Step 1: Organizing the information into lists

names = ["Alo Yetunde", "Oluchi Bolanle", "Adewunmi Ifeoluwa", "Adedayo Adeboye", "Omojuwa Iyinoluwa"]
slack_usernames = ["MaryAde364", "Oluchi Bolanle", "Ifeoluwa", "Adedayo", "Iyinomj"]
emails = ["aloyetunde99@gmail.com", "oluchibolanle@gmail.com", "iadewunmi39@gmail.com", "timsonad09@gmail.com", "iyinomojuwa1@gmail.com"]
hobbies = ["Reading", "Journaling", "Reading", "Playing games", "Cooking"]
countries = ["Nigeria", "Nigeria", "Nigeria", "Nigeria", "Nigeria"]
disciplines = ["Biochemistry", "Biochemistry", "Physiology", "Pharmacy", "Biotechnology"]
languages = ["Python", "Python", "Python", "Python", "Python"]

# Step 2: Converting to a DataFrame-like structure (without using pandas)
dataframe = f"""
| Name                 | Slack Username   | Email                      | Hobby         | Country  | Discipline     | Language |
|----------------------|-----------------|----------------------------|--------------|---------|--------------|----------|
| {names[0]}  | {slack_usernames[0]}  | {emails[0]}  | {hobbies[0]}  | {countries[0]}  | {disciplines[0]}  | {languages[0]} |
| {names[1]}  | {slack_usernames[1]}  | {emails[1]}  | {hobbies[1]}  | {countries[1]}  | {disciplines[1]}  | {languages[1]} |
| {names[2]}  | {slack_usernames[2]}  | {emails[2]}  | {hobbies[2]}  | {countries[2]}  | {disciplines[2]}  | {languages[2]} |
| {names[3]}  | {slack_usernames[3]}  | {emails[3]}  | {hobbies[3]}  | {countries[3]}  | {disciplines[3]}  | {languages[3]} |
| {names[4]}  | {slack_usernames[4]}  | {emails[4]}  | {hobbies[4]}  | {countries[4]}  | {disciplines[4]}  | {languages[4]} |
"""

# Step 3: Printing the structured information
print(dataframe)
