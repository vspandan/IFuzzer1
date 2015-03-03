import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.HashMap;

import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ParseTree;

import py4j.GatewayServer;
import py4j.Py4JNetworkException;
class AParser{
	boolean timeout ;

	String parseTr = "";
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
		timeout = false;
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


			Thread t=new Thread(new Runnable(){
				public void run(){
					ECMAScriptParser.ProgramContext pContext = parser.program();
					if (pContext!=null){
						if (pContext.children != null) 
							selectSubtrees(null, pContext.getChild(0), true, false);
					}	
				}
			});
			t.start();
			t.join(5000);//5seconds

			if (t.isAlive()) {
				t.stop();
				timeout=true;
        	}
		} catch (Exception e) {

		}
		finally{
			if (timeout)
				return "";
			return parseTr;
		}
	}

	private void selectSubtrees(String nonT, ParseTree s, boolean extractCF,
			boolean isIdentifier) {
		try {

			int childCount = s.getChildCount();
			if (childCount > 0) {
				String nTerminal = rules[((ParserRuleContext) s).getRuleIndex()];
				parseTr = parseTr + "<" + nTerminal + ">";
				non_Terminals.add(nTerminal);
				if (nTerminal.equals("identifier")) {
					identifiers.add(s.getText());
					isIdentifier = true;
				}
				for (int i = 0; i < childCount; i++)
					selectSubtrees(nonT, s.getChild(i), extractCF, isIdentifier);
				parseTr = parseTr + "</" + nTerminal + ">";
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

	AParser a=null;
	public AParser getParser(){
		a = new AParser();
		return a;
	}

	public void nullify(){
		a=null;
	}

	public static void main(String[] args) {
		AntlrParser a = new AntlrParser();
		try {
    		GatewayServer gatewayServer = new GatewayServer(a); 
    		gatewayServer.start();
			//System.out.println(a.parseTree(args[0],true));	
    	}
    	catch(Py4JNetworkException e){
    		System.out.println("\nJava Bridge Connection Failed, Another instance of java bridge is running. Continue\n");
    	}
    	catch(Exception e){
    	}
	}
}
