from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app=Flask(__name__)

#CONFIG
#db = yaml.load(open('db.yaml'))
db = yaml.safe_load(open('db.yaml'))

app.config['MYSQL_HOST']= db['mysql_host']
app.config['MYSQL_USER']= db['mysql_user']
app.config['MYSQL_PASSWORD']= db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/student')
def student():
    
   cur = mysql.connection.cursor()
   resultValue = cur.execute("SELECT * FROM student")
   print("hi executed DB fetch")
   if resultValue>0:
     userDetails = cur.fetchall()
     return render_template('student.html',userDetails=userDetails)
    
    # return redirect('/student/update')    


# @app.route('/update')
# def update():
    
#      return render_template('index.html')
    


@app.route('/up',methods = ['GET','POST'])
def index():
    
    if request.method =='POST':
        
       
        userDetails = request.form
        print(userDetails)
        name = userDetails['name']
        print(name)
        cur = mysql.connection.cursor()               
        sql = "UPDATE student SET PaperType ='%s' WHERE PaperType = '%s'" % (name,"Test")        
        cur.execute (sql)
        mysql.connection.commit()
        cur.close()
        return 'success' 
    return render_template('index.html')

    
    
if __name__ == '__main__':
    app.run(debug=True)


