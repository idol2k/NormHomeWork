from flask import Flask, request

import psycopg2

conn = psycopg2.connect(dbname = 'probniki', user = 'Viper', password = '', host = '127.0.0.1')
 
POSTS = [
    {
        'name': 'Ignat',
        'text': 'Kak dela?',
        'date': '11-12-2003 3:25:43'
    },
    {
        'name': 'Sergei',
        'text': 'Hello Ignat',
        'date': '13-12-2023 4:32:54'
    },
    {
        'name': 'Oleg',
        'text': 'Hello people!',
        'date': '23-04-2022 13:34:32'
    }
]


app = Flask(__name__)

@app.get('/get_posts')
def get_posts():
    return {'posts': POSTS}


@app.route('/text/', methods=['GET', 'POST'])
def put_posts():
    if request.method == 'POST':
        text_ = request.form.get('text')
        name_ = request.form.get('name')
        date_ = request.form.get('date')
        cursor = conn.cursor()
        cursor.execute('insert into posts (text, name, data) VALUES (%s,%s,%s)', (text_, name_, date_))
        conn.commit()
        return f'''<h1>Name: {name_}</h1> \n
                   <h1> Text: {text_}</h1>
                   <h1>Date: {date_}</h1>'''
    elif request.method == 'GET':
        return '''
                <form method="POST">
                    <div><label>Text: <input type="text" name="text"></label></div>
                    <div><label>Name: <input type="text" name="name"></label></div>
                    <div><label>Date: <input type="text" name="date"></label></div>
                    <input type="submit" value="Submit">
                </form>'''
    return print(request.method)
        



if __name__ == '__main__':
    app.run()


