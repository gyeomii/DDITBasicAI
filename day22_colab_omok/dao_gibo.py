import pymysql

class DaoGibo:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        

    
    def insert(self,pan,win,gibos,gibo_ais,anss):
        cnt =0 
        
        for i in range(len(anss)):
            gibo = gibos[i]
            gibo_ai = gibo_ais[i]
            ans = anss[i]
            sql = f"""
                insert into gibo
                    (pan,win,gibo,gibo_ai,ans)
                values 
                    ('{pan}','{win}','{gibo}','{gibo_ai}','{ans}')
            """
            print(sql)
            cnt += self.curs.execute(sql)
        
        
        self.conn.commit()
        return cnt

    
    def getPanMax(self):
        sql = f"""
            select IFNULL(max(pan),0)+1 AS max
            from gibo
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        return rows[0]['max'];
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    pan = "1"
    win = "2"
    gibo = ["1","1"]
    gibo_ai = ["x","x"]
    ans = ["0","1"]
    de = DaoGibo()
    # cnt = de.insert(pan, win, gibo, gibo_ai, ans)
    # print("cnt",cnt)
    mymax = de.getPanMax()
    print("mymax",mymax)
    
    
    
    
    