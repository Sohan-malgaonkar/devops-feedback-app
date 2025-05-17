from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
feedback_list = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']
        feedback_list.append({'name': name, 'email': email, 'comment': comment})
        return redirect(url_for('show_feedback'))
    return render_template('feedback.html')

@app.route('/feedback/show')
def show_feedback():
    return render_template('show_feedback.html', feedbacks=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)
