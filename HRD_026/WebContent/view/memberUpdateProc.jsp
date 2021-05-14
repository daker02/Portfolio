<%@page import="java.sql.Date" %>
<%@page import="dao.MemberDao" %>
<%@page import="vo.MemberVO" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
               //피라미터 추출
               request.setCharacterEncoding("UTF-8");
               int custno = Integer.parseInt(request.getParameter("custno"));
               String custname = request.getParameter("custname");
               String phone = request.getParameter("phone");
               String address = request.getParameter("address");
               Date joindate = Date.valueOf(request.getParameter("joindate"));
               String grade = request.getParameter("grade");
               String city = request.getParameter("city");
               
               //VO객체에 데이터 바인딩
               MemberVO member = new MemberVO();
               member.setCustno(custno);
               member.setCustname(custname);
               member.setPhone(phone);
               member.setAddress(address);
               member.setJoindate(joindate);
               member.setGrade(grade);
               member.setCity(city);
               
               //DB에 반영
               MemberDao dao = new MemberDao();
               int n = dao.memberUpdate(member);
               
               //화면 이동
               if(n > 0) {
            	   response.sendRedirect("/view/memberList.jsp");
               }
               else {
%>
               <script>
                       history.back();
               </script>
<%
               }
%>
</body>
</html>