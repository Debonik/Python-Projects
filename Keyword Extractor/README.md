# Keyword Extraction and Frequency Analysis

This code analyzes an article to find the main keywords and count how often they appear. Here's what each part of the code does:

## 1. Importing Libraries

The code uses three libraries:
- `TextBlob` to analyze the text.
- `nltk` to handle language processing tools.
- `Counter` from `collections` to count the keywords.

```python
from textblob import TextBlob
import nltk
from collections import Counter
```

## 2. Downloading Resources

The code makes sure the necessary resources are downloaded for text analysis.

```python
nltk.download('brown')
nltk.download('punkt')
```

## 3. Extracting Keywords and Counting Frequency

A function called `extract_keywords` is defined to do the following:

- Check if the text is not empty.
- Use `TextBlob` to find keywords (called noun phrases).
- Count how often each keyword appears.
- Pick the main keywords that appear more than once (you can change this).

```python
def extract_keywords(text):
    ...
    keyword_counts = Counter(keywords)
    main_keywords = {keyword: count for keyword, count in keyword_counts.items() if count > 1}
    return main_keywords
```

## 4. Analyzing the Article

The code then:
- Checks if the article is at least 1000 words.
- Calls the `extract_keywords` function to get the main keywords and their frequency.
- Prints the results.

```python
try:
    keywords_with_frequency = extract_keywords(article)
    print("Main Keywords with Frequency:")
    for keyword, frequency in keywords_with_frequency.items():
        print(f"Keyword: {keyword} - Frequency: {frequency}")
except Exception as e:
    print("An error occurred:", str(e))
```

## Summary

This code helps you understand what an article is about by finding the main topics (keywords) and seeing how often they are mentioned. It's like a quick summary of the article's main points.

You can use this code with any article by replacing the sample text with your own 1000-word article.
