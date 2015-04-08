import py4j.GatewayServer;
import py4j.Py4JNetworkException;

class AntlrParser {

	CodeFragmentExtractor c=null;
	static GatewayServer gatewayServer = null;

	public void nullify(){
	}

	public void restartServer(){
		try {
			gatewayServer.shutdown();
			AntlrParser a = new AntlrParser();

    		gatewayServer = new GatewayServer(a); 
    		gatewayServer.start(true);
			//System.out.println(a.parseTree(args[0],true));	
    	}
    	catch(Py4JNetworkException e){
    		System.out.println("\nError in restarting gateway server\n");
    	}
    	catch(Exception e){
    	}
	}
	public CodeFragmentExtractor getCodeFragmentExtractor(){
		if (c!=null)
			c=null;
		c= new CodeFragmentExtractor();
		return c;
	}

	public static void main(String[] args) {
		AntlrParser a = new AntlrParser();
		try {
    		gatewayServer = new GatewayServer(a); 
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
