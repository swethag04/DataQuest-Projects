import pandas as pd
import numpy as np

#Read police_killings.csv into a Pandas Dataframe called police_killings
police_killings = pd.read_csv("police_killings.csv", encoding = "ISO-8859-1")
police_killings.columns
police_killings.head(5)

#discover how many people of each race were killed
raceethnicity = police_killings["raceethnicity"]
counts = raceethnicity.value_counts()
print(counts)

# make a bar graph of how many people of each race were killed
%matplotlib inline
import matplotlib.pyplot as plt
raceethnicity = police_killings["raceethnicity"]
counts = raceethnicity.value_counts()
print(counts)
plt.bar(range(6),counts)
plt.xticks(range(6), counts.index, rotation="vertical")

#create a new called income that contains all the values from the p_income column, except the dashes (-)
income = police_killings["p_income"][police_killings["p_income"] != "-"]
income.astype(float)

#generate a histogram on income
plt.hist(income.astype(float),bins=20)

state_pop = pd.read_csv("state_population.csv")

# find number of killings in each state
counts = police_killings["state_fp"].value_counts()
print (counts)

#make a new Dataframe states
states = pd.DataFrame({"STATE":counts.index, "shootings":counts})

#merge state_pop and states
states = states.merge(state_pop, on="STATE")

#create a new column with population in millions
states["pop_millions"] = states["POPESTIMATE2015"] / 1000000


#determine rate of police killings per million in each state
states["rate"] = states["shootings"] / states["pop_millions"]

#sort rate of killings
states.sort("rate")
police_killings["state"].value_counts()
pk = police_killings[
    (police_killings["share_white"] != "-") & 
    (police_killings["share_black"] != "-") & 
    (police_killings["share_hispanic"] != "-")
]

pk["share_white"] = pk["share_white"].astype(float)
pk["share_black"] = pk["share_black"].astype(float)
pk["share_hispanic"] = pk["share_hispanic"].astype(float)
lowest_states = ["CT", "PA", "IA", "NY", "MA", "NH", "ME", "IL", "OH", "WI"]
highest_states = ["OK", "AZ", "NE", "HI", "AK", "ID", "NM", "LA", "CO", "DE"]

ls = pk[pk["state"].isin(lowest_states)]
hs = pk[pk["state"].isin(highest_states)]
columns = ["pop", "county_income", "share_white", "share_black", "share_hispanic"]

ls[columns].mean()
hs[columns].mean()

