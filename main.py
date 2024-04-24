from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)



class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open = StringField('Open', validators=[DataRequired()])
    close = StringField('Close', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=['☕️', '☕️' * 2, '☕️' * 3, '☕️' * 4, '☕️' * 5], validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=['💪', '💪💪', '💪' * 3, '💪' * 4, '💪' *5], validators=[DataRequired()])
    power = SelectField('Power',choices=['🔌', '🔌' * 2, '🔌' * 3, '🔌' * 4, '🔌' * 5] , validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open(file='cafe-data.csv', mode='a') as file:
            my_string = ('\n' + form.cafe.data + ',' + form.location.data + ',' + form.open.data + ',' +form.close.data + ','
                         + form.coffee.data + ',' + form.wifi.data + ',' + form.power.data)
            file.write(my_string)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
