const button = document.querySelector("button");
const modal = document.querySelector("dialog");
const buttonClose = document.querySelector("dialog button");

button.onclick = function() {
    console.log("Botão clicado");
    modal.showModal();
}

buttonClose.onclick = function() {
    console.log("Botão de fechar clicado");
    modal.close();
}
