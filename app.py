from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Список текстов для практики
with open('texts.txt', 'r', encoding='utf-8') as file:
    texts = file.read().splitlines()

@app.route('/')
def index():
    # Рендеринг главной страницы
    return render_template('index.html')

@app.route('/get_text', methods=['GET'])
def get_text():
    # Выбор случайного текста из списка
    text = random.choice(texts)
    return jsonify({'text': text})

if __name__ == '__main__':
    # Запуск приложения в режиме отладки
    app.run(debug=True)
