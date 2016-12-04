from flask import Flask, send_from_directory

application = Flask(__name__)

@application.route('/')
def home():
    return 'Endpoint for files is /file/<strong>file_name</strong>'

@application.route('/file/<file_name>', methods=['GET'])
def return_file(file_name):
    return send_from_directory('./', file_name)

if __name__ == '__main__':
    application.run(debug=True)