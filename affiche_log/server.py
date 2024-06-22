import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def ip():
    files = os.listdir('Data')
    return render_template('ip.html', files=files)

@app.route('/domain_detail/<domain_name>')
def domain_detail(domain_name):
    files = os.listdir(f'Data/{domain_name}')
    return render_template('domain.html', domain_name=domain_name,  files=files)

@app.route('/<domain_name>/log_detail/<log_name>')
def log_detail(log_name, domain_name):
    # file_path = os.listdir(f'Data/{domain_name}/{log_name}')
    file_path = f'Data/{domain_name}/{log_name}/log.txt'
    
    print(file_path)
    print(os.system('dir'))
    
    with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
            
    print(file_content)
    
    return render_template('log.html', file_content=file_content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="2000", debug=True)
