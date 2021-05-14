CREATE TABLE tbl_artist_201905(
artist_id char(4) NOT NULL,
artist_name varchar2(20),
artist_birth char(8),
artist_gender char(1),
talent char(1),
agency varchar2(20)
);

drop table tbl_artist_201905;


select artist_id,artist_name,artist_birth,decode(artist_gender,'M','남자','F','여자') artist_gender,decode(talent,'1','보컬','2','댄스','3','랩') talent,agency from tbl_artist_201905
INSERT INTO TBL_ARTIST_201905 (artist_id, artist_name,
artist_birth, artist_gender, talent, agency)
VALUES ('A001', '황스타', '19970101', 'F', '1', 'A엔터테인먼트');
INSERT INTO TBL_ARTIST_201905 (artist_id, artist_name,
artist_birth, artist_gender, talent, agency)
VALUES ('A002', '정스타', '19980201', 'M', '2', 'B엔터테인먼트');
INSERT INTO TBL_ARTIST_201905 (artist_id, artist_name,
artist_birth, artist_gender, talent, agency)
VALUES ('A003', '박스타', '19990301', 'M', '3', 'C엔터테인먼트');
INSERT INTO TBL_ARTIST_201905 (artist_id, artist_name,
artist_birth, artist_gender, talent, agency)
VALUES ('A004', '김스타', '20000401', 'M', '1', 'D엔터테인먼트');
INSERT INTO TBL_ARTIST_201905 (artist_id, artist_name,
artist_birth, artist_gender, talent, agency)
VALUES ('A005', '서스타', '20010501', 'F', '2', 'E엔터테인먼트');


CREATE TABLE tbl_mento_201905(
mento_id char(4) NOT NULL,
mento_name varchar2(20)
);


INSERT INTO TBL_MENTO_201905 (mento_id, mento_name)
VALUES ('J001', '이멘토');
INSERT INTO TBL_MENTO_201905 (mento_id, mento_name)
VALUES ('J002', '안멘토');
INSERT INTO TBL_MENTO_201905 (mento_id, mento_name)
VALUES ('J003', '한멘토');


CREATE TABLE tbl_point_201905(
serial_no char(4) NOT NULL,
artist_id char(4),
mento_id char(4),
point number(3)
);


drop table tbl_artist_201905;
drop table tbl_mento_201905;
drop table tbl_point_201905;

INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P001', 'A001', 'J001', 84);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P002', 'A001', 'J002', 82);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P003', 'A001', 'J003', 86);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P004', 'A002', 'J001', 98);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P005', 'A002', 'J002', 99);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P006', 'A002', 'J003', 100);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P007', 'A003', 'J001', 23);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P008', 'A003', 'J002', 43);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P009', 'A003', 'J003', 34);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P010', 'A004', 'J001', 67);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P011', 'A004', 'J002', 56);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P012', 'A004', 'J003', 89);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P013', 'A005', 'J001', 3);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P014', 'A005', 'J002', 6);
INSERT INTO tbl_point_201905 (serial_no, artist_id, mento_id, point)
VALUES ('P015', 'A005', 'J003', 9);


select * from tbl_artist_201905;

select A.artist_id , A.artist_name,A.artist_birth,C.point,C.point,B.mento_name 
from tbl_artist_201905 A,TBL_MENTO_201905 B,tbl_point_201905 C where A.artist_id = C.artist_id and C.mento_id = B.mento_id;


select  A.artist_id ,artist_name, sum(point) sum, round(avg(point),2) avg,rank() over(order by sum(point) desc) rank
from tbl_artist_201905 A, tbl_point_201905 P where A.artist_id = P.artist_id group by (A.artist_id ,artist_name ) order by rank  asc;

drop table tbl_artist_201905;
drop table tbl_mento_201905;
drop table tbl_point_201905;