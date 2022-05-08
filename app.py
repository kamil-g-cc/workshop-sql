from flask import Flask
import psycopg2
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    connection = psycopg2.connect("dbname=nw_traders user=kamil password=test123")
    cursor = connection.cursor()
    cursor.execute("SELECT count(*) from customers")
    data = cursor.fetchone()
    return """<h1>Witaj</h1><p>Mamy """+str(data[0])+""" klientów</p>
        <form action="/search_results">
            Szukaj: <input name="query">
            <input type="submit" value="Szukaj">
        </form>
    """


if __name__ == '__main__':
    app.run()
