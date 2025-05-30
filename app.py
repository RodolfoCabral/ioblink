from flask import redirect, url_for

def create_app():
    from src.main import create_app
    app = create_app()
    
    @app.route('/')
    def index():
        return redirect(url_for('auth.login'))
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
