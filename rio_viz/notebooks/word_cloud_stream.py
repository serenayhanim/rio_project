from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)
stopwords.add('rioferdy5')
stopwords.add('@rioferdy5')

def clean_data(dataframe):
    "clean text column"
    dataframe['tweet_clean'] = dataframe['text'].str.replace('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ')
    dataframe['tweet_clean'] = dataframe['text'].str.replace('@[A-Za-z0-9]+', ' ')
    dataframe['tweet_clean'] = dataframe['tweet_clean'].str.replace("didn't|ain't|don't|doesn't|wouldn't", " ")
    dataframe['tweet_clean'] = dataframe['tweet_clean'].str.replace("\'|rioferdy5|ll", " ")
    return(dataframe)

def show_wordcloud(data, title = None):
    "plot wordcloud"
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        width = 400,
        height = 300,
        max_words=200,
        min_font_size=6,
        max_font_size=40, 
        relative_scaling=0,
        scale=3,
        repeat=False,
        collocations=True,
        collocation_threshold=5,
        random_state=2 # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()