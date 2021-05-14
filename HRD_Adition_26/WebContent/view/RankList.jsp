<%@page import="vo.PointVO"%>
<%@page import="java.util.ArrayList"%>
<%@page import="dao.ArtistDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ include file="/master/header.jsp"%>

<section>
	<div class="container">
		<p class="title">참가자 등수 조회</p>
	</div>
</section>

<%
      ArtistDAO dao = new ArtistDAO();
      ArrayList<PointVO> list = dao.getPointList();
      if (!list.isEmpty()) {
%>

<<table>
  <tr>
    <td>참가번호</td>
    <td>참가자명</td>
    <td>점수</td>
    <td>평균</td>
    <td>순위</td>
  </tr>
  <%
       for(PointVO vo : list) {
  %>
  <tr>
    <td><%= vo.getArtist_id() %></td>
    <td><%= vo.getArtist_name() %></td>
    <td><%= vo.getSum() %></td>
    <td><%= vo.getAvg() %></td>
    <td><%= vo.getRank() %></td>
  </tr>
  
  <%
       }
      }
  %>
</table>



<%@ include file="/master/footer.jsp"%>