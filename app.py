from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def course():
    print('Course Name entered: ' + request.args.get('course_name'))
    print('Course Number entered: ' + request.args.get('course_num'))

    return render_template('favorite_course.html')

@app.route('/contact' , methods=['GET' , 'POST'])
def contact():
    if request.method == 'POST':

        first_name = request.form.get("firstnameInput1")
        last_name = request.form.get("lastnameInput1")
        email = request.form.get("emailInput1")
        major = request.form.get("majorInput1")

        print('Thank you for filling out the form!')
        print('First name entered: ' + first_name)
        print('Last name entered: ' + last_name)
        print('Email address entered: ' + email)
        print('University Major entered: ' + major)
        return render_template(
            'contact.html',
            first_name=first_name,
            last_name=last_name,
            email=email,
            major=major,
            form_submitted=True
        )
    else:
        return render_template('contact.html')



if __name__ == '__main__':
    app.run()
