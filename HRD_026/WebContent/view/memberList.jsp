<%@page import="vo.MemberVO" %>
<%@page import="dao.MemberDao" %>
<%@page import="java.util.ArrayList" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<%
    MemberDao dao = new MemberDao();
ArrayList<MemberVO> list = dao.memberList();
%>
<jsp:include page="../master/header.jsp"/>

<!-- section -->
<section>
        <div class="container">
                <p class="title">회원목록조회/수정</p>
<%
        if (!list.isEmpty()) {
%>
                  <table>
                          <tr>
                                 <td>회원번호</td>
                                 <td>회원성명</td>
                                 <td>회원전화</td>
                                 <td>회원주소</td>
                                 <td>가입일자</td>
                                 <td>고객등급</td>
                                 <td>거주지역</td>
                          </tr>
<%
       for(MemberVO member : list) {
%>
       <tr>
              <td><a href="/view/memberUpdate.jsp?custno=<%=member.getCustno()%>"><%=member.getCustno() %></a></td>
              <td><%=member.getCustname() %></td>
              <td><%=member.getPhone() %></td>
              <td><%=member.getAddress() %></td>
              <td><%=member.getJoindate() %></td>
              <td><%=member.getGrade() %></td>
              <td><%=member.getCity() %></td>
       </tr>
<%     }
%>       
                  </table>
<%}
 else {%>
 
 <p style="text-align: center"> 등록된 회원 정보가 없습니다.</p>
<%
       }
%>
        </div>
</section>
<!-- section -->

<jsp:include page="../master/footer.jsp"/>
</body>
</html>