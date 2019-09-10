import re
from collections import Counter

def read_corpus(corpus_file):
	unigram = []
	bigram = []
	with open(corpus_file, "r", encoding="utf-8") as reader:
		for line in reader.readlines():
			line = preprocess(line)
			unigram += find_unigram(line)
			bigram += find_bigram(line)
	# save(Counter(unigram))
	# save(Counter(bigram))
	return Counter(unigram), Counter(bigram)

def save(counter, dir):
	with open(dir, "w+", encoding="utf-8") as writer:
		for k, v in counter.items():
			writer.write(str(k) + " " + str(v) + "\n")
	print("Saved")

def find_unigram(text):
	return re.findall("\w+", text)

def find_bigram(text):
	bigram = []
	unigram = find_unigram(text)
	for i in range(len(unigram) - 1):
		bigram.append(unigram[i] + " " + unigram[i+1])
	return bigram

def preprocess(text):
	text = text.lower()
	text = re.sub(r"^@@[1-9]{4}\s", "", text)
	return text

if __name__ == "__main__":

	unigram, bigram = read_corpus("data/text.txt")
	print("Succeed")
	# save(unigram, dir="data/count_1w.txt")
	# save(bigram, dir="data/count_2w.txt")
	print(unigram.most_common(10))