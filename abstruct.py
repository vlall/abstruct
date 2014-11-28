import networkx as nx

'''
This dictionary of nodes contains all of the weighted keys and values
of every relevant definition node for a given word. The purpose of this is to connect
a specific word to its abstract definition. This definition is best
described as the group of words which are associated with word x's

'''
class abstruct:
	def __init__(self,word1):
		self.word1 = word1
		dictOfNodes = {'universe':'.3','world':'.3','earth':'.3', 'material':'.3', 'immaterial':'.3','passion':'.3',
		'logic':'.3','emotion':'.3','mathematics':'.3','science':'.3','philosophy':'.3','existence':'.3','hate':'.3', 'love':'.2'}
		listOfNodes = dictOfNodes.keys()
		listOfValues = dictOfNodes.values()
		self.listOfNodes=listOfNodes
		self.listOfValues=listOfValues

	def print_success(self):
		if (self.word1 in self.listOfNodes):
			return ('Success!')
		else:
			return ('Not a Word')

	def make(self, wordVar):
		#node names
		wordVar = nx.Graph()
		wordVar.add_nodes_from(self.listOfNodes)
		weightNum = self.listOfValues
		print weightNum
		for i in range(len(self.listOfNodes)):
			wordVar.add_edge(wordVar,self.listOfNodes[i], weight = weightNum[i])
		return (wordVar.nodes())

x = abstruct('hate')
print x.print_success()
print x.make('hate')
