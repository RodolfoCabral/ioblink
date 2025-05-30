from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from src.models.user import User

class RegistrationForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este email já está em uso. Por favor, escolha outro.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class RequestAccessForm(FlaskForm):
    name = StringField('Nome Completo', validators=[DataRequired(), Length(min=2, max=100)])
    phone = StringField('Telefone', validators=[DataRequired(), Length(min=10, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    order_number = StringField('Número do Pedido (opcional)', validators=[Optional(), Length(max=50)])
    submit = SubmitField('Solicitar Acesso')

class UserForm(FlaskForm):
    name = StringField('Nome Completo', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha (deixe em branco para manter a atual)', validators=[Optional(), Length(min=6)])
    role = SelectField('Função', choices=[('user', 'Usuário'), ('admin', 'Administrador')], validators=[DataRequired()])
    is_active = BooleanField('Usuário Ativo')
    submit = SubmitField('Salvar')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Solicitar Redefinição de Senha')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Nova Senha', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Nova Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Redefinir Senha')
