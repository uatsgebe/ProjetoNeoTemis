console.log("JS carregou");

// ===============================
// ELEMENTOS
// ===============================
const formLogin = document.getElementById("form-login");

const emailInput = document.getElementById("email");

const senhaInput = document.getElementById("senha");

const toggleSenha = document.getElementById("toggleSenha");


// ===============================
// LOGIN
// ===============================
const erroEmail =
    document.getElementById("erro-email");

const erroSenha =
    document.getElementById("erro-senha");


// ===============================
// MOSTRAR / OCULTAR SENHA
// ===============================
toggleSenha.addEventListener("click", function() {

    if (senhaInput.type === "password") {

        senhaInput.type = "text";

        toggleSenha.textContent = "Ocultar";

    } else {

        senhaInput.type = "password";

        toggleSenha.textContent = "Mostrar";

    }

});


// ===============================
// TERMOS DE USO E PRIVACIDADE
// ===============================
const form = document.querySelector("form");
const termos = document.getElementById("termos");
const erro = document.getElementById("erro-termos");

form.addEventListener("submit", function (e) {
  if (!termos.checked) {
    e.preventDefault(); // impede envio
    erro.style.display = "block"; // mostra mensagem
  } else {
    erro.style.display = "none"; // garante que some se estiver ok
  }
});

// opcional: some ao marcar
termos.addEventListener("change", function () {
  if (termos.checked) {
    erro.style.display = "none";
  }
});


// ===============================
// BOTÃO PERFIL
// ===============================
const perfilBotao = document.getElementById("perfilBotao");
const perfilDropdown = document.getElementById("perfilDropdown");

if (perfilBotao && perfilDropdown) {

    perfilBotao.addEventListener("click", function(event) {
        event.stopPropagation();
        perfilDropdown.classList.toggle("ativo");
    });

    document.addEventListener("click", function() {
        perfilDropdown.classList.remove("ativo");
    });

}

// ===============================
// DATA ATUAL (base.html)
// ===============================
const dataAtual = document.getElementById("dataAtual");

function atualizarDataHora() {

    if (!dataAtual) {
        return;
    }

    const agora = new Date();

    const opcoesData = {
        weekday: "long",
        day: "numeric",
        month: "long"
    };

    const dataFormatada = agora.toLocaleDateString(
        "pt-BR",
        opcoesData
    );

    const horaFormatada = agora.toLocaleTimeString(
        "pt-BR",
        {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit"
        }
    );
    
    const dataComMaiuscula =
    dataFormatada.charAt(0).toUpperCase() + dataFormatada.slice(1);

    dataAtual.textContent =
        `${dataComMaiuscula} | ${horaFormatada}`;
}

atualizarDataHora();

setInterval(atualizarDataHora, 1000);