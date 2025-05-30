from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from src.forms import LoginForm, RequestAccessForm
from src.models.user import User, db
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Login falhou. Por favor, verifique email e senha.', 'danger')
    
    return render_template('auth/login.html', title='Login', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth_bp.route('/request_access', methods=['GET', 'POST'])
def request_access():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = RequestAccessForm()
    if form.validate_on_submit():
        # Preparar o conteúdo do email
        admin_email = "rodolfocabral@outlook.com.br"
        subject = "Nova solicitação de acesso ao Sistema de Gestão de OS"
        
        # Criar mensagem
        msg = MIMEMultipart()
        msg['From'] = form.email.data
        msg['To'] = admin_email
        msg['Subject'] = subject
        
        # Corpo do email
        body = f"""
        Nova solicitação de acesso ao Sistema de Gestão de OS:
        
        Nome completo: {form.name.data}
        Telefone: {form.phone.data}
        Email: {form.email.data}
        Número do pedido: {form.order_number.data if form.order_number.data else 'Não informado'}
        
        Para criar o acesso, acesse o sistema e vá em Parâmetros > Usuários.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            # Aqui você pode configurar o envio de email
            # Como estamos em ambiente de desenvolvimento, apenas simulamos o envio
            # Em produção, você usaria um serviço SMTP real
            
            # Exemplo de código para envio real (comentado):
            # server = smtplib.SMTP('smtp.gmail.com', 587)
            # server.starttls()
            # server.login("seu_email@gmail.com", "sua_senha")
            # server.send_message(msg)
            # server.quit()
            
            flash('Solicitação de acesso enviada com sucesso! Entraremos em contato em breve.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash(f'Erro ao enviar solicitação: {str(e)}', 'danger')
    
    return render_template('auth/request_access.html', title='Solicitar Acesso', form=form)

# Removendo as rotas de redefinição de senha para evitar erros
# @auth_bp.route('/reset_password_request', methods=['GET', 'POST'])
# def reset_password_request():
#     pass

# @auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
#     pass
