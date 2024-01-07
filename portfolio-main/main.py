#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_db = request.form.get('button_db')
    button_html = request.form.get('button_html')
    button_discord = request.form.get('button_discord')
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python,button_discord=button_discord,button_html=button_html,button_db=button_db)

#Форма
@app.route('/form')
def form():
    return render_template('form.html')

#Результаты формы
@app.route('/submit', methods=['POST'])
def submit_form():
    #Создай переменные для сбора информации
    email = request.form['email']
    coment = request.form['coment']
    with open('form.txt', 'a', encoding='utf-8') as f:
        f.write(f'Почта: {email}\nКомментарий: {coment}\n' )
    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                           #Помести переменные
                            email=email, coment=coment
                           )

if __name__ == "__main__":
    app.run(debug=True)