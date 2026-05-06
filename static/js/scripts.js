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