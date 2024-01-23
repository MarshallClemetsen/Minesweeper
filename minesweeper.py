from flask import Flask, render_template,  request

app = Flask(__name__)

@app.route('/')
def index():
    # Number of buttons you want
    row_amount = 16
    row_length = 16
    try:
        row_amount = int(request.args.get('containerHeight', 20))
    except:
        row_amount = 20
    try:
        row_length = int(request.args.get('containerWidth', 30))
    except:
        row_length = 30

    # Generate button data
    button_data = [{'class': 'buttons', 'id': i} for i in range(1, (row_amount * row_length) + 1)]

    return render_template('button_grid.html', buttons=button_data, row_length=row_length, row_amount=row_amount)

if __name__ == '__main__':
    app.run(debug=True)
