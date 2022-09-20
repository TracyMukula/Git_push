from flask import Flask, request, jsonify
import sqlite3 as sql
app = Flask(__name__)
#conn = sql.connect('OCCUPATIONS.db')
#cursor = conn.cursor()

@app.route('/get_trial', methods = ['GET']) #get method not necessary because FLASK calls get by default.
def call_one():
    id = request.args.get('ID')
    if id == None:
        text = 'Please enter a valid ID'
    else:
        conn = sql.connect('C:\sqlite\OCCUPATIONS.db')
        cursor = conn.cursor()

        raw_sql = ('''
                        select ID, NAME, AGE, FIELD, EXPERIENCE from ENGINEERS;''')
        #WHERE ID = {}'''.format(id))
        print(raw_sql)
        result = cursor.execute(raw_sql)
        data =result.fetchall()
        print(data)
        # name = data[1]
        # field = data[3]
        # experience = data[4]
        x = dict()
        # x['name'] = name
        # x['field'] = field
        # x['experience'] = experience
        
    return jsonify({"user_data":x})

    
@app.route('/update_trial', methods = ['POST'])
def call_two():
    id = int(request.args.get('ID'))
    exp = int(request.args.get('EXPERIENCE'))
    conn = sql.connect('C:\sqlite\OCCUPATIONS.db')
    cursor = conn.cursor()
    raw_sql = '''UPDATE ENGINEERS SET EXPERIENCE = 2 WHERE ID = 1 '''
    cursor.execute(raw_sql)
    conn.commit()
    return jsonify({"message": id})

@app.route('/delete_trial', methods = ['POST'])
def call_three():
    id = int(request.args.get('ID'))
    conn = sql.connect('C:\sqlite\OCCUPATIONS.db')
    cursor = conn.cursor()
    cursor.execute('''
                    DELETE FROM ENGINEERS
                    WHERE ID = {}'''.format(id))
    conn.commit()
    return jsonify({"message": id})

@app.route('/insert_trial', methods = ['POST'])
def call_four():
    id = int(request.args.get('ID'))
    conn = sql.connect('OCCUPATIONS.db')
    cursor = conn.cursor()
    cursor.execute('''
                    INSERT INTO ENGINEERS(ID, NAME, AGE,FIELD,EXPERIENCE)
                    VALUES
                    (5, 'Arthur', 34, 'RADIOLOGY,' 6)''')
    conn.commit()
    return jsonify ({"message": id})
if __name__ == '__main__':
    app.run(debug=True, port = 5022, host ='127.0.0.1') #port number

