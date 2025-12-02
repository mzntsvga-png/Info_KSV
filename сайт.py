from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:

            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except:
            result = "Ошибка! Введите числа"
    

    return f'''
    <html>
        <body style="padding: 50px; font-family: Arial;">
            <h2>Сумма двух чисел</h2>
            <form method="POST">
                <input type="text" name="num1" placeholder="Первое число" required><br><br>
                <input type="text" name="num2" placeholder="Второе число" required><br><br>
                <button type="submit">Сложить</button>
            </form>
            <br>
            {'<h3>Результат: ' + str(result) + '</h3>' if result else ''}
        </body>
    </html>


    <h4>Сложение</h4>
    <a href="/minus">Вычитание</a>
    '''




@app.route('/minus', methods=['GET,"POST'])
def calc():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 - num2
        except:
            result = "Ошибка! Введите числа"
    
    return f'''
    <html>
        <body style="padding: 75px; font-family: Georgia;">
        <h2>Разность двух чисел</h2>
        <form method="POST">
                <input type="text" name="num1" placeholder="Первое число" required><br><br>
                <input type="text" name="num2" placeholder="Второе число" required><br><br>
                <button type="submit">Вычесть</button>
            </form>
            <br>
            {'<h3>Результат: ' +str(result) +'/h3>' if result else ''}
        </body>
    </html>

    <h4>Вычитание</h4>
    <a href="/">Сложение</a>
    '''



while __name__ == '__main__':
    app.ru