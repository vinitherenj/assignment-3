#Roll no. 33 and 45

from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer

fp = open('NaMo.txt','r')

text = fp.read()
text = text.lower()

sno = SnowballStemmer('english')
sent_list = sent_tokenize(text)

stop_words = list(stopwords.words('english'))
stop_words.append('.')
stop_words.append('"')
stop_words.append("'")
stop_words.append("''")
stop_words.append(',')
stop_words.append('``')
stop_words.append('`')
stop_words.append('--')
stop_words.append('(')
stop_words.append(')')
stop_words.append('[')
stop_words.append(']')
stop_words.append('{')
stop_words.append('}')
stop_words.append('$')
stop_words.append('#')
stop_words.append('*')
stop_words.append('^')
stop_words.append('@')
stop_words.append("'s")

after_stopping = []

for i in sent_list:
	word_tokens = word_tokenize(i)
	sent_stop = []
	for w in word_tokens:
		
		if (w not in stop_words):
			word = sno.stem(w)
			sent_stop.append(str(word))			### testing edit
		###hey there
	after_stopping.append(sent_stop)
	
sim_matrix = [[0]*len(sent_list) for i in range(len(sent_list))]
