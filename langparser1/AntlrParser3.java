import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.HashMap;

import org.antlr.runtime.ANTLRStringStream;
import org.antlr.runtime.ANTLRFileStream;
import org.antlr.runtime.CommonTokenStream;
import org.antlr.runtime.tree.CommonTree;

import py4j.GatewayServer;
import py4j.Py4JNetworkException;
class AParser3{
	boolean timeout ;

	String parseTr = "";
	String[] rules = null;

	HashMap<String, String> m = null;
	ArrayList<String> non_Terminals = null;
	ArrayList<String> identifiers = null;

	ES3Lexer lexer = null;
	CommonTokenStream stream = null;
	ES3Parser parser = null;

	public AParser3() {
		non_Terminals = new ArrayList<String>();
		m = new HashMap<String, String>();
		identifiers = new ArrayList<String>();
		timeout = false;
	}
	public static void main(String s[]){
		AParser3 a = new AParser3();
		System.out.println(a.parseTree("/home/spandan/geinterpreterfuzz/mozillaJSTestSuite/ecma_6/TypedArray/fill.js",false));
	}

	public String parseTree(String input, boolean extractCF) {
		//System.out.println(input);
		//System.out.println(extractCF);
		try 
		{
			if (input != null){
				if (extractCF)
					lexer = new ES3Lexer(new ANTLRStringStream(input));
				else
					lexer = new ES3Lexer(new ANTLRFileStream(input));
			}
			else
				return "";
			stream = new CommonTokenStream(lexer);
			parser = new ES3Parser(stream);

//			parser.setBuildParseTree(true);
//			rules = parser.ruleNames;

			final ES3Parser.program_return ret= parser.program();


			Thread t=new Thread(new Runnable(){
				public void run(){
					CommonTree ast = (CommonTree) ret.tree;
					
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
	private void selectSubtrees(String nonT, CommonTree s, boolean extractCF,
			boolean isIdentifier) {
		try {

			int childCount = s.getChildCount();
			if (childCount > 0) {
/*				String nTerminal = rules[((ParserRuleContext) s).getRuleIndex()];
				parseTr = parseTr + "<" + nTerminal + ">";
				non_Terminals.add(nTerminal);
				if (nTerminal.equals("identifier")) {
					identifiers.add(s.getText());
					isIdentifier = true;
				}
				for (int i = 0; i < childCount; i++)
					selectSubtrees(nonT, s.getChild(i), extractCF, isIdentifier);
				if (nTerminal.equals("sourceElement"))
					parseTr = parseTr + "</" + nTerminal + "> ; ";
				else
					parseTr = parseTr + "</" + nTerminal + ">";
			} else {
				if (isIdentifier && extractCF) {
					parseTr = parseTr + "__id__"+s.getText();
					isIdentifier = false;
				} else {
					parseTr = parseTr + " " + s.getText() + " ";
				}
*/			}
		} catch (Exception e) {
		}
	}
}