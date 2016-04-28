import pandas as pd
import numpy as np

#specify an encoding because the dataset has some characters that aren't in the Python default utf-8 encoding
star_wars = pd.read_csv("star_wars.csv", encoding ="ISO-8859-1")
star_wars.head(3)
star_wars.columns.values

#remove rows where respondentid is nan
star_wars = star_wars[pd.notnull(star_wars["RespondentID"])]

# convert yes/no to boolean true/false using dictionary and map function
yes_no = {
	"Yes": True,
	"No": False
}
star_wars["Have you seen any of the 6 films in the Star Wars franchise?"] = star_wars["Have you seen any of the 6 films in the Star Wars franchise?"].map(yes_no)

star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"]= star_wars["Do you consider yourself to be a fan of the Star Wars film franchise?"].map(yes_no)
star_wars.head(15)

# convert columns 3 to 9 to boolean
movie_map = {
	"Star Wars: Episode I  The Phantom Menace": True,
	np.nan: False,
	"Star Wars: Episode II  Attack of the Clones": True,
	"Star Wars: Episode III  Revenge of the Sith": True,
	"Star Wars: Episode IV  A New Hope": True,
	"Star Wars: Episode V The Empire Strikes Back": True,
	"Star Wars: Episode VI Return of the Jedi": True
}

star_wars["Which of the following Star Wars films have you seen? Please select all that apply."]= star_wars["Which of the following Star Wars films have you seen? Please select all that apply."].map(movie_map)
star_wars["Unnamed: 4"]= star_wars["Unnamed: 4"].map(movie_map)
star_wars["Unnamed: 5"] = star_wars["Unnamed: 5"].map(movie_map)
star_wars["Unnamed: 6"] = star_wars["Unnamed: 6"].map(movie_map)
star_wars["Unnamed: 7"] = star_wars["Unnamed: 7"].map(movie_map)
star_wars["Unnamed: 8"] = star_wars["Unnamed: 8"].map(movie_map)
star_wars.head(15)

#rename columns 3 to 9
star_wars = star_wars.rename(columns={
    	"Which of the following Star Wars films have you seen? Please select all that apply.": "seen_1",
    	"Unnamed: 4" : "seen_2",
    	"Unnamed: 5" : "seen_3",
    	"Unnamed: 6" : "seen_4",
    	"Unnamed: 7" : "seen_5",
    	"Unnamed: 8" : "seen_6",
	})

# convert datatype of columns 9 to 15 to float and rename columns
star_wars[star_wars.columns[9:15]]= star_wars[star_wars.columns[9:15]].astype(float)

star_wars = star_wars.rename(columns={
   	"Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "ranking_1" ,
   	"Unnamed: 10" : "ranking_2",
   	"Unnamed: 11" : "ranking_3",
   	"Unnamed: 12" : "ranking_4",
   	"Unnamed: 13" : "ranking_5",
   	"Unnamed: 14" : "ranking_6"
   	 
	})

# find the highest ranked movie by calculating mean
print(star_wars["ranking_1"].mean())
print(star_wars["ranking_2"].mean())
print(star_wars["ranking_3"].mean())
print(star_wars["ranking_4"].mean())
print(star_wars["ranking_5"].mean())
print(star_wars["ranking_6"].mean())
star_wars[star_wars.columns[9:15]].mean()

%matplotlib inline
import matplotlib.pyplot as plt
plt.bar(range(0,6), star_wars[star_wars.columns[9:15]].mean())

# find the most seen movie by calculating sum
star_wars[star_wars.columns[3:9]].sum()
plt.bar(range(0,6), star_wars[star_wars.columns[3:9]].sum())

#split dataframe into two groups based on gender - male and female and find most seen and highest ranked movie by gender
males = star_wars[star_wars["Gender"] == 'Male']
males[males.columns[9:15]].mean()
plt.bar(range(0,6), males[males.columns[9:15]].mean())

females = star_wars[star_wars["Gender"]== 'Female']
plt.bar(range(0,6), females[females.columns[9:15]].mean())

plt.bar(range(0,6), males[males.columns[3:9]].sum())
plt.bar(range(0,6), females[females.columns[3:9]].sum())
