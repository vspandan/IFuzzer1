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
class AParser2{
	boolean timeout ;

	String parseTr = "";
	String[] rules = null;

	HashMap<String, String> m = null;
	ArrayList<String> non_Terminals = null;
	ArrayList<String> identifiers = null;

	ECMAScript1Lexer lexer = null;
	CommonTokenStream stream = null;
	ECMAScript1Parser parser = null;

	public AParser2() {
		non_Terminals = new ArrayList<String>();
		m = new HashMap<String, String>();
		identifiers = new ArrayList<String>();
		timeout = false;
	}
	public static void main(String s[]){
		AParser2 a = new AParser2();
		System.out.println(a.parseTree("/home/spandan/geinterpreterfuzz/mozillaJSTestSuite/ecma_6/TypedArray/fill.js",false));
	}

	public String parseTree(String input, boolean extractCF) {
		//System.out.println(input);
		//System.out.println(extractCF);
		try 
		{
			if (input != null){
				if (extractCF)
					lexer = new ECMAScript1Lexer(new ANTLRInputStream(input));
				else
					lexer = new ECMAScript1Lexer(new ANTLRInputStream(
						new FileInputStream(input)));
			}
			else
				return "";
			stream = new CommonTokenStream(lexer);
			parser = new ECMAScript1Parser(stream);

			parser.setBuildParseTree(true);
			rules = parser.ruleNames;

			final ECMAScript1Parser.ProgramContext pContext[]= new ECMAScript1Parser.ProgramContext [1];


			Thread t=new Thread(new Runnable(){
				public void run(){
					ECMAScript1Parser.ProgramContext pContext = parser.program();
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
				/*if (nTerminal.equals("stat"))
					parseTr = parseTr + "</" + nTerminal + "> ; ";
				else
				*/	parseTr = parseTr + "</" + nTerminal + ">";
			} else {
				if (isIdentifier && extractCF) {
					parseTr = parseTr + "__id__"+s.getText();
					isIdentifier = false;
				} else {
					parseTr = parseTr + " " + s.getText() + " ";
				}
			}
		} catch (Exception e) {
		}
	}
}