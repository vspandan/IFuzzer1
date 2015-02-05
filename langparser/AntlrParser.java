import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.HashMap;

import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ParseTree;

class AntlrParser {
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

	public AntlrParser() {
		non_Terminals = new ArrayList<String>();
		m = new HashMap<String, String>();
		identifiers = new ArrayList<String>();
	}

	public String parseTree(String fileName, boolean extractCF) {

		try {
			if (fileName != null)
				lexer = new ECMAScriptLexer(new ANTLRInputStream(
						new FileInputStream(fileName)));
			else
				System.exit(0);
			stream = new CommonTokenStream(lexer);
			parser = new ECMAScriptParser(stream);
			parser.setBuildParseTree(true);
			rules = parser.ruleNames;

			ECMAScriptParser.ProgramContext pContext = parser.program();
			if (pContext.children != null) {
				selectSubtrees(null, pContext.getChild(0), extractCF, false);
			}
			return parseTr;
		} catch (Exception e) {

		}
		return "";
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

	private String retrieveCodeFrag(String pTreeRepr, String nonT, int position) {
		String[] val = pTreeRepr.split(" ");
		int posTrack = 0;
		boolean indicator = false;
		int temp = 0;
		String subcode = "";

		for (String v : val) {

			if (v.contains("<<<")) {
				posTrack = posTrack + 1;
				if (indicator)
					temp = temp + 1;
			}
			if (posTrack == position && !indicator) {
				posTrack = -10000;
				indicator = true;
				temp = temp + 1;
			}
			if (v.contains(">>>"))
				if (indicator)
					temp = temp - 1;

			if (indicator)
				if (!v.contains("<<<"))
					if (!v.contains(">>>")) {
						if (v.equals("."))
							subcode = subcode.trim() + v;
						else if (subcode.length() > 0
								&& subcode.charAt(subcode.length() - 1) == '.')
							subcode = subcode.trim() + v;
						else
							subcode = subcode.trim() + " " + v;
					}

			if (temp == 0 && indicator)
				indicator = false;

		}
		return subcode.trim();
	}

	public HashMap<String, String> extractCodeFrag(String fileName, boolean extractCF) {
		if (fileName == null)
			System.exit(0);
		else
			parseTr = parseTree(fileName, extractCF);

		HashMap<String, String> d = new HashMap<String, String>();

		if (parseTr.length() > 0) {
			int position = 1;
			File f = new File(DEFAULT_DATABASE_PATH);
			if (!f.exists())
				f.mkdirs();

			for (int i = 0; i < non_Terminals.size(); i++) {
				String nt = non_Terminals.get(i);
				String code = retrieveCodeFrag(parseTr, nt, position);
				if (code.length() > 0) {

					d.put(nt, code);
				}
				position += 1;
			}
		}
		return d;
	}

	public static void main(String[] args) {
		AntlrParser a = new AntlrParser();
			System.out.println(a.parseTree(args[0],true));	
	}
}
