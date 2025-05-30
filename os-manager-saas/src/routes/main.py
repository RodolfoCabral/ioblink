from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from src.models.user import User, db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('auth.login'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

@main_bp.route('/relatorios/diarios')
@login_required
def relatorios_diarios():
    return render_template('dashboard.html', title='Relatórios Diários')

@main_bp.route('/relatorios/mensais')
@login_required
def relatorios_mensais():
    return render_template('dashboard.html', title='Relatórios Mensais')

@main_bp.route('/relatorios/personalizados')
@login_required
def relatorios_personalizados():
    return render_template('dashboard.html', title='Relatórios Personalizados')

@main_bp.route('/kpis/desempenho')
@login_required
def kpis_desempenho():
    return render_template('dashboard.html', title='KPIs de Desempenho')

@main_bp.route('/kpis/manutencao')
@login_required
def kpis_manutencao():
    return render_template('dashboard.html', title='KPIs de Manutenção')

@main_bp.route('/kpis/custo')
@login_required
def kpis_custo():
    return render_template('dashboard.html', title='KPIs de Custo')

@main_bp.route('/ativos/cadastrar')
@login_required
def ativos_cadastrar():
    return render_template('dashboard.html', title='Cadastrar Ativos')

@main_bp.route('/ativos/listar')
@login_required
def ativos_listar():
    return render_template('dashboard.html', title='Listar Ativos')

@main_bp.route('/ativos/categorias')
@login_required
def ativos_categorias():
    return render_template('dashboard.html', title='Categorias de Ativos')

@main_bp.route('/manutencao/preventiva')
@login_required
def manutencao_preventiva():
    return render_template('dashboard.html', title='Manutenção Preventiva')

@main_bp.route('/manutencao/corretiva')
@login_required
def manutencao_corretiva():
    return render_template('dashboard.html', title='Manutenção Corretiva')

@main_bp.route('/manutencao/preditiva')
@login_required
def manutencao_preditiva():
    return render_template('dashboard.html', title='Manutenção Preditiva')

@main_bp.route('/chamados/novo')
@login_required
def chamados_novo():
    return render_template('dashboard.html', title='Novo Chamado')

@main_bp.route('/chamados/abertos')
@login_required
def chamados_abertos():
    return render_template('dashboard.html', title='Chamados em Aberto')

@main_bp.route('/chamados/historico')
@login_required
def chamados_historico():
    return render_template('dashboard.html', title='Histórico de Chamados')

@main_bp.route('/programacao/diaria')
@login_required
def programacao_diaria():
    return render_template('dashboard.html', title='Programação Diária')

@main_bp.route('/programacao/semanal')
@login_required
def programacao_semanal():
    return render_template('dashboard.html', title='Programação Semanal')

@main_bp.route('/programacao/mensal')
@login_required
def programacao_mensal():
    return render_template('dashboard.html', title='Programação Mensal')

@main_bp.route('/materiais/inventario')
@login_required
def materiais_inventario():
    return render_template('dashboard.html', title='Inventário de Materiais')

@main_bp.route('/materiais/solicitacoes')
@login_required
def materiais_solicitacoes():
    return render_template('dashboard.html', title='Solicitações de Materiais')

@main_bp.route('/materiais/fornecedores')
@login_required
def materiais_fornecedores():
    return render_template('dashboard.html', title='Fornecedores de Materiais')

@main_bp.route('/parametros/usuarios')
@login_required
def parametros_usuarios():
    if current_user.role != 'admin':
        flash('Acesso negado. Você não tem permissão para acessar esta página.', 'danger')
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('admin.users'))

@main_bp.route('/parametros/permissoes')
@login_required
def parametros_permissoes():
    if current_user.role != 'admin':
        flash('Acesso negado. Você não tem permissão para acessar esta página.', 'danger')
        return redirect(url_for('main.dashboard'))
    return render_template('dashboard.html', title='Permissões do Sistema')

@main_bp.route('/parametros/sistema')
@login_required
def parametros_sistema():
    if current_user.role != 'admin':
        flash('Acesso negado. Você não tem permissão para acessar esta página.', 'danger')
        return redirect(url_for('main.dashboard'))
    return render_template('dashboard.html', title='Configurações do Sistema')

@main_bp.route('/minha-conta')
@login_required
def minha_conta():
    return render_template('dashboard.html', title='Minha Conta')

@main_bp.route('/suporte')
@login_required
def suporte():
    return render_template('dashboard.html', title='Suporte')
