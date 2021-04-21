import csv
from pprint import pprint


def define_topic():
    # {topic: {word: amount}}
    topic_word_count = {}

    # {topic: all words in this topic amount}
    topic_all_words = {}
    # {all unique words amount}
    unique_words = set()

    # all articles counter
    articles = 0
    # {topic: articles of this topic amount}
    topic_articles = {}

    with open("bbc_train.csv", encoding="utf-8") as f:
        rd = csv.reader(f)
        for topic, text in rd:
            articles += 1
            if topic in topic_articles.keys():
                topic_articles[topic] += 1
            else:
                topic_articles[topic] = 1
            for word in text.split():
                # lowercase tokens longer than 3 chars
                if len(word) > 3:
                    unique_words.add(word.lower())
                    if topic in topic_all_words.keys():
                        topic_all_words[topic] += 1
                        if word.lower() in topic_word_count[topic].keys():
                            topic_word_count[topic][word.lower()] += 1
                        else:
                            topic_word_count[topic][word.lower()] = 1
                    else:
                        topic_word_count[topic] = {word.lower(): 1}
                        topic_all_words[topic] = 1
    pprint(topic_all_words)
    pprint(len(unique_words))
    pprint(topic_articles)
    pprint(articles)


if __name__ == '__main__':
    define_topic()
