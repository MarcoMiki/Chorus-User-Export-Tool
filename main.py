from flask import Flask, render_template, request, make_response
from Chorus import Chorus

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/export', methods=['POST'])
def export_users():
    url = request.form["url"]
    key = request.form["apikey"]
    try:
        chorus = Chorus(url=url, key=key)
        export = chorus.export_user_data()
        response = make_response(export)
        response.headers['Content-Disposition'] = 'attachment; filename=_chorus_user_export.csv'
        response.mimetype = 'text/csv'
        return response
    except Exception as e:
        print("Error exporting user data: ", e)
        return render_template('index.html', error=True)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)
