from flask import Flask, render_template, jsonify

try:
    from sheets import volunteers, trainings, roles, role_map
except ImportError:
    from .sheets import volunteers, trainings, roles, role_map


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


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/volunteers', methods=['GET'])
def serve_volunteers():
    return jsonify(volunteers)

@app.route('/trainings', methods=['GET'])
def serve_trainings():
    return jsonify(trainings)

@app.route('/roleMap', methods=['GET'])
def serve_role_map():
    return jsonify(role_map)

@app.route('/roles', methods=['GET'])
def serve_roles():
    return jsonify(roles)


def main():
    app.config['DEBUG'] = False
    try:
        app.run('0.0.0.0', port=80)
    except PermissionError:
        print("Permission Denied. This uses port 80. Try again with sudo.")

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('0.0.0.0')
