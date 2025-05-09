import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {

	public static void main(String[] args) {

		try {

			ServerImpl serverImpl = new ServerImpl();
			LocateRegistry.createRegistry(2000);
			Naming.rebind("rmi://localhost:2000/Server" , serverImpl);

			System.out.println("Server Started....");

		} catch (Exception e) {

			System.out.println("Exception Occurred At Server!" + e.getMessage());
			e.printStackTrace();
		}

	}

}
