# SentimentAnalysis

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: Kodakandla Rushikesh Reddy

*INTERN ID*: CTO4WP231

*DOMAIN*: DATA ANALYTICS

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*This Python script uses the TextBlob library to analyze the sentiment of a list of text reviews. The process of identifying whether a text conveys a positive, negative, or neutral emotion is known as sentiment analysis. The script starts by importing the two necessary libraries: pandas for data management and tabulation, and TextBlob for sentiment analysis and natural language processing.

The purpose of the analyze() function is to assess each text input's sentiment. The polarity score, which ranges from -1.0 to 1.0, is determined by converting the input text into a TextBlob object. Neutral sentiment is indicated by a polarity value of precisely zero, negative sentiment is suggested by a value below zero, and positive sentiment is indicated by a value above zero.

The next step is to generate a small dataset of comments or product reviews using a few sample sentences from a Python dictionary. The data is first converted into a pandas DataFrame so that the text can be arranged in a columnar fashion. The sentiment of each sentence is identified as "positive," "negative," or "neutral" using the analyze() function and apply() method. This is appended to a new column called "sentiment." The original list of sentences and the sentiments are printed when the DataFrame with the processed data is printed. This method is able to effectively analyze the general sentiment that is held in a set of text data using basic NLP techniques.*

*OUTPUT*
