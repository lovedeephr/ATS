from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory database for now (we'll improve this later)
job_postings = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post_job', methods=['POST'])
def post_job():
    title = request.form['title']
    description = request.form['description']
    job_postings.append({'title': title, 'description': description})
    return "Job posted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
