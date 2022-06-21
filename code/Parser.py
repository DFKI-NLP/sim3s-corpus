from xml.dom import minidom
import random

def parse(file, shuffle = False):
    xmldoc = minidom.parse(file)
    itemlist = xmldoc.getElementsByTagName('Document')

    documents = []
    for element in itemlist:

        id = element.attributes['id'].value
        text = element.getElementsByTagName('text')[0].firstChild.nodeValue
        sentiment = element.getElementsByTagName('sentiment')[0].firstChild.nodeValue
        relevance = element.getElementsByTagName('relevance')[0].firstChild.nodeValue

        oppinions =[]
        for opinion in element.getElementsByTagName('Opinion'):
            category = opinion.getAttribute('category')
            categories = category.split("#")
            if (len(categories) != 2):
                print("Expected number of categories = 2! for opinion= " + str(category))
            fromLoc = opinion.getAttribute('from')
            toLoc = opinion.getAttribute('to')
            target = opinion.getAttribute('target')
            polarity = opinion.getAttribute('polarity')
            oppinions.append(
                Oppinion(category=category, fromLoc=fromLoc, toLoc=toLoc, target=target, polarity=polarity,
                         mainCategory=categories[0], subCategory=categories[1]))

        document = Document(id=id, text=text, opinions=oppinions, relevance=relevance, sentiment=sentiment)
        documents.append(document)


    texts = []; sentiments = []; relevance = []; id = []; opinions=[];
    for document in documents:
        texts.append(document._text)
        sentiments.append(document._sentiment)
        relevance.append(document._relevance)
        id.append(document._id)
        opinions.append(document._opinions)

    if shuffle == True:
        combined = list(zip(texts, sentiments, relevance, id, opinions))
        random.Random(1202).shuffle(combined)
        texts[:], sentiments[:], relevance[:], id[:], opinions[:] = zip(*combined)

    return (texts, sentiments, relevance, id, opinions)

#Class to represent a single document
class Document:
    def __init__(self, id=None, text=None, opinions=None, relevance=None, sentiment=None):
        self._id = id
        self._text = text
        self._opinions = opinions
        self._relevance = relevance
        self._sentiment = sentiment

        @property
        def id(self):
            return self._id

        @property
        def text(self):
            return self._text

        @property
        def opinions(self):
            return self._opinions

        @property
        def relevance(self):
            return self._relevance

        @property
        def sentiment(self):
            return self._sentiment


        @id.setter
        def id(self, value):
            self._id = value

        @text.setter
        def text(self, value):
            self._text = value

        @opinions.setter
        def opinions(self, value):
            self._opinions = value

        @relevance.setter
        def relevance(self, value):
            self._relevance = value

        @sentiment.setter
        def sentiment(self, value):
            self._sentiment = value

    #Method to get string representation of a Document
    def __str__(self):
        return 'id=' + str(self._id) + " relevance= " + str(self._relevance) + " sentiment=" + str(self._sentiment)

#Class to represent an oppinion
class Oppinion:
    def __init__(self, category=None, fromLoc=None, toLoc=None, target=None, polarity=None, mainCategory=None, subCategory=None):
        self._category = category
        self._fromLoc = fromLoc
        self._toLoc = toLoc
        self._target = target
        self._polarity = polarity
        self._mainCategory = mainCategory
        self._subCategory = subCategory

        @property
        def category(self):
            return self._category

        @property
        def fromLoc(self):
            return self._fromLoc

        @property
        def toLoc(self):
            return self._toLoc

        @property
        def target(self):
            return self._target

        @property
        def polarity(self):
            return self._polarity

        @property
        def mainCategory(self):
            return self._mainCategory

        @property
        def subCategory(self):
            return self._subCategory

        @category.setter
        def category(self, value):
            self._category = value

        @fromLoc.setter
        def fromLoc(self, value):
            self._fromLoc = value

        @toLoc.setter
        def toLoc(self, value):
            self._toLoc = value

        @target.setter
        def target(self, value):
            self._target = value

        @polarity.setter
        def polarity(self, value):
            self._polarity = value

        @mainCategory.setter
        def mainCategory(self, value):
            self._mainCategory = value

        @subCategory.setter
        def subCategory(self, value):
            self._subCategory = value

    #Method to get string representation of an Oppinion
    def __str__(self):
        return 'polarity=' + self._polarity + " category= " + self._category + " target=" + self._target +" " +self._fromLoc+"-" +self._toLoc +" main=" +self._mainCategory +" sub=" +self._subCategory

## Class to represent OEPV
class OEPV:
    def __init__(self, fromLoc, toLoc, reltype, target):
        self._fromLoc = fromLoc
        self._toLoc = toLoc
        self._reltype = reltype
        self._target = target

        @property
        def fromLoc(self):
            return self._fromLoc

        @property
        def toLoc(self):
            return self._toLoc

        @property
        def reltype(self):
            return self._reltype

        @property
        def target(self):
            return self._target

        @fromLoc.setter
        def fromLoc(self, value):
            self._fromLoc = value

        @toLoc.setter
        def toLoc(self, value):
            self._toLoc = value

        @reltype.setter
        def reltype(self, value):
            self._reltype = value

        @target.setter
        def target(self, value):
            self._target = value

    # Method to get string representation of an OEPV
    def __str__(self):
        return 'reltype=' + self._reltype +" target=" + self._target + " " + self._fromLoc + "-" + self._toLoc

