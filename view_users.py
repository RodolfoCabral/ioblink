# Visualizador de Usuários do Sistema

import sqlite3

def view_users():
    try:
        conn = sqlite3.connect('site.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, email, role, is_active FROM users")
        users = cursor.fetchall()
        
        print("\n=== Usuários Cadastrados no Sistema ===")
        print("ID | Nome | Email | Função | Ativo")
        print("-" * 70)
        for user in users:
            print(f"{user[0]} | {user[1]} | {user[2]} | {user[3]} | {'Sim' if user[4] else 'Não'}")
        
        conn.close()
        print("\nPara adicionar novos usuários, acesse o sistema como administrador.")
        
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        print("Certifique-se de que o arquivo site.db foi criado (execute a aplicação pelo menos uma vez).")

if __name__ == "__main__":
    view_users()
