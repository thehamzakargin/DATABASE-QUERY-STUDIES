import mysql.connector
from connection import connection
from datetime import datetime


mycursor = connection.cursor()
sql = "INSERT INTO okul.stuff(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
stuff = [
    ("101","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("102","Ali","Can",datetime(2005, 6, 17),"E"),
    ("103","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("104","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("105","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("106","Ali","Cenk",datetime(2003, 8, 25),"E")
]

mycursor.executemany(sql, stuff)

try:
    connection.commit
    print(f'{mycursor.rowcount} tane kayıt eklendi.')
except mysql.connector.Error as err:
    print('hata:', err)
finally:
    connection.close()





'''
class stuff:
    connection = connection
    mycursor = connection.cursor()
    def _init_(self, StudentNumber,Name,Surname,Birthdate,Gender):
        self.StudentNumber = StudentNumber
        self.Name = Name
        self.Surname = Surname
        self.Birthdate = Birthdate
        self.Gender = Gender

    def saveStuff(self):
        sok = ("INSERT INTO stuff(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)")
        values = (self.StudentNumber, self.Name, self.Surname, self.Birthdate, self.Gender)
        stuff.mycursor.execute(sok, values)

        try:
           stuff.connection.commit
           print(f'{stuff.mycursor.rowcount} tane kayıt eklendi.')
        except mysql.connector.Error as err:
           print('hata:', err)
        finally:
           stuff.connection.close()

ahmet = stuff("201","ahmet","yılmaz",datetime(2005, 5, 17),"E")
ahmet.saveStuff()
'''



import pandas as pd
df = pd.read_csv("pandasWork/player_data.csv")
#result = df.head(20)
#result = len(df.index)
#result = df["weight"].mean() #weight dene şeyin ortalaması 
#result = df["weight"].max() #en kilolu arkadaşımızın kilosu weight ağırlık demek beyler
result = df[df["weight"] ==df["weight"].max()]["name"].iloc[0] #listedeki en kilolu adamın columns değerine gidip iloc yazarak il endexi yazmasını istedik sadece 
def str_find(name):
    if "and" in name.lower():
        return True
    return False
result = df[df["name"].apply(str_find)]
print(result)
