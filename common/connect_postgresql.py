import psycopg2
# 数据库连接
class ConnectDb():
    # 初始化连接数据库，创建游标
    def __init__(self):
        # 连接数据库
        self.db = psycopg2.connect(
        database="hrs-fat",
        user="thedev",
        password="G4xArzY86UTYcThfqrNaBcp=kJxjXzCG",
        host="pgm-bp13uk5rn4321pv09o.pg.rds.aliyuncs.com",
        port=1921)
        # 创建游标
        self.cur = self.db.cursor()
    def select_sql(self,sql):
        # sql = '"select * from hrs_user where user_id="10001"'
        self.cur.execute(sql)
        result=self.cur.fetchall()
        print(result)
        return  result

    def execute_sql(self,sql):
        self.cur.execute
        self.db.commit()

'''
1.导入数据库
'''


    def close(self):
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    ConnectDb
    ConnectDb.select_sql()

# def hr_queryData(cur):
#     cur.execute("select * from hrs_user")  # 查询员工入职信息
#     cur.
# # cur.execute("delete  from hrs_user where user_id='10080670'")   #删除员工入职信息
# cur.execute("delete  from hrs_employee_contract where user_id='10080701'")   #删除员工合同
# cur.execute("delete  from hrs_employee_salary where user_id='10080701'")   #删除员工薪资
# cur.execute("delete  from hrs_employee_changes where user_id='10080701'")   #删除员工异动
#
# # cur.execute("select * from hrs_user where user_name like '%邹%'")
# # cur.execute("select * from hrs_user where user_name like '%邹%'")
# # rows = cur.fetchall()  # all rows in table
# print("删除成功................")
# conn.commit()
# cur.close()  # 关闭游标
# conn.close()  # 关闭数据库
# def hr_queryData(cur):
#     cur.execute("select * from hrs_user")  # 查询员工入职信息
#     cur.
# # cur.execute("delete  from hrs_user where user_id='10080670'")   #删除员工入职信息
# cur.execute("delete  from hrs_employee_contract where user_id='10080701'")   #删除员工合同
# cur.execute("delete  from hrs_employee_salary where user_id='10080701'")   #删除员工薪资
# cur.execute("delete  from hrs_employee_changes where user_id='10080701'")   #删除员工异动
#
# # cur.execute("select * from hrs_user where user_name like '%邹%'")
# # cur.execute("select * from hrs_user where user_name like '%邹%'")
# # rows = cur.fetchall()  # all rows in table
# print("删除成功................")
# conn.commit()
# cur.close()  # 关闭游标
# conn.close()  # 关闭数据库
