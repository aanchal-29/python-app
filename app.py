from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app=Flask(__name__)

#CONFIG
#db = yaml.load(open('db.yaml'))
db = yaml.safe_load(open('db.yaml'))
print(db)
app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/student')
def student():
    
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM student")
    if resultValue>0:
        userDetails = cur.fetchall()
        return render_template('student.html',userDetails=userDetails)
    mysql.connection.commit()
    cur.close
    

    return redirect('/Modify')    



@app.route('/Modify',methods=['GET','POST'])
def index():
    
    if request.method =='POST':
        
       
        userDetails = request.form

        name = userDetails['Name']
        cur = mysql.connection.cursor()

        inst= "select * FROM student where PaperType=Test"
        sql = "INSERT INTO inst VALUES (%s)"

        cur.execute(sql, name)
        #  cur.execute ( "INSERT INTO student (select RollNo,Name,PaperType where PaperType="Test" ) )
         #VALUES(%s)",(name)
        mysql.connection.commit()
        cur.close
        return 'success'
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)


