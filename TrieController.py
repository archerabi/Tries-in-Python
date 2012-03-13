from Trie import *
from view import *
class TrieController():
	def __init__(self):
		self.trie = Trie()
		self.initTrie()
		self.view = TrieDemoView()
		self.view.textEntered.connect(self.handleTextChanged)

	def handleTextChanged(self,stringEntered):
		if len (stringEntered)==0:
			return
		print "word list for " + stringEntered
		text = ""
		for word in  self.trie.getWordList(str(stringEntered)):
			text += word + "\n"
		self.view.setSuggestions(text)

	def initTrie(self):
		f = open("words.txt",'r')
		i = 0
		for line in f:
			self.trie.addWord(line)
			i+=1
		print "added " + str(i) + " words"

	def getView(self):
		return self.view
