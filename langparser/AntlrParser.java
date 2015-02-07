import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.HashMap;

import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ParseTree;

import py4j.GatewayServer;
class AParser{
	int DEFAULT_SCORE = 0;
	int count = 0;
	int pos = 0;

	boolean pri = false;

	String parseTr = "";
	String DEFAULT_FILE = "temp";
	String DEFAULT_DATABASE_PATH = "database";
	String[] rules = null;

	HashMap<String, String> m = null;
	ArrayList<String> non_Terminals = null;
	ArrayList<String> identifiers = null;

	ECMAScriptLexer lexer = null;
	CommonTokenStream stream = null;
	ECMAScriptParser parser = null;

	public AParser() {
		non_Terminals = new ArrayList<String>();
		m = new HashMap<String, String>();
		identifiers = new ArrayList<String>();
	}

	public String parseTree(String input, boolean extractCF) {
		//System.out.println(input);
		//System.out.println(extractCF);
		try 
		{
			if (input != null){
				if (extractCF)
					lexer = new ECMAScriptLexer(new ANTLRInputStream(input));
				else
					lexer = new ECMAScriptLexer(new ANTLRInputStream(
						new FileInputStream(input)));
			}
			else
				return "";
			stream = new CommonTokenStream(lexer);
			parser = new ECMAScriptParser(stream);

			parser.setBuildParseTree(true);
			rules = parser.ruleNames;

			final ECMAScriptParser.ProgramContext pContext[]= new ECMAScriptParser.ProgramContext [1];


			Thread t=new Thread(){
				public void run(){
					pContext[0] = parser.program();
				}
			};
			t.start();
			t.join(20000);
			if (t.isAlive()) {
         		t.stop();
        	}
			if (pContext[0]!=null){
				if (pContext[0].children != null) 
					selectSubtrees(null, pContext[0].getChild(0), true, false);
			}
			
		} catch (Exception e) {

		}
		finally{
			return parseTr;
		}
	}

	private void selectSubtrees(String nonT, ParseTree s, boolean extractCF,
			boolean isIdentifier) {
		try {
			int childCount = s.getChildCount();
			if (childCount > 0) {
				String nTerminal = rules[((ParserRuleContext) s).getRuleIndex()];
				parseTr = parseTr + "<<<" + nTerminal + ": ";
				non_Terminals.add(nTerminal);
				if (nTerminal.equals("identifier")) {
					identifiers.add(s.getText());
					isIdentifier = true;
				}
				for (int i = 0; i < childCount; i++)
					selectSubtrees(nonT, s.getChild(i), extractCF, isIdentifier);
				parseTr = parseTr + " >>> ";
			} else {
				if (isIdentifier && extractCF) {
					parseTr = parseTr + "__id__"+s.getText();
					isIdentifier = false;
				} else {
					parseTr = parseTr + s.getText() + " ";
				}
			}
		} catch (Exception e) {

		}
	}
}

class AntlrParser {
	public AParser getParser(){
		return new AParser();
	}


	public static void main(String[] args) {
		AntlrParser a = new AntlrParser();
    	GatewayServer gatewayServer = new GatewayServer(a); 
    	gatewayServer.start();
		//System.out.println(a.parseTree(args[0],true));	
	}
}
