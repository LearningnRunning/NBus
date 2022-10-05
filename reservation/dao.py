import pymysql
from reservation.vo import Reserve

#Dao
class ReserveDao:
    def __init__(self):
        print("reserve dao")
        self.conn = None

    def connect(self):
        print("reserve connect")
        self.conn = pymysql.connect(host='localhost', user='root', password='12345678', db='Nbus', charset='utf8')

    def disconn(self):
        print("reserve disconnect")
        self.conn.close()

    # 추가 메서드
    def insert(self, a:Reserve):
        #1. db 커넥션 수립
        self.connect()
        print("insert connect")

        # 2. 사용할 cursor객체 생성. db 작업 메서드가 이 클래스에 정의되어 있으므로 꼭 필요.
        cursor = self.conn.cursor()
        print("insert cursor")

        # 3. 실행할 sql문 정의
        sql = 'insert into reserve(reserve, id, arrmsg, rtNm, plainNo, stNm, stNmD, reserve, etc) ' \
              'values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        print("insert sql")

        # 4. sql 문에 %s를 사용했다면 각 자리에 들어갈 값을 튜플로 정의
        d = (a.reservenum, a.id, a.arrmsg, a.rtNm, a.plainNo, a.stNm, a.stNmD, a.reserve, a.etc)
        print(d)

        # 5. sql 실행(실행할 sql, %s매칭한 튜플)
        cursor.execute(sql, d)
        print("insert execute")

        # 6. 쓰기동작(insert, update, delete) 에서 쓰기 완료
        self.conn.commit()
        print("insert commit")

        # db 커넥션 끊음
        self.disconn()
        print("insert disconn")

        # 검색 메서드
    def select(self, id:str):
        try:
            print("select")
            self.connect()#db연결
            cursor=self.conn.cursor() # 사용할 커서 객체 생성
            sql = 'select*from reserve where id=%s'
            print("select serach")
            d=(id,) #(O,) 튜플로 만들기 ',' 없으면 그냥 문자열로 된다.
            print("select", d)
            cursor.execute(sql, d) #sql 실행
            row = cursor.fetchone() # fetchone() : 현재 커서 위치의 한 줄 추출
            if row:
                print(row)
                return Reserve(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8])

        except Exception as e:
            print(e)
        finally:
            self.disconn()



    def selectById(self, id:str): #id 기준 검색, 여러개 검색
        res=[]
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'select*from reserve where id like %s' # like 활용
            d = (id,)
            cursor.execute(sql, d)  # sql 실행
            res =[Reserve(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                  for row in cursor]
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
            sql = 'delete from reserve where id = %s'
            d = (id,)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()

            return print('삭제가 완료되었습니다.')

        except Exception as e:
            print(e)
        finally:
            self.disconn()

    def update(self, a:Reserve):
        try:
            self.connect()  # db연결
            cursor = self.conn.cursor()  # 사용할 커서 객체 생성
            sql = 'update reserve set reserve=%s, id=%s, arrmsg=%s, ' \
                  'rtNm=%s, plainNo=%s, stNm=%s, stNmD=%s, ' \
                  'reserve=%s, etc=%s)' \
                  'where id = %s'

            d = (a.reservenum, a.id, a.arrmsg, a.rtNm, a.plainNo, a.stNm, a.stNmD, a.reserve, a.etc)
            cursor.execute(sql, d)  # sql 실행
            self.conn.commit()

            return print('수정이 완료되었습니다.')

        except Exception as e:
            print(e)
        finally:
            self.disconn()



