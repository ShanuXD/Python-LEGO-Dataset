import pandas as pd
import matplotlib.pyplot as plt

df_colors = pd.read_csv('data/colors.csv', names=["ID", "COLOR", "RGB", "IS_TRANS"], header=0)
# print(df.head())
# print(df.tail())
# print(df_colors['COLOR'].nunique())
# print(df_colors.groupby('IS_TRANS').count())
# print(df_colors['IS_TRANS'].value_counts())

df_set = pd.read_csv('data/sets.csv')
# print(df_set['year'].min())

# First year
min_idx = df_set['year'].idxmin()

# how many different products the company was selling in their first year since launch
# print(df_set.loc[min_idx]) ----> wrong
# print(df_set[df_set['year'] == df_set['year'].min()])

# top 5 largest number of parts
top_five_logo = df_set.sort_values('num_parts', ascending=False)
# print(top_five_logo.head())

set_by_year = df_set.groupby('year').count()
# print(set_by_year['num_parts'].head())
# print(set_by_year['num_parts'].tail())

# plt.figure(figsize=(8, 5))

# plt.plot(set_by_year.index, set_by_year['num_parts'])

# plt.plot(set_by_year.index[:-2], set_by_year['num_parts'][:-2])
# plt.plot(set_by_year.index[:-2], set_by_year.num_parts[:-2])

# plt.show()


theme_by_year = df_set.groupby('year').agg({'theme_id': pd.Series.nunique})
# print(theme_by_year.head())
#
theme_by_year.rename(columns={'theme_id': 'nr_theme'}, inplace=True)
# print(theme_by_year.head())
# print(theme_by_year.tail())
#
# plt.plot(theme_by_year.index[:-1], theme_by_year.nr_theme[:-1])
# plt.show()

# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.plot(set_by_year.index[:-1], set_by_year.num_parts[:-1], color='r')
# ax2.plot(theme_by_year.index[:-1], theme_by_year.nr_theme[:-1], color='g')
# ax1.set_xlabel('Year')
# ax1.set_ylabel("Number of Sets", color='r')
# ax2.set_ylabel("Number of Themes", color='g')
# plt.show()


parts_per_set = df_set.groupby('year').agg({'num_parts': pd.Series.mean})
#
# plt.scatter(parts_per_set.index[:-1], parts_per_set[:-1])
# plt.show()

# set_theme = df_set['theme_id'].value_counts()
# print(set_theme.head())

themes = pd.read_csv('data/themes.csv')
# print(themes[themes.name == 'Star Wars'])
# print(df_set[df_set.theme_id == 18])
# print(df_set[df_set.theme_id == 209])

set_theme_count = df_set['theme_id'].value_counts()
set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})
# print(set_theme_count.head())

merged_df = pd.merge(set_theme_count, themes, on='id')

print(merged_df.head())


plt.figure(figsize=(8, 5))
plt.xticks(fontsize=8, rotation=45)
plt.yticks(fontsize=8)
plt.ylabel('Nr of Sets', fontsize=8)
plt.xlabel('Theme Name', fontsize=8)
plt.bar(merged_df.name[:5], merged_df.set_count[:5])
plt.show()