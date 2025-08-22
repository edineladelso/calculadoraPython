let inText = document.querySelector("#inText");
let dvAnswer = document.querySelector("#answer");
const operadores = document.querySelectorAll(".operador"); // Elevado e Raiz
const btReset = document.querySelector("#btReset");
const backspace = document.querySelector("#btBackspace");
const btEnter = document.querySelector("#btEnter");
const scButtons = document.querySelectorAll(".scButtons button");

scButtons.forEach(function (val) {
    val.addEventListener("click", () => {
        inText.value += val.textContent;
    })
})

operadores.forEach( function(oper) {oper.addEventListener("click", () => {
    if (oper.classList.contains("b1Elevado")) {
        inText.value += "^";
    } else if (oper.classList.contains("b2Raiz")) {
        inText.value += "√";
    }
    inText.focus();
    inText.setSelectionRange(inText.value.length, inText.value.length);
    dvAnswer.textContent = ""; // Limpa a resposta ao inserir um operador
})})

btReset.addEventListener("click", () => {
    inText.value = ""
    dvAnswer.textContent = ""
})

backspace.addEventListener("click", () => {
    inText.value = inText.value.slice(0, -1)
})

btEnter.addEventListener("click", () => {
    dvAnswer.textContent = inText.value
})

inText.addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();
        btEnter.click();
    }

    if (event.key === "Backspace") {
        event.preventDefault();
        backspace.click();
    }

    if (event.key === "/") { }
});