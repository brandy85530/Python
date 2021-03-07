#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pymysql
from pymysql.cursors import DictCursor


def main():
    con = pymysql.connect(host='localhost', port=3306,
                          database='exam', charset='utf8',
                          user='youruser', password='yourpassword')
    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute('select eno as no, ename as name, course, score, pass from tb_1 where pass ="pass"')
            results = cursor.fetchall()
            print('编號\t學生\t科目\t成績\t是否通過')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['course'], end='\t')
                print(dept['score'], end='\t')
                print(dept['pass'])
    finally:
        con.close()


if __name__ == '__main__':
    main()


# In[ ]:




