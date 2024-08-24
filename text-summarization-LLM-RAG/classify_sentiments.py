import pandas as pd


data_for_review = pd.read_csv("dataset_with_sentiment.csv")

data_for_el = data_for_review.loc[data_for_review["category"]=="Electronics_5"].reset_index(drop=True)

data_for_el = data_for_el[['category', 'vendors','Label', 'cleaned_text']]

# Group by vendors and label, and then summarize the cleaned_text for each group
summary_df = data_for_el.groupby(['vendors', 'Label'])['cleaned_text'].apply(lambda texts: ' '.join(texts)).reset_index()



