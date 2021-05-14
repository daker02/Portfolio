package common;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class JdbcUtil {
	public static Connection getConnection() {
		Connection conn = null;
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			conn = DriverManager.getConnection

			("jdbc:oracle:thin:@localhost:1521:xe", "hr", "hr");

		} catch (Exception e) {
			e.printStackTrace();
		}
		return conn;
	}

	public static void close(Connection conn, PreparedStatement pstmt, ResultSet rs) {
		if (rs != null) {
			try {
				rs.close();
			} catch (SQLException e) { // 오류메시지출력 (내용생략) }
			}
		}
		close(conn, pstmt);
	}

	public static void close(Connection conn, PreparedStatement pstmt) {
		if (pstmt != null) {
			try {
				pstmt.close();
			} catch (SQLException e) { // 오류메시지출력 }
			}
		}
		if (conn != null) {
			try {
				conn.close();
			} catch (SQLException e) { // 오류메시지출력 }
			}
		}
	}
}