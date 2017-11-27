#https://github.com/aspera1631/vis_demo_data
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Import data
data1 = pd.read_csv('https://raw.githubusercontent.com/aspera1631/vis_demo_data/master/pop_vs_degrees.csv')

print data1

#Rescale the data
data1['degrees'] = data1['degrees']/10000
data1['pop'] = data1['pop']/1000000

#Set the context and font size
sns.set_context("poster", font_scale=1)
#Create a figure and set its size
plt.figure(figsize=(10, 8))

#Create the regression plot, where we supply x and y columns. "g" = green.
g = sns.regplot(x='pop', y='degrees', data = data1, color= "g")
#Set the plot limits, axis labels, and chart title.
g.set(xlim= (0), ylim= (0), xlabel= "Population [millions]", ylabel= "Total degrees/awards in 2013 [x10k]", title= "Total awards vs. population by state")


#Seaborn colorschemes
# Seaborn can tap into colorbrewer, whose color schemes are illustrated here.  colorbrewer.org
#Kuler

data2 = pd.read_csv('datasets/opt_by_inst.csv')

#Set context, increase font size
sns.set_context("poster", font_scale=1.5)
#Create a figure
plt.figure(figsize=(15, 8))
#Define the axis object
ax = sns.barplot(x='optics graduates', y='inst_nm', data=data2, palette="Blues_d")
#set paramters
ax.set(xlabel='Optics PhDs awarded', ylabel='Institution name', title= "Top optics-granting institutions")




#Pokemon
#https://elitedatascience.com/wp-content/uploads/2017/04/Pokemon.csv
df = pd.read_csv('Pokemon.csv', index_col=0)
df.head()


# Recommended way
sns.lmplot(x='Attack', y='Defense', data=df)
 
# Alternative way
# sns.lmplot(x=df.Attack, y=df.Defense)

#Remove reg fit line
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, # No regression line
           hue='Stage')   # Color by evolution stage


#sensible axes, look at negative axis points
#Seaborn is built on top of matplotlib and although seaborn is usually enough, sometimes we need to call matplotlib

# Plot using Seaborn
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, 
           hue='Stage')
 
# Tweak using Matplotlib
plt.ylim(0, None)
plt.xlim(0, None)


#The role of pandas
#Boxplot
sns.boxplot(data=df)


#Dropping columns, (easier to do in pandas beforehand)

2
3
4
5
# Pre-format DataFrame
stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
 
# New boxplot using stats_df
sns.boxplot(data=stats_df)


#Seaborn themes

# Set theme
sns.set_style('whitegrid')
 
# Violin plot
sns.violinplot(x='Type 1', y='Attack', data=df)

#Maybe you want to make the colors match the type? Can specify your own colorscheme

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]
                   
#Notice the order above matches the order of cols

# Violin plot with Pokemon color palette
sns.violinplot(x='Type 1', y='Attack', data=df, 
               palette=pkmn_type_colors) # Set color palette

#Violin plots are good for distributions but we don't have that many datapoints so we can zoom in further
#That's where the swarm plot comes in. This visualization will show each point, while "stacking" those with similar values:
# Swarm plot with Pokemon color palette
sns.swarmplot(x='Type 1', y='Attack', data=df, 
              palette=pkmn_type_colors)

#Combine plots?
# Set figure size with matplotlib
plt.figure(figsize=(10,6))
 
# Create plot
sns.violinplot(x='Type 1',
               y='Attack', 
               data=df, 
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)
 
sns.swarmplot(x='Type 1', 
              y='Attack', 
              data=df, 
              color='k', # Make points black
              alpha=0.7) # and slightly transparent
 
# Set title with matplotlib
plt.title('Attack by Type')


#What is we want to see other stats together?
	
stats_df.head()
#Currently everything is in different columns so we need to do some data manipulation
#Panda's melt function has 3 arguments: df to melt, variables to keep (others will be melted), new name for melted variable

# Melt DataFrame
melted_df = pd.melt(stats_df, 
                    id_vars=["Name", "Type 1", "Type 2"], # Variables to keep
                    var_name="Stat") # Name of melted variable
melted_df.head()

#plt.clf()
#Now we can use swarm plot but x val will be stat and y will be the corresponding value
# Swarmplot with melted_df
sns.swarmplot(x='Stat', y='value', data=melted_df, 
              hue='Type 1')


#Few final tweaks

# 1. Enlarge the plot
plt.figure(figsize=(10,6))
 
sns.swarmplot(x='Stat', 
              y='value', 
              data=melted_df, 
              hue='Type 1', 
              split=True, # 2. Separate points by hue
              palette=pkmn_type_colors) # 3. Use Pokemon palette
 
# 4. Adjust the y-axis
plt.ylim(0, 260)
 
# 5. Place legend to the right
plt.legend(bbox_to_anchor=(1, 1), loc=2)



#Some other plots
# Distribution Plot (a.k.a. Histogram)
sns.distplot(df.Attack)


#Joint distribution plots combine information from scatter plots and histograms to give you detailed information for bi-variate distributions.
# Joint Distribution Plot
sns.jointplot(x='Attack', y='Defense', data=df)



