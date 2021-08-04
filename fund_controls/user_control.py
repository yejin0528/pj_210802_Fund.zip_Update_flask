from flask import Flask
from flask_login import UserMixin
from db_models import mysql


class User():
    # 회원가입
    @staticmethod
    def get(signup_id):  # get user
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "SELECT * FROM user_info where id = '%s' " % signup_id
        cursor.execute(sql)
        user = cursor.fetchone()

        if not user:
            return None
        else:
            return user

    @staticmethod  # signup
    def signUp(signup_id, signup_pw, name):
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "INSERT INTO user_info(id, password, name) VALUES ('%s', '%s', '%s')" % (
            str(signup_id), str(signup_pw), str(name))
        cursor.execute(sql)
        conn.commit()

    # 로그인
    @staticmethod
    def getUser(login_id):  # get user
        conn = mysql.MYSQL_CONN
        cursor = conn.cursor()
        sql = "SELECT * FROM user_info where id = '%s' " % login_id

        cursor.execute(sql)
        user = cursor.fetchone()

        if not user:
            return None
        else:
            return user
