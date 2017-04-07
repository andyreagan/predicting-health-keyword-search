# processTweetsNew.py
# crawl the tweets, and look for keywords
# output with daily resolution
#
# NOTES
# uses the new 15-minute compressed format
# 
# USAGE 
# gzip -cd tweets.gz | python processTweetsNew.py 2014-01-01 keywords
#  
# this will read keywords.txt and the tweets from stdin
# and save a frequency file, labMT vector in keywords/[keyword]
# for each keyword

# we'll use most of these
from json import loads,dumps
import codecs
import datetime
import re
import sys

def tweetreader(tweet,outfile):
    # takes in the hashtag-stripped text
    # the keyword list
    # and the title of the file to append to
    for keyword in keyWords:
        if keyword["re"].search(tweet["text"]) is not None:
            # print("match for {0}:".format(keyword["folder"]))
            # print(tweet["text"])
            g = codecs.open("raw-tweets/{0}/{1}.txt".format(keyword["folder"],outfile),"a","utf8")
            g.write(dumps(tweet))
            g.write("\n")
            g.close()
        # else:
        #     print("no match for {0}".format(keyword["folder"]))

def gzipper(outfile):
    f = sys.stdin
    for line in f:
        try:
            tweet = loads(line)
        except:
            print "failed to load a tweet"
        if "text" in tweet:
            # print("found text")
            tweetreader(tweet,outfile)

keyWords = [{
        "re": re.compile(r"\b[0-9]+ (?:days|weeks) pregnant\b",flags=re.IGNORECASE),
        "folder": "pregnant-1",
        },
                {
        "re": re.compile(r"\bdue in [0-9]+ weeks\b",flags=re.IGNORECASE),
        "folder": "pregnant-2",
        },
                {
        "re": re.compile(r"\bdue to give birth in [0-9]+ weeks\b",flags=re.IGNORECASE),
        "folder": "pregnant-3",
        },
                {
        "re": re.compile(r"\b(?:i'm|am|we're|we are) (?:pregnant|preggers|preggo)\b",flags=re.IGNORECASE),
        "folder": "pregnant-4",
        },
                {
        "re": re.compile(r"\b(?:i'm|am) (?:going to have a baby|having a baby)\b",flags=re.IGNORECASE),
        "folder": "pregnant-5",
        },
                {
        "re": re.compile(r"\bi (?:was|have)(?: been diagnosed with|)[a-z ]*cancer\b",flags=re.IGNORECASE),
        "folder": "cancer-1",
        },
                {
        "re": re.compile(r"\bmy doctor prescribed (?:prozac|xanax|abilify)\b",flags=re.IGNORECASE),
        "folder": "depression-1",
        },
                {
        "re": re.compile(r"\bi am taking (?:prozac|xanax|abilify)\b",flags=re.IGNORECASE),
        "folder": "depression-2",
        },
            {
        "re": re.compile(r"\bi[a-z ]*diagnosed with depression\b",flags=re.IGNORECASE),
        "folder": "depression-3",
        },
                            {
        "re": re.compile(r"\bmy [a-z]+ told me (?:i'm|i am) depressed\b",flags=re.IGNORECASE),
        "folder": "depression-4",
        },
                            {
        "re": re.compile(r"\bi [a-z ]+ (?:depressed|depression)\b",flags=re.IGNORECASE),
        "folder": "depression-5",
        },
                            {
        "re": re.compile(r"\bi (?:am|was) diagnosed with (?:ptsd|post(?:-| )traumatic stress disorder)\b",flags=re.IGNORECASE),
        "folder": "ptsd-1",
        },
                            {
        "re": re.compile(r"\bmy [a-z ]+ told me i have (?:ptsd|post(?:-| )traumatic stress disorder)\b",flags=re.IGNORECASE),
        "folder": "ptsd-2",
        },
                            {
        "re": re.compile(r"\bi recieved a (?:ptsd|post(?:-| )traumatic stress disorder) diagnosis\b",flags=re.IGNORECASE),
        "folder": "ptsd-3",
        },
                            {
        "re": re.compile(r"\bi [a-z ]+ (?:ptsd|post(?:-| )traumatic stress disorder)\b",flags=re.IGNORECASE),
        "folder": "ptsd-4",
        },
            ]

if __name__ == "__main__":
    # load the things
    outfile = sys.argv[1]

    gzipper(outfile)

    print "complete"
  








