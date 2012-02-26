
class Node(object):
    parent = None
    value = None
    children={}#contains a map with child characters as keys and their Node as values


class Trie(object):

    root = Node()
    root.value = "/" 
       
    def addWord(self,word):
        currentNode = self.root
        i = 0
        print "adding word '"+ word+"' to trie "
        for c in word:
            print "adding character " + c
            try:
                currentNode = currentNode.children[c]
		print "character "+c + " exists"
            except:
                self.createSubTree(word[i:len(word)],currentNode)
                break
            i = i + 1
                
            
    def addCharacter(self,c,children):
        i =0;
        for existingc in children:
            if existingc > c:
                children.insert(i,c)
                break
            i=i+1
           
 
    def createSubTree(self,word,node):
        print "creating subtree for " + word
        currentNode = node
        for c in word:
            currentNode.children[c] = Node()
            currentNode.children[c].value = c
            currentNode.children[c].parent = currentNode
	    currentNode.children[c].children = None
            currentNode = currentNode.children[c]
                         
    def printTree(self):
        currentNode = self.root
        while True:
		print currentNode.children
        	for n in currentNode.children:
        		print n.value

trie = Trie()
trie.addWord("w")
trie.addWord("wo")
#trie.printTree()
