from flask import Flask

app = Flask(__name__)


@app.route('/<texto>')
def texto(texto):
    return f'Hello, {texto}'


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/adicao/<num1>+<num2>')
def adicao(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return (f'{num1} + {num2} = {num1 + num2}')
    except ValueError:
        return "Insira números inteiros. EX: 2, 584, 13..."


@app.route('/subtração/<num1>-<num2>')
def subtracaoo(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return (f'{num1} - {num2} = {num1 - num2}')
    except ValueError:
        return "Insira números inteiros. EX: 2, 584, 13..."


@app.route('/divisao/<num1>/<num2>')
def divisao(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return (f'{num1} / {num2} = {num1 / num2}')
    except ValueError:
        return "Insira números inteiros. EX: 2, 584, 13..."
    except ZeroDivisionError:
        return "Não é possível dividir por zero."


@app.route('/multiplicacao/<num1>*<num2>')
def multiplicacao(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        return (f'{num1} * {num2} = {num1 * num2}')
    except ValueError:
        return "Insira números inteiros. EX: 2, 584, 13..."

@app.route('/impar_par/<int:num1>')
def impar_par(num1):
    if num1 % 2 == 0:
        return f'Número {num1} é par'
    elif num1 % 2 == 1:
        return f"Número {num1} é ímpar"


if __name__ == '__main__':
    app.run(debug=True)
