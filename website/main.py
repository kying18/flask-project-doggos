from flask import Flask, render_template, send_file, request
from flask_mail import Mail, Message
import random
import config

app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=config.EMAIL,
    MAIL_PASSWORD=config.PASSWORD,
)
mail = Mail(app)

@app.route("/")
@app.route("/index/")
def index():
    return render_template('home.html', success=False, error=False)

@app.route("/send_email/", methods=['POST'])
def send_email():
    try:
        if random.randint(1, 10) == 1:
            type = "dank meme"
        else:
            type = "good doggo"

        msg = Message("Here's a {} from {}".format(type, request.form['name']),
                      sender="lookatthedoggo@gmail.com",
                      recipients=[request.form['email']])

        if type == "dank meme":
            urls = [
                'www.reddit.com/r/memes/comments/futfxj/ecosystem_is_back_to_normal/',
                'www.reddit.com/r/memes/comments/fuv27g/spidersaur_spidersaur_does_whatever_a_spidersaur/',
                'www.reddit.com/r/memes/comments/fuvfek/damn_raccoon_and_his_desire_to_kill_me/',
                'www.reddit.com/r/funny/comments/fuwdbw/calm_down_admiral/'
            ]
            attach = "{}: {}".format(type, random.choice(urls))
        else:
            extensions = ['B-j--aABWXd', 'B-iYYtJh8MD', 'B-daWgSh-m6', 'B-W_IakhkHW', 'B-SIpRHB1mA']
            attach = "{}: www.instagram.com/icanteven/p/{}".format(type, random.choice(extensions))

        msg.html = "Hey there! This is a message from {}.".format(request.form['name'])+ \
                    "<br/><br/>Hope quarantine is treating you well.<br/>Here's a {}".format(attach) +\
                   "<br/><br/><br/>Sent via <a href=\"http://dankmemesdoggodreams.pythonanywhere.com/\">dankmemesdoggodreams.pythonanywhere.com</a>."+ \
                   "<br/>Check out <a href='https://youtu.be/8q3qje9K5uU'>this video</a> on YouTube!!"
        mail.send(msg)
        return render_template('home.html', success=True, error=False)
    except:
        return render_template('home.html', success=False, error=True)

# run the application
if __name__ == "__main__":
    send_email()
    app.run(debug=True)
