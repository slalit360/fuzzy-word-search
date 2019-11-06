import operator

word_dict = {}

with open('word_search.tsv') as file:
    for row in file:
        word, count = row.split('\t')
        word_dict[word.strip()] = int(count.strip())


def getMatchingWord(word_searched):
    matchedword = []
    resultsWord = []

    matcheddict = {k: v for k, v in word_dict.items() if word_searched in k }
    matchedword = matcheddict.keys()

    result_tuple = [ ( wd, wd.find(word_searched)+1, word_dict[wd], len(wd) ) for wd in matchedword ]
    result_tuple.sort( key=operator.itemgetter(1) ) # sort on pos_idx prefix ranks higher
    print([i[1] for i in result_tuple][:25])

    #result_tuple.sort(key=operator.itemgetter(2), reverse=True) # sort on common ranks higher
    #print([i[2] for i in result_tuple][:25])

    result_tuple.sort(key=operator.itemgetter(3))  # sort on len shorter ranks higher
    print([i[3] for i in result_tuple][:25])

    resultsWord = [i[0] for i in result_tuple][:25]

    print("Matched Word : ", len(matchedword))
    print("Result Word: ", len(resultsWord))

    return resultsWord

