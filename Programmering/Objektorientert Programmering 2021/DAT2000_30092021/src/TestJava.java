import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class TestJava {
	private final String url = "jdbc:postgresql://localhost/dvdrental";
	private final String user = "postgres";
	private final String password ="loltehelf";
	
	public Connection connect() throws SQLException {
		return DriverManager.getConnection(url, user, password);
	}


public TestJava() {
	// TODOAuto-generated constructor stub}
	}
	
	public static void main(String[] args) {
		// TODOAuto-generated method stub
		//System.out.println("HellowWorld");
		TestJava t= new TestJava();
		try {
			t.connect();
			System.out.println("Connected to the PostgreSQL server successfully.");
		} catch(SQLException e)  {
			// TODOAuto-generated catch block
			e.printStackTrace();
		}
	}
}

