import cx_Oracle
#한글 지원 방법
import os

class ReviewDao:
    def __init__(self):
        os.putenv('NLS_LANG', '.UTF8')
        
        #연결에 필요한 기본 정보 (유저, 비밀번호, 데이터베이스 서버 주소)
        dsn =cx_Oracle.makedsn('112.220.114.130','1521','xe')
        self.con = cx_Oracle.connect(user="team4_202204F",password="java",dsn=dsn,encoding="UTF-8")
        self.cursor = self.con.cursor()
    #input데이터를 위한 도서 전체 목록가져오기
    def selectBookList(self):
        sql="select book_no from book order by book_no"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
    
    def selectRentNo(self, mem_id):
        sql = f"""
        select rent_no
        from rent
        where mem_id = '{mem_id}' 
        order by rent_no
        """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
    
    def selectBookNo(self, rentNo):
        sql = f"""
        select book_no, rev_grade 
        from review 
        where rent_no = {rentNo} 
        """
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row
    
    def __del__(self):
        self.cursor.close()
        self.con.close()

if __name__ == '__main__':
    reviewArr = []
    bookArr = []
    dao = ReviewDao()
    books = dao.selectBookList()
    for book in books:
        bookArr.append(book[0])
    
    print(bookArr)
    
    #for idx, bookNo in enumerate(bookData):
        
    
    rentNos = dao.selectRentNo("eco")
    for rentNo in rentNos:
        print(rentNo[0])
        bookData = dao.selectBookNo(rentNo[0])
        print(bookData[0])
        
    for book in bookArr:
        if book == bookData[0]:
            if bookData[1] >= 2.5:
                reviewArr.append(1)
        else:
            reviewArr.append(0)
    
    print(len(reviewArr))