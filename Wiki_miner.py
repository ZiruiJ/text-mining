import wikipedia
import string
import pickle


# babson = wikipedia.page("Babson College")
# print(babson.title)
# print(babson.url)
# print(babson.content)

def process_page(pagename):
    """Makes a histogram that contains the words from a page.
    pagename: string
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    page_content = wikipedia.page(pagename).content
    print(type(page_content))
    print(page_content)

    page_content = page_content.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in page_content.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1

    
    return hist

# print(process_page('Babson College'))
# print(process_page('Boston University'))


def most_common(hist ,excluding_stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.
    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.
    returns: list of (frequency, word) pairs
    """
    hist = process_page("Bentley University")
    t = []
    f = open("stopwords.txt","r")
    stopwords = f.readlines()
    stopwords = list(stopwords)


    for word, freq in hist.items():
        if excluding_stopwords:
            if word  in stopwords:
                continue
        t.append((freq,word))
    t.sort(reverse=True)
    return t

# print(most_common('Babson College'))

def print_most_common(hist, num=40):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)

print (print_most_common('Bentley University'))




# bu= wikipedia.page ("Boston University")
# print (bu.title)
# print (bu.url)
# print (bu.content)

# bc= wikipedia.page ("Boston College")
# print (bc.title)
# print (bc.url)
# print (bc.content)

# bentley= wikipedia.page ("Bentley University")
# print (bentley.title)
# print (bentley.url)
# print (bentley.content)

