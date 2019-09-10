from math import log
from collections import Counter

def memo(f):
    "Memoize function f, whose args must all be hashable."
    cache = {}
    def fmemo(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    fmemo.cache = cache
    return fmemo

def product(nums):
	result = 1
	for x in nums:
		result *= x
	return result

def load(corpus):
	c = Counter()
	with open(corpus, "r", encoding="utf-8") as loader:
		for line in loader.readlines():
			line = line.replace("\n", "")
			line_list = line.split()
			c[" ".join(line_list[:-1])] = int(line_list[-1])
	return c

def P(word):
	return unigram[word]/ sum(unigram.values())

def Pwords(word):
	return product(P(w) for w in word)

def splits(text):
	return [(text[:i+1], text[i+1:]) for i in range(len(text))]

@memo
def segment(text):
	if not text:
		return []
	candidates = ([first] + segment(res) for first, res in splits(text))
	return max(candidates, key=Pwords)

unigram = load("data/count_1w.txt")
bigram = load("data/count_2w.txt")

print(segment("iwanttoeatenglishfood"))