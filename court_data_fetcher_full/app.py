from flask import Flask, request, render_template
from scraper import fetch_case_details
from models import log_query, setup_db

app = Flask(__name__)
setup_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    case_data = None
    error = None

    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']
        try:
            case_data = fetch_case_details(case_type, case_number, filing_year)
            log_query(case_type, case_number, filing_year, case_data)
        except Exception as e:
            error = str(e)

    return render_template('index.html', case_data=case_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)