from flask import Flask
from redis import Redis
import mysql.connector


app = Flask(__name__)
redis = Redis(host='redis-container', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return ' - - - This basic web page has been viewed {} time(s) - - -'.format(redis.get('hits'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

def tasks() :
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'docker'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks')
    results = [{title: completed} for (title, completed) in cursor]
    cursor.close()
    connection.close()

    return results



@app.route('/delete/<title>', methods=['POST'])
def delete(title):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'docker'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    query = "DELETE FROM tasks WHERE title = %s"
    cursor.execute(query, (title,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)