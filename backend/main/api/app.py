from flask import Flask, render_template, request
import os
from backend.main.db.DBManager import DBManager

app = Flask(__name__)

@app.route('/')
def home():
    #TODO this path is notworking
    return render_template('templates/index.html')

#TODO add Delete and Modify
@app.route('/grades', methods=['POST', 'GET'])
def grades():
    if request.method == 'GET':
        my_db.cursor.execute(''' SELECT scale, grade, numeric_grade, description FROM grades order by id ''')
        rs = my_db.cursor.fetchall()
        print(rs)
        return rs

    if request.method == 'POST':
        name = 'bar'
        scale = 'foo'
        numeric_grade = 10
        my_db.cursor.execute(''' INSERT INTO grades (scale, grade, numeric_grade) VALUES(%s,%s,%s) ''',
                             (name, scale, numeric_grade))
        #TODO commit function in the Connection class does not exist. This needs to reference mysql commit
        my_db.commit()
        my_db.cursor.close()
        return f"Done!!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    my_db = DBManager()
    app.run(debug=True, host='0.0.0.0', port=port)

