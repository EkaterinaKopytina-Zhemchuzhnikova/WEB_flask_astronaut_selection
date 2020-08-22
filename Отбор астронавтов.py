from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/astronaut selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                         href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                         integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                         crossorigin="anonymous">
                         <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style2.css')}" />
                         <title>Отбор астронавтов</title>
                    </head>
                    <body>
                        <h1>Анкета претендента</h1>
                        <p>на участие в миссии</p>
                        <div>
                            <form class="login_form" method="post">
                            <div>
                            <input type="text" class="form-control" id="user_surname" placeholder="Введите фамилию" name="user_surname">
                            <input type="text" class="form-control" id="user_name" placeholder="Введите имя" name="user_name">
                            </div>
                            <div>
                            <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                            </div>

                        <div class="form-group">
                        <label for="classSelect">Какое у вас образование?</label>
                        <select class="form-control" id="classSelect" name="class">
                            <option>начальное</option>
                            <option>среднее</option>
                            <option>высшее</option>
                        </select>
                        </div>

                        <div class="form-group">
                            <label for="form-check">Какие у вас есть профессии?</label>

                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="profession" id="1" value="1" checked>
                            <label class="form-check-label" for="1">
                             Инженер-исследователь
                            </label>
                        </div>

                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="profession" id="2" value="2">
                            <label class="form-check-label" for="2">
                                Пилот
                            </label>
                        </div>

                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="profession" id="3" value="3">
                            <label class="form-check-label" for="3">
                                Строитель
                            </label>
                        </div>

                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="profession" id="4" value="4">
                            <label class="form-check-label" for="4">
                                Экзобиолог
                            </label>
                        </div>

                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="profession" id="5" value="5">
                            <label class="form-check-label" for="5">
                                Инженер по терраформированию
                            </label>
                        </div>

                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="profession id="6" value="6">
                            <label class="form-check-label" for="6">
                                Климатолог
                            </label>
                        </div>
                        </div>
                    
                        <div class="form-group">
                            <label for="form-check">Укажите пол</label>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                            <label class="form-check-label" for="male">
                             Мужской
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                            <label class="form-check-label" for="female">
                                Женский
                            </label>
                        </div>
                        </div>

                        <div class="form-group">
                            <label for="about">Почему вы хотите принять участие в миссиии?</label>
                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                        </div>

                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                        </div>

                        <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                        </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                        </form>
                        </div>
                        </div>
                    </body>
                </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
