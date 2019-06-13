import pymysql
import pandas as pd

from domain.readJSON import getJSON


def getDB():
    mydb = pymysql.connect(
        "mydbtfg-cluster.cluster-cmsvfrkk9jfj.eu-west-3.rds.amazonaws.com",
        "sllull",
        "Vy55Uu58",
        "historials_clinics"
    )
    return mydb


def readSQLtoDF ():
    mydb = getDB()
    df = pd.read_sql('SELECT * FROM historials_clinics', con=mydb)
    return df


def insertData ():
    data = getJSON()
    mydb = getDB()
    sql = "INSERT INTO historials_clinics VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (data['dia'], data['mes'], data['any'], data['cp'], data['edat'], data['sexe'], data['pes'], data['urg_vis'], data['prediction'])
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()


def selectPrediction(pred):
    mydb = getDB()
    df = pd.read_sql('SELECT * FROM historials_clinics WHERE diagnostic ='+str(pred), con=mydb)
    return df
