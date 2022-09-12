from flask import Flask, request, jsonify
import sqlite3 as sql
app = Flask(__name__)
conn = sql.connect('OCCUPATIONS.db')
cursor = conn.cursor()

@app.route('/get_trial', methods = ['GET']) #get method not necessary because FLASK calls get by default.
def call_one():
    id = request.args.get('ID')
    if id == None:
        text = 'Please enter a valid ID'
    else:
        cursor.execute('''
                        select * from ENGINEERS
                        WHERE ID = id''')
    return jsonify({"message": id})

    
@app.route('/update_trial', methods = ['PUT'])
def call_two():
    ID = request.args.get('ID')
    EXPERIENCE = request.args.get('EXPERIENCE')
    cursor.execute('''
                    UPDATE ENGINEERS
                    SET EXPERIENCE = 5
                    WHERE ID = 1 ''')
    conn.commit()
    return jsonify({"message": ID})

@app.route('/delete_trial', methods = ['DELETE'])
def call_three():
    ID = request.args.get('ID')
    cursor.execute('''
                    DELETE FROM ENGINEERS
                    WHERE ID = 3''')
    conn.commit()
    return jsonify({"message": ID})

@app.route('/insert_trial', methods = ['PUT'])
def call_four():
    ID = request.args.get('ID')
    cursor.execute('''
                    INSERT INTO ENGINEERS(ID, NAME, AGE,FIELD,EXPERIENCE)
                    VALUES
                    (5, 'Arthur', 34, 'RADIOLOGY,' 6)''')
    conn.commit()
    return jsonify ({"message": ID})
if __name__ == '__main__':
    app.run(debug=True, port = 5022, host ='127.0.0.1') #port number

