from flask import Flask, request, redirect, jsonify
import random
import string
from threading import Thread

app = Flask(__name__)

# In-memory database to store URLs
url_mapping = {}

# Function to generate a random short URL
def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('url')
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    short_url = generate_short_url()
    while short_url in url_mapping:
        short_url = generate_short_url()

    url_mapping[short_url] = original_url
    return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
    original_url = url_mapping.get(short_url)
    if not original_url:
        return jsonify({'error': 'URL not found'}), 404

    return redirect(original_url)

def run_flask():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Import and run the Tkinter GUI
    from gui import root
    root.mainloop()
