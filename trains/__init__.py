from flask import Flask, render_template, jsonify, request

# try:
from mailer import Mailer
from sheets import volunteers, trainings, roles, role_map
# except ImportError:
#     from .mailer import Mailer
#     from .sheets import volunteers, trainings, roles, role_map


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='%%',
        variable_end_string='%%',
        comment_start_string='<#',
        comment_end_string='#>',
    ))


app = CustomFlask(__name__)
app.mailer = Mailer()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/roles', methods=['GET'])
def serve_roles():
    return jsonify(roles)

@app.route('/send', methods=['POST'])
def send_email():
    target_roles = request.get_json()['sent_roles']
    email_text = request.get_json()['email_text']
    app.mailer.send(email_text, target_roles)
    return 'True'

def main():
    app.config['DEBUG'] = False
    try:
        app.run('0.0.0.0', port=80)
    except PermissionError:
        print("Permission Denied. This uses port 80. Try again with sudo.")

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('0.0.0.0')
