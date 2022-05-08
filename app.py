from flask import Flask, request
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

@app.route('/search_results')
def search():
    out = ""
    search_phrase = request.args.get("query")
    connection = psycopg2.connect("dbname=nw_traders user=kamil password=test123")
    cursor = connection.cursor()
    sql_query = "SELECT product_name FROM products WHERE product_name LIKE '"+search_phrase+"%'"
    print(sql_query)
    cursor.execute(sql_query)
    data = cursor.fetchall()

    for row in data:
        out+="<tr><td>" + row[0] + "</td></tr>"

    return """<h1>Witaj</h1>
            <h2>Wyniki wyszukiwania</h2>
            <table>
                <tr><th>Nazwa produktu</th></tr>
                """+ out +"""
            </table>
        """


if __name__ == '__main__':
    app.run()
