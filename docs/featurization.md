# Featurization Stage

```python
from sklearn.feature_extraction.text import CountVectorizer

max_features = 100
ngrams = 3 # tri gram

# since a word can't give a proper understaing but the whole sentence will that's why Countvectorize is used
vectorizer = CountVectorizer(max_features = max_features, ngram_range=(1, ngrams)) 
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names_out())
```