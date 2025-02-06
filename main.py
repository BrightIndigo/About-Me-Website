from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', name='Twoje Imię', bio='Krótki opis o mnie.', image_url='static/profile.jpg', social_links={'GitHub': 'https://github.com/BrightIndigo', 'LinkedIn': 'https://www.linkedin.com/in/krzysztof-wilgucki-aa7b0a2a4/'})

@app.route('/about')
def about_me():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
