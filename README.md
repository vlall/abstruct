abstruct
========
**high-priority project undergoing work**

##What is abstruct?
Abstruct is a machine learning library that will utilize numerous aspects of AI using Python.

Basic Components:

####1. Structure Function:
List the words, find the elements in the sentence and create models of the relationships between these elements.

Divides into sentence structure:
- who 
- what 
- when
- where 
- *why*: Curiosity is key 
- how

####2. Synonyms, Antonyms
Each retrieval has a weighted accuracy to the word it’s referring to. The beauty of abstract is the plasticity of the network. Each response also as a weighted value in relation to the input word. This weight changes given on the machine learning algorithm implemented later. Weighted values can also be applied to neural network structures later.

Example using artibrary weights:
```
synonym(word, degree of abstraction)
	#Synonym normal
synonym(guy, 0) = man (.9)
	#Up to a superset
synonym(guy, -1) = human (.8) || person (.8)
	#Down to a subset
synonym(guy, +1) = boy (.85) || senior (.3)||
	#Inverse normal
antonym(guy, 0)	= woman
	#Inverse superset
antonym(guy, -1) = inhuman(.9) || creature(.5) 
	Inverse subset
antonym(guy, +1) = girl (.85)
	
```

```
if (degree > 0)
	# abstraction is more specific 
if (degree < 0 )
	# abstraction is more broad
```

####3. Abstraction via Abduction and Induction
  Fundamental to the AI aspect of interpreting the NLP data
	
	
