import pymysql
import numpy as np

class DaoGibo:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    
    def selectGiboAi(self):
        gibo_ais = []
        anss = []
        
        gibo_ais_pp = []
        
        sql = f"""
            select gibo_ai,ans
            from gibo
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            gibo_ais.append(row['gibo_ai'])
            anss.append(row['ans'])

        
        for h4 in gibo_ais:
            line = []
            for i in range(400):
                hanjari = h4[i:i+1]
                if hanjari == "0":
                    line.append(0)
                if hanjari == "1":
                    line.append(1)
                if hanjari == "x":
                    line.append(-1)
                
            gibo_ais_pp.append(line)
        
        # line_trash = []
        # for i in range(400):
        #     line_trash.append(-1)
        # gibo_ais_pp.append(line_trash)
        #
        # anss.append(399)
        
        gibo_ais_pp_n =  np.array(gibo_ais_pp)
        anss_n = np.array(anss)
        print(gibo_ais_pp_n.shape)
        print(anss_n.shape)
        
        print(gibo_ais_pp_n)
        print(anss_n)
        np.save("omok_train6",gibo_ais_pp_n)
        np.save("omok_answer6",anss_n)
        


        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        
if __name__ == '__main__':
    dg = DaoGibo()
    dg.selectGiboAi()
    
    
    