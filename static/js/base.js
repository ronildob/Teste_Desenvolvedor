// Primeira Maiscula

    document.getElementById('nome').addEventListener('input', function() {
        let nomeInput = this.value;
        let nomeFormatado = formatarNome(nomeInput);
        this.value = nomeFormatado;
    });

    function formatarNome(nome) {
        let palavras = nome.split(' ');

        let nomeFormatado = palavras.map(function(palavra) {
            if (palavra.trim() !== '') {
                return palavra.charAt(0).toUpperCase() + palavra.slice(1).toLowerCase();
            }
            return '';
        });

        return nomeFormatado.join(' ');
    }


// Mostrar/Ocutar senha 

    function toggleSenhaVisibility() {
        var campoSenha = document.getElementById('password');
        var toggleSenhaIcon = document.getElementById('iconSenha');

        if (campoSenha.type === 'password') {
            campoSenha.type = 'text';
            toggleSenhaIcon.classList.remove('fa-eye');
            toggleSenhaIcon.classList.add('fa-eye-slash');
        } else {
            campoSenha.type = 'password';
            toggleSenhaIcon.classList.remove('fa-eye-slash');
            toggleSenhaIcon.classList.add('fa-eye');
        }
    }

 
// formatar e-mail tudo minusculo
    document.addEventListener('DOMContentLoaded', function() {
        let inputEmail = document.querySelector('input[id="email"]');
        if (inputEmail) {
            inputEmail.addEventListener('input', function() {
                let emailInput = this.value;
                let emailFormatado = emailInput.toLowerCase();
                this.value = emailFormatado;
            });
        }
    });

    

    