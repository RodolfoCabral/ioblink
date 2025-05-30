# Instruções para o Sistema de Gestão de Ordens de Serviço

## Visão Geral
Este é um mini SaaS para geração e controle de ordens de serviço em ativos, desenvolvido com Flask. O sistema possui autenticação segura, menu lateral com 8 módulos principais e seus respectivos subitens, além de uma área superior com logo e informações do usuário.

## Estrutura do Projeto
```
app/
├── venv/                  # Ambiente virtual Python
├── src/                   # Código-fonte principal
│   ├── models/            # Modelos de banco de dados
│   ├── routes/            # Rotas da aplicação
│   ├── static/            # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── css/           # Folhas de estilo
│   │   ├── js/            # Scripts JavaScript
│   │   └── img/           # Imagens e logo
│   ├── templates/         # Templates HTML
│   └── main.py            # Arquivo principal da aplicação
├── app.py                 # Ponto de entrada da aplicação
└── requirements.txt       # Dependências do projeto
```

## Configuração Inicial

1. **Ambiente Virtual**: O projeto já vem com um ambiente virtual configurado em `venv/`.

2. **Banco de Dados**: O sistema está configurado para usar MySQL. As configurações podem ser ajustadas em `src/main.py`.

3. **Dependências**: Todas as dependências necessárias estão listadas em `requirements.txt`.

## Executando o Sistema

1. Ative o ambiente virtual:
   ```
   source venv/bin/activate
   ```

2. Execute a aplicação:
   ```
   python app.py
   ```

3. Acesse o sistema em seu navegador:
   ```
   http://localhost:5000
   ```

## Personalizando o Sistema

### Substituindo a Logo
A logo temporária está localizada em `src/static/img/logo.png`. Para substituí-la:

1. Prepare sua nova logo com dimensões similares (recomendado: 200x80px)
2. Substitua o arquivo `logo.png` mantendo o mesmo nome
3. Reinicie a aplicação para ver as mudanças

### Personalizando Cores
As cores principais do sistema (laranja e preto) podem ser ajustadas no arquivo `src/static/css/style.css`, modificando as variáveis CSS no início do arquivo:

```css
:root {
  --primary-color: #ff7b00;    /* Cor laranja principal */
  --primary-light: #ff9a3c;    /* Variação clara do laranja */
  --primary-dark: #e56c00;     /* Variação escura do laranja */
  --secondary-color: #212121;  /* Cor preta principal */
  --secondary-light: #484848;  /* Variação clara do preto */
  --secondary-dark: #000000;   /* Variação escura do preto */
  /* ... outras variáveis ... */
}
```

## Funcionalidades Principais

### Autenticação
- Login seguro com email e senha
- Registro de novos usuários
- Recuperação de senha
- Proteção de rotas com login obrigatório

### Menu Lateral
O sistema possui 8 módulos principais, cada um com 3 subitens:

1. **Relatórios**
   - Diários
   - Mensais
   - Personalizados

2. **KPIs**
   - Desempenho
   - Manutenção
   - Custo

3. **Cadastro de Ativos**
   - Cadastrar
   - Listar
   - Categorias

4. **Plano de Manutenção**
   - Preventiva
   - Corretiva
   - Preditiva

5. **Abrir Chamado**
   - Novo
   - Em Aberto
   - Histórico

6. **Programação**
   - Diária
   - Semanal
   - Mensal

7. **Materiais**
   - Inventário
   - Solicitações
   - Fornecedores

8. **Parâmetros**
   - Usuários
   - Permissões
   - Sistema

### Área Superior
- Logo do sistema (personalizável)
- Informações do usuário logado
- Menu dropdown com opções:
  - Minha Conta
  - Redefinir Senha
  - Suporte
  - Sair

## Segurança
- Senhas armazenadas com hash bcrypt
- Proteção contra CSRF em formulários
- Validação de dados de entrada
- Sessões seguras com Flask-Login

## Próximos Passos Recomendados
1. Criar usuários administradores iniciais
2. Personalizar a logo conforme sua identidade visual
3. Implementar as funcionalidades específicas de cada módulo
4. Configurar backup regular do banco de dados

## Suporte
Para qualquer dúvida ou problema, entre em contato com o desenvolvedor.
