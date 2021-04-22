import csv
import math
from pprint import pprint

# {topic: {word: amount}}
topic_word_count = {}

# {topic: all words in this topic amount}
topic_all_words = {}
# {all unique words amount}
unique_words = set()

# {topic: articles of this topic amount}
topic_articles = {}


def train_topic():
    # all articles counter
    articles = 0

    with open("bbc_train.csv", encoding="utf-8") as f:
        rd = csv.reader(f)
        for topic, text in rd:
            articles += 1
            if topic in topic_articles.keys():
                topic_articles[topic] += 1
            else:
                topic_articles[topic] = 1
            for word in text.split():
                word = word.lower()
                # lowercase tokens longer than 3 chars
                if len(word) > 4:
                    unique_words.add(word)
                    if topic in topic_all_words.keys():
                        topic_all_words[topic] += 1
                        if word in topic_word_count[topic].keys():
                            topic_word_count[topic][word] += 1
                        else:
                            topic_word_count[topic][word] = 1
                    else:
                        topic_word_count[topic] = {word: 1}
                        topic_all_words[topic] = 1
    return articles


def define_topic():
    correct_topics = 0
    incorrect_topics = 0
    articles_amount = train_topic()
    topic_possibility = {}

    with open("bbc_test.csv", encoding="utf-8") as f:
        rd = csv.reader(f)
        for topic, text in rd:
            for key in topic_articles.keys():
                topic_possibility[key] = math.log(topic_articles[key] / articles_amount)
            for word in text.split():
                word = word.lower()
                if len(word) > 4:
                    for key in topic_possibility.keys():
                        if word in topic_word_count[key].keys():
                            pwc = (topic_word_count[key][word] + 1) / (topic_all_words[topic] + len(unique_words))
                        else:
                            pwc = 1 / (topic_all_words[key] + len(unique_words))
                        topic_possibility[key] = topic_possibility[key] + math.log(pwc)
            max_possibility_topic = ""
            max_possibility = 0
            for key in topic_possibility.keys():
                if topic_possibility[key] > max_possibility or max_possibility == 0:
                    max_possibility = topic_possibility[key]
                    max_possibility_topic = key
            if max_possibility_topic == topic:
                correct_topics += 1
            else:
                incorrect_topics += 1
            topic_possibility.clear()
    pprint("correct: " + str(correct_topics))
    pprint("incorrect: " + str(incorrect_topics))
    pprint("accuracy: " + str((100 * correct_topics) / (correct_topics + incorrect_topics)) + "%")


if __name__ == '__main__':
    define_topic()
