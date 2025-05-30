// Arquivo JavaScript principal
document.addEventListener('DOMContentLoaded', function() {
    // Inicialização de componentes
    initSidebar();
    initUserDropdown();
    
    // Adicionar classes ativas com base na URL atual
    setActiveMenuItems();
});

// Inicialização da sidebar
function initSidebar() {
    const toggleBtn = document.getElementById('toggle-sidebar');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');
    
    if (toggleBtn && sidebar && mainContent) {
        toggleBtn.addEventListener('click', function() {
            sidebar.classList.toggle('collapsed');
            mainContent.classList.toggle('expanded');
        });
    }
    
    // Inicializar submenus
    const menuItems = document.querySelectorAll('.menu-item');
    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            const submenu = this.nextElementSibling;
            if (submenu && submenu.classList.contains('submenu')) {
                if (submenu.classList.contains('open')) {
                    submenu.classList.remove('open');
                } else {
                    // Fechar todos os submenus abertos
                    document.querySelectorAll('.submenu.open').forEach(menu => {
                        menu.classList.remove('open');
                    });
                    submenu.classList.add('open');
                }
            }
        });
    });
}

// Inicialização do dropdown do usuário
function initUserDropdown() {
    const userInfo = document.querySelector('.user-info');
    const userDropdown = document.getElementById('user-dropdown');
    
    if (userInfo && userDropdown) {
        userInfo.addEventListener('click', function(e) {
            e.stopPropagation();
            userDropdown.classList.toggle('show');
        });
        
        // Fechar dropdown ao clicar fora
        document.addEventListener('click', function(e) {
            if (userDropdown.classList.contains('show') && !userInfo.contains(e.target)) {
                userDropdown.classList.remove('show');
            }
        });
    }
}

// Definir itens de menu ativos com base na URL atual
function setActiveMenuItems() {
    const currentPath = window.location.pathname;
    
    // Encontrar e ativar o item de submenu correspondente
    const submenuItems = document.querySelectorAll('.submenu-item');
    submenuItems.forEach(item => {
        if (item.getAttribute('href') === currentPath) {
            item.classList.add('active');
            
            // Abrir o submenu pai
            const parentSubmenu = item.closest('.submenu');
            if (parentSubmenu) {
                parentSubmenu.classList.add('open');
                
                // Ativar o item de menu pai
                const parentMenuItem = parentSubmenu.previousElementSibling;
                if (parentMenuItem && parentMenuItem.classList.contains('menu-item')) {
                    parentMenuItem.classList.add('active');
                }
            }
        }
    });
}

// Funções para manipulação de alertas
function showAlert(message, type = 'info') {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${type}`;
    alertContainer.textContent = message;
    
    const pageContent = document.querySelector('.page-content');
    if (pageContent) {
        pageContent.prepend(alertContainer);
        
        // Auto-remover após 5 segundos
        setTimeout(() => {
            alertContainer.remove();
        }, 5000);
    }
}

// Funções para validação de formulários
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return false;
    
    let isValid = true;
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

// Funções para responsividade em dispositivos móveis
function checkMobileView() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');
    
    if (window.innerWidth <= 768) {
        sidebar.classList.add('collapsed');
        mainContent.classList.add('expanded');
    } else {
        sidebar.classList.remove('collapsed');
        mainContent.classList.remove('expanded');
    }
}

// Verificar tamanho da tela ao carregar e redimensionar
window.addEventListener('resize', checkMobileView);
window.addEventListener('load', checkMobileView);
