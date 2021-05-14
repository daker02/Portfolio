<%@page import="dao.ArtistDAO"%>
<%@page import="vo.ArtistVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

    <%
       request.setCharacterEncoding("utf-8");
       String artist_id = request.getParameter("artist_id");
       String artist_name = request.getParameter("artist_name");
       String artist_birth = request.getParameter("artist_birth");
       String artist_gender = request.getParameter("artist_gender");
       String talent = request.getParameter("talent");
       String agency = request.getParameter("agency");
       
       ArtistVO vo = new ArtistVO();
       vo.setArtist_id(artist_id);
       vo.setArtist_name(artist_name);
       vo.setArtist_birth(artist_birth);
       vo.setArtist_gender(artist_gender);
       vo.setTalent(talent);
       vo.setAgency(agency);
       
       ArtistDAO dao = new ArtistDAO();
       int n = dao.InsertArtist(vo);
       
       if(n > 0 ) {
    	   response.sendRedirect("/view/ArtistList.jsp");
       }else {
    	   %>
    	   <script>
    	   history.back();
    	   </script>
    	   <%
       }
    %>