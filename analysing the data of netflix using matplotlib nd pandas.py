''' analysing the data of netflixusing matplotlib and pandas'''
# import the libraries
import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv('netflix_titles.csv')
# print the first 5 rows of the data
# print(data.head())

# removes null values
df = df.dropna(subset=['type', 'release_year' , 'country' , 'rating', 'duration'])

# how many movies and tv shows are there in the data( bar chart)
type_count = df['type'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(type_count.index, type_count.values, color=['skyblue', 'orange'])
plt.title('Number of Movies and TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
# plt.show()

# percentage of ratings distribution (pie chart)
rating_count = df['rating'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(rating_count , labels=rating_count.index, autopct='%1.1f%%', startangle=90) # startangle for rotation counterclockwise
plt.title('Percentage of Ratings Distribution on Netflix')
plt.tight_layout()
plt.savefig('content_ratings_pie.png')
# plt.show()

# duration wise distribution of movies (histogram)
movie_df = df[df['type'] == 'Movie'].copy() # create a copy
movie_df['duration'] = movie_df['duration'].str.replace(' min', '').astype(int) # convert to int and minutes
plt.figure(figsize=(8, 6))
plt.hist(movie_df['duration'], bins=30, color='purple', edgecolor='black')
plt.title('Duration Distribution of Movies on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movie_duration_histogram.png')
# plt.show()

# no of release over years(scatter plot)
release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.scatter(release_counts.index, release_counts.values, color='green')
plt.title('Number of Releases Over the Years on Netflix')
plt.xlabel('Year')
plt.ylabel('Number of Releases')
plt.tight_layout()
plt.savefig('releases_over_years.png')
# plt.show()

# top 10 countries with most content (horizontal bar chart)
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8, 6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Countries with Most Content on Netflix')
plt.xlabel('Number of Shows/Movies')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top_10_countries.png')
# plt.show()

# compare movies and tv shows over the years (subplots line chart)
content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
''' groups data by release year and type , counts no of rows in each group
, turns type level into columns , fills null values with 0'''
fig , ax = plt.subplots(1 , 2 , figsize=(12 , 5))

# plot movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Number of Movies Released Over the Years on Netflix')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# plot tv shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[1].set_title('Number of TV Shows Released Over the Years on Netflix')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Movies vs TV Shows Released Over the Years on Netflix', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # adjust layout to make room for suptitle
plt.savefig('movies_vs_tvshows_over_years.png')
plt.show()