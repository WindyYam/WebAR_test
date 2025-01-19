import http.server
import socketserver
import os
import json

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        super().do_GET()

    def handle_games_api(self):
        """Handles the /api/games endpoint."""
        games_dir = os.path.join(os.getcwd(), 'games')
        games = []

        # Collect games dynamically from the games directory
        if os.path.exists(games_dir):
            for game_id, game_folder in enumerate(sorted(os.listdir(games_dir))):
                game_path = f'games/{game_folder}/index.html'
                if os.path.exists(os.path.join(games_dir, game_folder, 'index.html')):
                    games.append({'id': game_id, 'path': game_path})

        # Respond with the JSON
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(games).encode('utf-8'))

# Serve the current directory
os.chdir(os.path.dirname(__file__))

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://127.0.0.1:{PORT}")
    httpd.serve_forever()
