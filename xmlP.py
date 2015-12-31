import xml.etree.ElementTree as ElementTree
s="<program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>s </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>z </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>"
s1="<program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>a </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>b </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>"
et = ElementTree.fromstring(s)
parent_map = dict((c, p) for p in et.getiterator() for c in p)
et1 = ElementTree.fromstring(s1)
parent_map1 = dict((c, p) for p in et1.getiterator() for c in p)
nt="variableStatement"
li= et.findall('.//'+nt)
li1= et1.findall('.//'+nt)

print li

import random

importPlaceholder= random.choice(li)
importPlaceholder1= random.choice(li1)

etTemp = ElementTree.fromstring("<MutationNode> "+nt+" </MutationNode>")

parent = parent_map[importPlaceholder]
index = parent._children.index(importPlaceholder)
parent._children[index] = etTemp

# parent = parent_map1[importPlaceholder1]
# index = parent._children.index(importPlaceholder1)
# parent._children[index] = importPlaceholder

class Test:
	out=""
	def treeToProg(self,root):
	    if root is not None:
	        for child in root:
	            if child.text is not None:
	                self.out+=child.text
	            self.treeToProg(child)   
	            if child.tail is not None:
	                self.out+=child.tail
	    return self.out
t=Test()
print t.treeToProg(et)
# t=Test()
# print t.treeToProg(et1)

# <program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>s </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>b </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>
# <program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>a </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>z </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>