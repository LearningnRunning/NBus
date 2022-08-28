import pymysql
from member.vo import Member

#Dao
class MemberDao:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1234', db='javawork', charset='utf8')

    def disconn(self):
        self.conn.close()

    # 추가 메서드
    def insert(self, a:Member):
        #1. db 커넥션 수립
        self.connect()

        # 2. 사용할 cursor객체 생성. db 작업 메서드가 이 클래스에 정의되어 있으므로 꼭 필요.
        cursor = self.conn.cursor()

        # 3. 실행할 sql문 정의
        sql = 'insert into member(id, pwd, name,email) values(%s, %s, %s, %s)'

        # 4. sql 문에 %s를 사용했다면 각 자리에 들어갈 값을 튜플로 정의
        d = (a.id, a.pwd, a.name,a.email)

        # 5. sql 실행(실행할 sql, %s매칭한 튜플)
        cursor.execute(sql, d)

        # 6. 쓰기동작(insert, update, delete) 에서 쓰기 완료
        self.conn.commit()

        # db 커넥션 끊음
        self.disconn()

        # 검색 메서드
    def select(self, id:str):
        try:
            self.connect()#db연결
            cursor=self.conn.cursor() # 사용할 커서 객체 생성
            sql = 'select*from member where id=%s'
            d=(id,) #(O,) 튜플로 만들기 ',' 없으면 그냥 문자열로 된다.
            cursor.execute(sql, d) #sql 실행
            row = cursor.fetchone() # fetchone() : 현재 커서 위치의 한 줄 추출
            if row:
                return Member(row[0],row[1],row[2],row[3])

        except Exception as e:
            print(e)
        finally:
            self.disconn()



    def selectByName(self, name:str): #name 기준 검색, 여러개 검색
        res=[]
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select*from member where name like %s' # like 활용
            d = (name,)
            cursor.execute(sql, d)  # sql 실행
            res =[Member(row[0], row[1], row[2], row[3]) for row in cursor]
            # for row in cursor:
            #     res.append(Addr(row[0], row[1], row[2], row[3]))
            return res

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    # 삭제(name)
    def delete(self, id:str):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'delete from member where id = %s'
            d = (id,)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()

            return print('삭제가 완료되었습니다.')

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def update(self, a:Member):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'update member set pwd=%s, name=%s,email=%s where id = %s'

            d = (a.pwd,a.name,a.email,a.id)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()

            return print('수정이 완료되었습니다.')

        except Exception as e:
            print(e)
        finally:
            self.disconn()



