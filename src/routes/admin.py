from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from src.models.user import User, db, bcrypt
from src.forms import UserForm
from datetime import datetime

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/users')
@login_required
def users():
    # Verificar se o usuário é administrador
    if current_user.role != 'admin':
        flash('Acesso negado. Você não tem permissão para acessar esta página.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    # Obter todos os usuários
    users = User.query.all()
    return render_template('admin/users.html', title='Gerenciar Usuários', users=users)

@admin_bp.route('/users/add', methods=['GET', 'POST'])
@login_required
def add_user():
    # Verificar se o usuário é administrador
    if current_user.role != 'admin':
        flash('Acesso negado. Você não tem permissão para acessar esta página.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    form = UserForm()
    if form.validate_on_submit():
        # Verificar se o email já está em uso
        if User.query.filter_by(email=form.email.data).first():
            flash('Este email já está em uso. Por favor, escolha outro.', 'danger')
            return render_template('admin/add_user.html', title='Adicionar Usuário', form=form)
        
        # Criar novo usuário
        user = User(
            name=form.name.data,
            email=form.email.data,
            role=form.role.data,
            is_active=form.is_active.data,
            created_at=datetime.utcnow()
        )
        user.set_password(form.password.data)
        
        # Salvar no banco de dados
        db.session.add(user)
        db.session.commit()
        
        flash(f'Usuário {form.name.data} adicionado com sucesso!', 'success')
        return redirect(url_for('admin.users'))
    
    return render_template('admin/add_user.html', title='Adicionar Usuário', form=form)

@admin_bp.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    # Verificar se o usuário é administrador
    if current_user.role != 'admin':
        flash('Acesso negado. Você não tem permissão para acessar esta página.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    # Obter o usuário a ser editado
    user = User.query.get_or_404(user_id)
    
    # Não permitir editar o próprio usuário master
    if user.email == 'rodolfocabral@outlook.com.br' and current_user.id != user.id:
        flash('Não é permitido editar o usuário master do sistema.', 'warning')
        return redirect(url_for('admin.users'))
    
    form = UserForm(obj=user)
    
    # Se o formulário for enviado e válido
    if form.validate_on_submit():
        # Verificar se o email já está em uso por outro usuário
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user and existing_user.id != user_id:
            flash('Este email já está em uso por outro usuário.', 'danger')
            return render_template('admin/edit_user.html', title='Editar Usuário', form=form, user=user)
        
        # Atualizar dados do usuário
        user.name = form.name.data
        user.email = form.email.data
        user.role = form.role.data
        user.is_active = form.is_active.data
        user.updated_at = datetime.utcnow()
        
        # Atualizar senha se fornecida
        if form.password.data:
            user.set_password(form.password.data)
        
        # Salvar alterações
        db.session.commit()
        
        flash(f'Usuário {user.name} atualizado com sucesso!', 'success')
        return redirect(url_for('admin.users'))
    
    # Limpar o campo de senha para não exibir no formulário
    form.password.data = ''
    
    return render_template('admin/edit_user.html', title='Editar Usuário', form=form, user=user)

@admin_bp.route('/users/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    # Verificar se o usuário é administrador
    if current_user.role != 'admin':
        flash('Acesso negado. Você não tem permissão para acessar esta página.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    # Obter o usuário a ser excluído
    user = User.query.get_or_404(user_id)
    
    # Não permitir excluir o próprio usuário ou o usuário master
    if user.id == current_user.id:
        flash('Você não pode excluir seu próprio usuário.', 'danger')
        return redirect(url_for('admin.users'))
    
    if user.email == 'rodolfocabral@outlook.com.br':
        flash('Não é permitido excluir o usuário master do sistema.', 'danger')
        return redirect(url_for('admin.users'))
    
    # Excluir usuário
    db.session.delete(user)
    db.session.commit()
    
    flash(f'Usuário {user.name} excluído com sucesso!', 'success')
    return redirect(url_for('admin.users'))

@admin_bp.route('/users/toggle/<int:user_id>', methods=['POST'])
@login_required
def toggle_user(user_id):
    # Verificar se o usuário é administrador
    if current_user.role != 'admin':
        flash('Acesso negado. Você não tem permissão para acessar esta página.', 'danger')
        return redirect(url_for('main.dashboard'))
    
    # Obter o usuário a ser ativado/desativado
    user = User.query.get_or_404(user_id)
    
    # Não permitir desativar o próprio usuário ou o usuário master
    if user.id == current_user.id:
        flash('Você não pode desativar seu próprio usuário.', 'danger')
        return redirect(url_for('admin.users'))
    
    if user.email == 'rodolfocabral@outlook.com.br' and not user.is_active:
        flash('Não é permitido desativar o usuário master do sistema.', 'danger')
        return redirect(url_for('admin.users'))
    
    # Alternar status do usuário
    user.is_active = not user.is_active
    db.session.commit()
    
    status = 'ativado' if user.is_active else 'desativado'
    flash(f'Usuário {user.name} {status} com sucesso!', 'success')
    return redirect(url_for('admin.users'))
