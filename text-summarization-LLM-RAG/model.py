import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

df = pd.read_csv('data/vendor_reviews.csv')
def categorize_rating(rating):
    if rating >= 4.0:
        return 'Good'
    elif 2.5 <= rating < 4.0:
        return 'Average'
    else:
        return 'Bad'

df['Label'] = df['rating'].apply(categorize_rating)

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())  # Remove punctuation and lower case
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text

df['cleaned_text'] = df['review'].apply(clean_text)




vectorizer = TfidfVectorizer(max_features=5000)
X= vectorizer.fit_transform(df['cleaned_text']).toarray()
X = pd.concat([pd.DataFrame(X), df[['rating']]], axis=1)
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.columns = X_train.columns.astype(str)
X_test.columns = X_test.columns.astype(str)


if __name__ == "__main__":


    model = LogisticRegression()
    model2 = MultinomialNB()

    model.fit(X_train, y_train)
    model2.fit(X_train, y_train)



    y_pred = model.predict(X_test)

    df.rename(columns={'label': 'predicted_sentiment'}, inplace=True)
    df.to_csv('updated_dataset_with_sentiment.csv', index=False)