import networkx as nx

def main():
	if __name__== "__main__":
		make('hate')


class abstruct:
	def __init__(self, word1):
		listOfNodes = ['universe','world','earth', 'material', 'immaterial','passion'
		'logic','emotion','mathematics','science','philosophy','existence','hate', 'love']
		if (word1 in listOfNodes):
			return ('Success!')
		else:
			return ('Not a Word')

	def make(wordVar):
		#node names
		wordVar = nx.Graph()
		wordVar.add_nodes_from(listOfNodes)
		wordVar.add_edge('logic','subject', weight = .3)
		print (wordVar.nodes())


x = abstruct('hate')
