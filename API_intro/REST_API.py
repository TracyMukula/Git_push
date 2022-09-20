from flask import Flask, request, jsonify
import sqlite3 as sql
app = Flask(__name__)
conn = sql.connect('C:\sqlite\MEDICAL.db')
cursor = conn.cursor()

@app.route('/get_method', methods = ['GET'])
def first_call():
    doctor_id = request.args.get('id')
    if doctor_id == None:
        x = 'Please enter a valid id'
    else:
        conn = sql.connect('C:\sqlite\MEDICAL.db')  #another way of doing this.
        cursor = conn.cursor()
        raw_sql=('''select*from DOCTORS
                    where id = {}'''.format(doctor_id))
        data = cursor.execute(raw_sql)
        doctor = str(data.fetchone())
        print(doctor)
        conn.commit()
    return jsonify({"personal_data": doctor})


@app.route('/update_method', methods = ['POST'])
def second_call():
    conn = sql.connect('C:\sqlite\MEDICAL.db')
    cursor = conn.cursor()
    doctor_id = int(request.args.get('id'))
    field = str(request.args.get('field'))
    raw_sql= (''' update DOCTORS
                set field = 'Antenatal'
                where id = 3''')
    data = cursor.execute(raw_sql)
    updated = ('''select*from doctors''')
    result = cursor.execute(updated).fetchall() #ask
    conn.commit()
    return jsonify({"updated_table": result})
   
   
@app.route('/delete_method', methods = ['POST']) #use post as long as you are using arguments
def third_call():
    conn = sql.connect('C:\sqlite\MEDICAL.db')
    cursor = conn.cursor()
    doctor_id = int(request.args.get('id'))
    raw_sql = ('''delete from doctors
                where id = {}'''.format(doctor_id))
    output = cursor.execute(raw_sql)
    new_table = ('''select*from doctors''')
    result = cursor.execute(new_table).fetchall() #ask
    conn.commit()
    return jsonify({"updated_table": result})

@app.route('/insert_method', methods = ['POST'])
def fourth_call():
    conn = sql.connect('C:\sqlite\MEDICAL.db')
    cursor = conn.cursor()
    doctor_id = int(request.args.get('id'))
    raw_sql = ('''insert into DOCTORS values (4, 'Pearl', 29, 'Intern', 1)''')
    output = cursor.execute(raw_sql)
    new_table = ('''select*from DOCTORS''')
    result = cursor.execute(new_table).fetchall()
    conn.commit()
    return jsonify ({"updated_table": result})


if __name__ == '__main__':
    app.run(debug=True, port = 5022, host ='127.0.0.1') #port number

  #print(type(result))
        # id = result[0][0]
        # name = result[0][1]
        # age = result[0][2]
        # field = result[0][3]
        # experience = result[0][4]
        # x = dict()
        # x['doctor_id'] = id
        # x['doctor_name'] = name
        # x['age'] = age
        # x['field'] =  field
        # x['experience'] = experience   

# conn.commit()
#     updated()
#     return updated() #updated
# def updated():
#     conn = sql.connect('C:\sqlite\MEDICAL.db')
#     cursor = conn.cursor()
#     sql_1 = ('''select*from DOCTORS''')
#     result = cursor.execute(sql_1).fetchall()
#     print(result)
#     one = result[0]
#     two = result[1]
#     three = result[2]
#     four = result[3]
#     five = result[4]
#     x = dict()
#     x['doctor_one'] = one
#     x['doctor_two'] = two
#     x['doctor_three'] = three
#     x['doctor_four'] = four
#     x['doctor_five'] = five
#     conn.commit()
#     return jsonify ({"result":x})