from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import model
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'supersecretkey' 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/get_subpaths', methods=['POST'])
def get_subpaths():
    selected_path = request.form.get('selected_path')
    
    all_paths = model.getPaths()
    
    subpaths = [path for path in all_paths if path.startswith(f'/{selected_path}/')]
    subpaths = [path[len(f'/{selected_path}/'):] for path in subpaths]
    return jsonify(subpaths=subpaths)

@app.route('/examples')
def examples():
    return render_template('examples.html')

@app.route('/endpoints')
def endpoints():

    all_paths = model.getPaths()

    top_level_paths = list(set(
        path.split('/')[1] for path in all_paths if path.split('/')[1]))
    json_output = session.pop('json_output', "")
    #print(f"json_output: {json_output}")
    return render_template('endpoints.html', top_level_paths=top_level_paths, all_paths=all_paths, json_output=json_output)


@app.route('/submit', methods=['POST'])
def submit():
    selected_top_path = request.form.get('selected_top_level_path')
    selected_sub_path = request.form.get('selected_sub_path')
    print(selected_top_path, selected_sub_path)
    endpoint = str("https://api.weather.gov/" + selected_top_path + "/" + selected_sub_path)
    print(f"Endpoint: {endpoint}")
    json_output = model.getEndpointResponse(endpoint)
    session['json_output'] = json_output
    #path_input = request.form['path']
    return redirect(url_for('endpoints'))



if __name__ == '__main__':

 
    app.run(debug=True)
    
