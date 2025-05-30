from flask import Flask
from flask_login import LoginManager
from src.models.user import db, User, bcrypt
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'desenvolvimento-temporario-chave-secreta')
    
    # Configuração do banco de dados SQLite (em vez de MySQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicialização das extensões
    db.init_app(app)
    bcrypt.init_app(app)
    
    # Configuração do Login Manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, faça login para acessar esta página.'
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Registro dos blueprints
    from src.routes.auth import auth_bp
    from src.routes.main import main_bp
    from src.routes.admin import admin_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    
    # Criação das tabelas do banco de dados e usuário master
    with app.app_context():
        db.create_all()
        
        # Verificar se o usuário master já existe
        master_email = "rodolfocabral@outlook.com.br"
        if not User.query.filter_by(email=master_email).first():
            # Criar usuário master
            master_user = User(
                name="Administrador Master",
                email=master_email,
                role="admin",
                is_active=True
            )
            master_user.set_password("101002Rm#")
            db.session.add(master_user)
            db.session.commit()
            print("Usuário master criado com sucesso!")
    
    return app
