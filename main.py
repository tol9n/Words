import random

from flask import Flask, send_file, render_template, request, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = 'abc'

ban = ['ь', 'ъ']


def word_check(word):
    file = open("russian.txt", 'r', encoding='utf-8')
    words = file.readlines()
    if word + '\n' in words:
        return True
    else:
        return False


@app.route('/')
def index():
    return render_template('index.html')


ass = []


@app.route('/words', methods=['GET', 'POST'])
def words():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        word = request.form['word']
        ans = word_check(word)
        if ans:
            if word not in ass:
                last_word = ass[-1] if len(ass) > 0 else ''
                if last_word != '':
                    index = -2 if last_word[-1] in ['ь', 'ъ'] else -1
                    if word[0] == last_word[index]:
                        ass.append(word)
                    else:
                        flash(f'слово не подходит, твое слово должно начинаться на "{last_word[index]}"')
                else:
                    ass.append(word)
            else:
                flash('это слово уже есть')
        else:
            flash('такого слова нет')
        return render_template('index.html', ans=ass)


@app.route('/download')
def download_file():
    return send_file('test.txt', as_attachment=True)


if __name__ == "__main__":
    app.run(host='172.30.105.99', port=5001)
    #app.run()
