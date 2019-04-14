'''
Project by Patrick Tuyizere on 2019/03/26
A Portfolio showcasing the skills I have acquired in web designed and development.
I acknowledge the love and support from friends and family throughout the completion of this project.

'''

from flask import Flask, render_template, session, redirect, url_for



app = Flask(__name__)

# Define app configurations
app.config['SECRET_KEY'] = "]^S1$&tw*,(Q4Q]{b?*&]<xctTg?2.Fn%0m]Ri[%!u*<+Uy6?kNCLlcJmiwdxh/"
app.config['DEBUG'] = True
app.config['MONGODB_SETTINGS'] = {
    'db': 'Portfolio',
    'host': 'localhost',
    'port': 27017
}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')



# Start server
if __name__ == '__main__':
    app.run(host='localhost', port=5000)