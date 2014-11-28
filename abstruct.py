import networkx as nx

#def main():
#	if __name__== "__main__":


class abstruct:
	def __init__(self,word1):
		self.word1 = word1
		listOfNodes = ['universe','world','earth', 'material', 'immaterial','passion'
		'logic','emotion','mathematics','science','philosophy','existence','hate', 'love']
		self.listOfNodes=listOfNodes

	def print_success(self):
		if (self.word1 in self.listOfNodes):
			return ('Success!')
		else:
			return ('Not a Word')

	def make(self, wordVar):
		#node names
		wordVar = nx.Graph()
		wordVar.add_nodes_from(self.listOfNodes)
		for i in range(len(self.listOfNodes)):
			wordVar.add_edge(wordVar,self.listOfNodes[i], weight = .3)
		return (wordVar.nodes())

x = abstruct('hate')
print x.print_success()
print x.make('hate')
