package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import common.JdbcUtil;
import vo.ArtistVO;
import vo.MentoVO;
import vo.PointVO;

public class ArtistDAO {
	public ArrayList<ArtistVO> getArrayList() {
		ArrayList<ArtistVO> list = new ArrayList<ArtistVO>();
		
		Connection conn = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		
		try {
			conn = JdbcUtil.getConnection();
			ps = conn.prepareStatement("select artist_id, artist_name, artist_birth, decode(artist_gender, 'M','남','F','여') artist_gender, decode(talent, '1','보컬','2','댄스','3','랩') talent, agency from tbl_artist_201905");
			rs = ps.executeQuery();
			
			while (rs.next()) {
				ArtistVO vo = new ArtistVO();
				vo.setArtist_id(rs.getString("artist_id"));
				vo.setArtist_name(rs.getString("artist_name"));
				vo.setArtist_birth(rs.getString("artist_birth"));
				vo.setArtist_gender(rs.getString("artist_gender"));
				vo.setTalent(rs.getString("talent"));
				vo.setAgency(rs.getString("agency"));
				list.add(vo);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			JdbcUtil.close(conn, ps, rs);
		}
		return list;
	}
	
	public ArrayList<MentoVO> getmentoList(){
		ArrayList<MentoVO> list = new ArrayList<MentoVO>();
		Connection conn = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		
		try {
			conn = JdbcUtil.getConnection();
			ps = conn.prepareStatement("select A.artist_id, A.artist_name, A.artist_birth, C.point, C.point grade, B.mento_name from tbl_artist_201905 A, tbl_mento_201905 B, tbl_point_201905 C where A.artist_id = C.artist_id and C.mento_id = B.mento_id");
			rs = ps.executeQuery();
			
			while(rs.next()) {
				MentoVO vo = new MentoVO();
				vo.setArtist_id(rs.getString("artist_id"));
				vo.setArtist_name(rs.getString("artist_name"));
				vo.setArtist_birth(rs.getString("artist_birth"));
				vo.setPoint(rs.getInt("point"));
				vo.setGrade(rs.getInt("grade"));
				vo.setMento_name(rs.getString("mento_name"));
				list.add(vo);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			JdbcUtil.close(conn, ps, rs);
		}
		return list;
	}
	
	public ArrayList<PointVO> getPointList(){
		ArrayList<PointVO> list = new ArrayList<PointVO>();
		Connection conn = null;
		PreparedStatement ps = null;
		ResultSet rs = null;
		
		try {
			conn = JdbcUtil.getConnection();
			ps = conn.prepareStatement("select A.artist_id, artist_name, sum(point) sum, round(avg(point),2) avg, rank() over(order by sum(point) desc) rank from tbl_artist_201905 A, tbl_point_201905 P where A.artist_id = P.artist_id group by (A.artist_id, artist_name) order by rank asc");
			rs = ps.executeQuery();
			
			while(rs.next()) {
				PointVO vo = new PointVO();
				vo.setArtist_id(rs.getString("artist_id"));
				vo.setArtist_name(rs.getString("artist_name"));
				vo.setSum(rs.getInt("sum"));
				vo.setAvg(rs.getInt("avg"));
				vo.setRank(rs.getInt("rank"));
				list.add(vo);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			JdbcUtil.close(conn, ps, rs);
		}
		return list;
	}
	
	public int InsertArtist(ArtistVO vo) {
		int n = 0;
		Connection conn = null;
		PreparedStatement ps = null;
		
		try {
			conn = JdbcUtil.getConnection();
			ps = conn.prepareStatement("insert into tbl_artist_201905 values(?,?,?,?,?,?)");
			ps.setString(1, vo.getArtist_id());
			ps.setString(2, vo.getArtist_name());
			ps.setString(3, vo.getArtist_birth());
			ps.setString(4, vo.getArtist_gender());
			ps.setString(5, vo.getTalent());
			ps.setString(6, vo.getAgency());
			n = ps.executeUpdate();
			
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			JdbcUtil.close(conn, ps);
		}
		return n;
	}
}
