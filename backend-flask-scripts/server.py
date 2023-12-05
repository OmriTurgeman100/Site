from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def run_script():
    try:
        result = subprocess.check_output(['python', r'C:\Users\omrig\Desktop\Project\backend-flask-scripts\script1.py']).decode('utf-8')

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/runscript1', methods=['GET'])
def run_script1():
    try:
        result = subprocess.check_output(['python', r'C:\Users\omrig\Desktop\Project\backend-flask-scripts\script1.py']).decode('utf-8')

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/runscript2', methods=['GET'])
def run_script2():
    try:
        result = subprocess.check_output(['python', r'C:\Users\omrig\Desktop\Project\backend-flask-scripts\script2.py']).decode('utf-8')

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})
        
@app.route('/runscript3', methods=['GET'])
def run_script3():
    try:
        result = subprocess.check_output(['python', r'C:\Users\omrig\Desktop\Project\backend-flask-scripts\script3.py']).decode('utf-8')

        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)