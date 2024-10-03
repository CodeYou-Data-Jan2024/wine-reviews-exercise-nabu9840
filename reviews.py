import pandas as pd
wine_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')
country_summary = wine_reviews.groupby('country'), num_reviews = ('country', 'size'), average_points = ('points', 'mean')
wine_reviews.sort_values(by='points', ascending=True)
wine_reviews.to_csv('reviews-per-country.csv', index=False)