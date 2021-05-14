package common;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DBUtils {

	public static Connection getConnection() {
		Connection con = null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe", "hr", "hr");
		} catch (Exception e) {
			e.printStackTrace();
		}
		return con;
	}

	public static void close(Connection conn, PreparedStatement ps, ResultSet rs) {
		if (rs != null) {
			try {
				rs.close();
			} catch (Exception e) {
				System.out.println("오류 발생 : " + e);
			}
		}
		close(conn, ps);
	}

	public static void close(Connection conn, PreparedStatement ps) {
		if (ps != null) {
			try {
				ps.close();
			} catch (Exception e) {
				System.out.println("오류 발생 : " + e);
			}
		}

		if (conn != null) {
			try {
				conn.close();
			} catch (Exception e) {
				System.out.println("오류 발생 : " + e);
			}
		}
	}

}
