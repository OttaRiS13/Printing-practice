from flask import Flask, render_template, request, jsonify
from flask_caching import Cache
import random
import time

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

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

@app.route('/save_result', methods=['POST'])
def save_result():
    data = request.json
    time_taken = data.get('time_taken')
    correct_count = data.get('correct_count')
    incorrect_count = data.get('incorrect_count')

    # Сохранение результатов в кэш
    results = cache.get('results') or []
    results.append({
        'time_taken': time_taken,
        'correct_count': correct_count,
        'incorrect_count': incorrect_count
    })
    cache.set('results', results)

    return jsonify({'status': 'success'})

@app.route('/get_results', methods=['GET'])
def get_results():
    results = cache.get('results') or []
    return jsonify({'results': results})

@app.route('/clear_results', methods=['POST'])
def clear_results():
    cache.set('results', [])
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    # Запуск приложения в режиме отладки
    app.run(debug=True)
