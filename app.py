from flask import Flask, render_template, request, flash
from flaskext.mysql import MySQL


mysql = MySQL()
app = Flask(__name__)
app.config['SECRET_KEY'] = "Junior"

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = ''#password
app.config['MYSQL_DATABASE_DB'] = ''#nome banco
app.config['MYSQL_DATABASE_HOST'] = ''#idress
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/cadastrarProduto', methods=['POST'])
def cadastro_produto():
    nome = request.form['nome']
    preco = request.form['preco']
    categoria_do_produto = request.form['categoria_produto']
    if nome and preco and categoria_do_produto:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into cadastro_pilotos (nome, preco, categoria_do_produto)'
                       'VALUES (%s, %s, %s)', (nome, preco, categoria_do_produto))
        conn.commit()
        dic = {'nome': nome, 'preco': preco, 'categoria_do_produto': categoria_do_produto}
        flash('sucess')
        return render_template('index.html', dic)
    flash('fail')
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
