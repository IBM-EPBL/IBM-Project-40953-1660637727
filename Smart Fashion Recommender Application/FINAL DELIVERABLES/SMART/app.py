from flask import Flask,render_template,request,flash,url_for,redirect,session
import mysql.connector
#from flask_mysqldb import MySQL
import os
import json


 


image=os.path.join('static')
app=Flask(__name__)
app.config['UPLOAD_FOLDER']=image


#app.config["MYSQL_HOST"]="localhost"
#app.config["MYSQL_USER"]="root"
#app.config["MYSQL_PASSWORD"]=""
#app.config["MYSQL_DB"]="flask_registration"
#mysql=MySQL(app)

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='oneline'
)



@app.route('/connect')
def connect():
    #display=mydb
    return render_template("connect.html")
@app.route('/index')
def index():
    myimg=os.path.join(app.config['UPLOAD_FOLDER'],'college.png')
    return render_template("index.html",user_image=myimg)
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #details=request.form
        lgname=request.form['lname']
        pas=request.form['lpas']
        mycursor=mydb.cursor()
        sql="""SELECT * FROM `registration` WHERE `name`=%s AND `pas`=%s """
        mycursor.execute(sql,(lgname,pas))
        myres = mycursor.fetchall()
        for x in myres:
            name = x[1]
            pss = x[3]
            print(name,pss)
        #mycursor.execute("SELECT *  from registration WHERE name=abish AND pass=1234")
        
            
        
        
            if name == lgname or pss == pas:
                #lgname=myresult['name']
                #pas=myresult['pas']
                #name=lgname
                #pss=pas
                return redirect('/page')
            
            
            
            #session["lpas"]=myresult('pass')
            
        #else:
            #return redirect('/index')
    return render_template("login.html")

@app.route('/register',methods=['GET','POST'])
    

def register():
    if request.method =='POST':
        details=request.form
        uname=details['username']
        
        email=details['email']
        inves=details['question1_field']
        # usd="wfwef"
        
        cpassw=details['cinves']
        mycursor=mydb.cursor()
        sql="INSERT INTO registration(name,email,pas,cpass) VALUES (%s,%s,%s,%s)"
        val=(uname,email,inves,cpassw)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        #iden=mycursor.rowcount
        #con=mysql.connection.cursor()
        #sql="insert into registration(name,email,password,confirm password) value (%s,%s,%s,%s)"
        #con.execute(sql,[uname,email,passw,cpassw])
        #mysql.connection.commit()
        #con.close
        return redirect('/login')
    return render_template("register.html")
@app.route('/rer', methods=['GET','POST'])
def rer():
    if request.method == 'POST':
        details=request.form
        uname=details['username']
        email=details['email']
        inves=details['inves']
        cinves=details['cinves']
        mycursor=mydb.cursor()
        sql="""INSERT INTO registration(name,email,pass,cpass) VALUES (%s,%s,%s,%s)"""
        val=(uname,email,inves,cinves)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
    return render_template('register2.html')

@app.route('/page')
def bat():
    return render_template('page.html')
        
@app.route('/shirts')
def shirts():
    return render_template('shirts.html')
@app.route('/chudr')
def chudr():
    return render_template('chudr.html')
@app.route('/jk')
def jk():
    return render_template('jk.html')
    
        
    
    
if __name__ == '__main__':
    
    app.debug = True
    app.run(host='localhost',port=5000)
    