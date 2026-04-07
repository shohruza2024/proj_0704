from flask import Flask, render_template

app = Flask(__name__)


roy = ['Lobar', 'Indira', 'Shohruza', 'Shakarjon', 'Drumboy']

@app.route('/')
def home():
    return render_template('index.html', royxat=roy)


@app.route('/roy/<int:indeks>')
def element(indeks):
    if 0 <= indeks < len(roy):
        el = roy[indeks]
    else:
        el = 'Error'

    return render_template('index.html', el = el)


@app.route('/roy/qidiruv/<name>')
def find(name):
    if name.lower() in list(map(lambda el: el.lower(), roy)):
        res = f'Topildi: {name.title()}'
    else:
        res = f"Bu '{name.title()}' nom topilmadi"
    
    return render_template('find.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)
