from flask import Flask, request

import psycopg2

conn = psycopg2.connect(dbname = 'probniki', user = 'Viper', password = '', host = '127.0.0.1')

app = Flask(__name__)

@app.get('/post/<int:post_id>')
def get_posts(post_id):
    cursor = conn.cursor()
    cursor.execute(f'select * from users where id = {post_id}')
    users = cursor.fetchall()
    for i in users:
        return f'''<div>NAME:{i[1]}</div>
                    <div>SURNAME:{i[2]}</div>
                    <div>AGE:{i[3]}</div>
                   '''









if __name__ == '__main__':
    app.run()