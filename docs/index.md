## Analyzing deaths in France in 2020

You can use the [editor on GitHub](https://github.com/GreLeBr/deces_2020/edit/master/docs/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Age pyramid of deaths in France



```python
# Building categories for age group
bins = pd.IntervalIndex.from_tuples([(0, 5), (5, 10), (10, 15), (15,20),(20,25), (25,30), (30,35), (35,40), (40,45), (45,50), (50, 55),(55, 60), (60,65), (65,70), (70,75), (75, 80), (80,85), (85, 90), (90, 95), (95,100), (105,110), (110,115) ])

# Starting by making temp columns
df["birthdate1"]=df["datenaiss"].astype("str")
df["deathdate1"]=df["datedeces"].astype("str")
# Assigning "NaN" to missing dates
df["birthdate1"]=df["birthdate1"].apply(lambda x: np.nan if "00" in x[-2:] or "00" in x[-4:-2] or "0000" in x[:-4] or x=="0" else x)
df["deathdate1"]=df["deathdate1"].apply(lambda x: np.nan if "00" in x[-2:] or "00" in x[-4:-2] or "0000" in x[:-4] or x=="0" else x)
# Dropping missing values
df.dropna(inplace=True)
# Dropping temp columns
df.drop(columns=["deathdate1", "birthdate1"], inplace=True)
# Converting date str to date values
df["birthdate"]=pd.to_datetime(df["datenaiss"],  format='%Y%m%d')
df["deathdate"]=pd.to_datetime(df["datedeces"],  format='%Y%m%d')
# Assigning age group to rows
df['Range']=df.groupby("sexe", as_index=False)[["lifespan"]].transform(lambda x: pd.cut(x, bins) )

# Splitting First name and last name
df["nomprenomsplit"]=df["nomprenom"].apply(lambda x: x.split("*"))
df["nom"]=df["nomprenomsplit"].apply(lambda x: x[0])
df["prenom"]=df["nomprenomsplit"].apply(lambda x: x[1])
df["prenom"]=df["prenom"].apply(lambda x: x.replace("/", ""))

# Drawing figure

plt.figure(figsize=(20,15))
plt.xlim((-90000, 90000))
plt.axvline(x=0, linestyle='--', color="black")

bar_plot = sns.barplot(x='lifespan', y='Range', data=data[22:],  order=data["Range"][21::-1])

for ytick in bar_plot.get_yticks():
    bar_plot.text(data["lifespan"][21-ytick] + 100+ data["lifespan"][21-ytick]* 0.05 ,ytick,  data["lifespan"][21-ytick], verticalalignment="center",  fontsize=14 )

bar_plot = sns.barplot(x='lifespan', y='Range', data=data[:22],  order=data["Range"][21::-1])
for ytick in bar_plot.get_yticks():
    bar_plot.text(data["lifespan"][43-ytick] -7000 + data["lifespan"][43-ytick]* 0.05, ytick,  -data["lifespan"][43-ytick], verticalalignment="center", ha="left", fontsize=14)  

bar_plot.tick_params( axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

bar_plot.set_xlabel(xlabel="Number of deaths in 2020",fontsize=18 )
bar_plot.set_ylabel(ylabel="Age ranges",fontsize=18 )

props = dict(boxstyle='round', facecolor='yellow', alpha=0.5)

bar_plot.text(50000, 20, "Men", fontsize=25,bbox=props )
bar_plot.text(-50000, 20, "Women", fontsize=25, bbox=props )


``` 

[Predict age by name](https://www.ekintzler.com/projects/age-prediction/)
[Choropleth on Heroku](https://choropleth-greg.herokuapp.com/)
[Choropleth on GitHub](https://grelebr.github.io/deces_2020/choropleth.html)


markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)


For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/GreLeBr/deces_2020/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.

