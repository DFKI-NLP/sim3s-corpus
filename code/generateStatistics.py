from Parser import parse
from collections import Counter
from glob import glob

files = glob("../corpus/" + '/**/*.xml', recursive=True)

for file in files:

    print("Loading file= " +file)

    #Load data
    trainText, trainSentiment, trainRelevance, trainId, trainOpinions = parse(file)
    flat_opinions = [item for sublist in trainOpinions for item in sublist]

    #Print statistics
    print("#Docs=" +str(len(trainText)))
    print("Relevance=" +str(Counter(trainRelevance)))
    print("Distribution of overall sentiment=" +str(Counter(trainSentiment)))
    print("#Opinions= " +str(len(flat_opinions)))
    print("Distribution of opinion-classes= "+str(Counter(list(map(lambda  x : x._category,  flat_opinions)))))


    print("-----")