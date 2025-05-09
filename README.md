# URL Shortener

This is a simple Flask-based web service for creating shortened URLs and redirecting them.

## Features
- Shorten a given URL.
- Redirect to the original URL using the shortened URL.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Use the endpoints:
   - `POST /shorten`: Provide a JSON body with a `url` field to shorten a URL.
   - `GET /<short_url>`: Redirects to the original URL associated with the shortened URL.

## Example

1. Shorten a URL:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com"}' http://127.0.0.1:5000/shorten
   ```

   Response:
   ```json
   {
       "short_url": "abc123"
   }
   ```

2. Redirect using the shortened URL:
   Open `http://127.0.0.1:5000/abc123` in your browser to be redirected to `https://example.com`. 
