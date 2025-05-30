#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Script para adicionar novos usuários ao sistema
import sqlite3
import sys

try:
    import bcrypt
except ImportError:
    print("Instalando dependência bcrypt...")
    import subprocess
    subprocess.call(["pip", "install", "bcrypt"])
    import bcrypt

def add_user(name, email, password, role='user', is_active=True):
    try:
        # Conectar ao banco de dados
        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()
        
        # Verificar se o usuário já existe
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        if cursor.fetchone():
            print(f"Erro: O email {email} já está em uso.")
            conn.close()
            return False
        
        # Gerar hash da senha
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Inserir novo usuário
        cursor.execute(
            "INSERT INTO users (name, email, password_hash, role, is_active) VALUES (?, ?, ?, ?, ?)",
            (name, email, password_hash, role, is_active)
        )
        
        # Salvar alterações
        conn.commit()
        conn.close()
        
        print(f"Usuário {name} ({email}) cadastrado com sucesso!")
        return True
        
    except Exception as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return False

if __name__ == "__main__":
    print("=== Cadastro de Novo Usuário ===")
    name = input("Nome completo: ")
    email = input("Email: ")
    password = input("Senha: ")
    role = input("Função (admin/user) [padrão: user]: ") or "user"
    is_active_input = input("Usuário ativo? (s/n) [padrão: s]: ").lower() or "s"
    is_active = is_active_input.startswith("s")
    
    add_user(name, email, password, role, is_active)
