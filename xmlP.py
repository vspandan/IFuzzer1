import xml.etree.ElementTree as ElementTree
s="<program><statementListItem><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&quot;1&quot; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><assignmentOperator>&lt;&lt;= </assignmentOperator><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>undefined </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression></assignmentExpression>if ( <expression><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>!== <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>1 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></expression>) </assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><block>{ <statementList><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><callExpression><memberExpression><primaryExpression><identifierName>$ERROR </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&apos;#1: x = &quot;1&quot;; x &lt;&lt;= undefined; x === 1. Actual: &apos; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>+ <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression>( <expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></expression>) </primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments><eos>; </eos></callExpression></leftHandSideExpression></conditionalExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementList>} </block></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>undefined </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><assignmentOperator>&lt;&lt;= </assignmentOperator><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&quot;1&quot; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression></assignmentExpression>if ( <expression><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>!== <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>0 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></expression>) </assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><block>{ <statementList><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><callExpression><memberExpression><primaryExpression><identifierName>$ERROR </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&apos;#2: x = undefined; x &lt;&lt;= &quot;1&quot;; x === 0. Actual: &apos; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>+ <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression>( <expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></expression>) </primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments><eos>; </eos></callExpression></leftHandSideExpression></conditionalExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementList>} </block></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression>new <memberExpression><primaryExpression><identifierName>String </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&quot;1&quot; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><assignmentOperator>&lt;&lt;= </assignmentOperator><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>undefined </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression></assignmentExpression>if ( <expression><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>!== <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>1 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></expression>) </assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><block>{ <statementList><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><callExpression><memberExpression><primaryExpression><identifierName>$ERROR </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&apos;#3: x = new String(&quot;1&quot;); x &lt;&lt;= undefined; x === 1. Actual: &apos; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>+ <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression>( <expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></expression>) </primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments><eos>; </eos></callExpression></leftHandSideExpression></conditionalExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementList>} </block></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>undefined </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><expressionStatement><expression><assignmentExpression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><assignmentOperator>&lt;&lt;= </assignmentOperator><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression>new <memberExpression><primaryExpression><identifierName>String </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&quot;1&quot; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments></memberExpression></newExpression></leftHandSideExpression></conditionalExpression><eos>; </eos></assignmentExpression></assignmentExpression>if ( <expression><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>!== <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>0 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></expression>) </assignmentExpression></expression></expressionStatement></statement></statementListItem><statementListItem><statement><block>{ <statementList><statement><expressionStatement><expression><assignmentExpression><conditionalExpression><leftHandSideExpression><callExpression><memberExpression><primaryExpression><identifierName>$ERROR </identifierName></primaryExpression></memberExpression><arguments>( <argumentList><assignmentExpression><conditionalExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal>&apos;#4: x = undefined; x &lt;&lt;= new String(&quot;1&quot;); x === 0. Actual: &apos; </literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression>+ <conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression>( <expression><assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><identifierName>x </identifierName></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></expression>) </primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></conditionalExpression></assignmentExpression></argumentList>) </arguments><eos>; </eos></callExpression></leftHandSideExpression></conditionalExpression><eos></eos></assignmentExpression></expression></expressionStatement></statement></statementList>} </block></statement></statementListItem></program>"
s1="<program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>a </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>b </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>"
et = ElementTree.fromstring(s)
parent_map = dict((c, p) for p in et.getiterator() for c in p)
et1 = ElementTree.fromstring(s1)
parent_map1 = dict((c, p) for p in et1.getiterator() for c in p)
nt="assignmentExpression"
li= et.findall('.//'+nt)
# li1= et1.findall('.//'+nt)

print li

# import random

# importPlaceholder= random.choice(li)
# importPlaceholder1= random.choice(li1)

# etTemp = ElementTree.fromstring("<MutationNode> "+nt+" </MutationNode>")

# parent = parent_map[importPlaceholder]
# index = parent._children.index(importPlaceholder)
# parent._children[index] = etTemp

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
class ProgramGen:
    def __init__(self):
        self.out=""

    def treeToProg(self,root):
        if root is not None:
            if root.text is not None:
                self.out+=root.text
            for child in root:
                self.treeToProg(child)   
            if root.tail is not None:
                self.out+=root.tail
        return self.out   
t=Test()
# print t.treeToProg(et)
for importPlaceholder in li:
	t=Test()
	print t.treeToProg(importPlaceholder)
	print "\n"

# t=Test()
# print t.treeToProg(et1)

# <program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>s </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>b </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>
# <program><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>a </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem><statementListItem><statement><variableStatement>var <variableDeclarationList><variableDeclaration><identifierBinding><identifierReference><identifierName>z </identifierName></identifierReference></identifierBinding><initialiser>= <assignmentExpression><conditionalExpression><leftHandSideExpression><newExpression><memberExpression><primaryExpression><literal><numericLiteral>100 </numericLiteral></literal></primaryExpression></memberExpression></newExpression></leftHandSideExpression></conditionalExpression></assignmentExpression></initialiser></variableDeclaration></variableDeclarationList></variableStatement></statement></statementListItem><statementListItem><statement><emptyStatement>; </emptyStatement></statement></statementListItem></program>