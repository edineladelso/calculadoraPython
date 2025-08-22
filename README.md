<p align="left"> <img src="https://komarev.com/ghpvc/?username=edineladelso&color=yellow" alt="Profile views" /> </p>
<h1 align="center">Calculadora Python</h1>

Uma calculadora simples, interativa e extensível feita em Python, capaz de realizar operações matemáticas básicas e avançadas.  
**Agora com interface web (frontend) e backend em Python (API Flask), além da interface de terminal!**

<p>
   link do repositorio
  <a href="https://github.com/edineladelso/calculadoraPython" target="_blank">
    https://github.com/edineladelso/calculadoraPython
  </a>
</p>

## Funcionalidades

- Adição (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`)
- Potenciação (`^`)
- Radiciação (`r` ou `√`)

## Evolução do Projeto

O projeto foi expandido para incluir:

- **Frontend Web:** Interface gráfica moderna feita em HTML, CSS e JavaScript.
- **Backend Flask:** API REST em Python que recebe expressões matemáticas via JSON, calcula e retorna o resultado.
- **Reaproveitamento do Código:** O backend utiliza o mesmo código de cálculo da versão terminal, garantindo compatibilidade e facilidade de manutenção.

## Como Usar

### 1. Interface Terminal (original)

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/edineladelso/calculadoraPython.git
   cd calculadoraPython
   ```

2. **Execute o programa:**

   ```bash
   python3 main.py
   ```

3. **Digite sua expressão matemática:**
   - Exemplos:
     - `2+3`
     - `10-4`
     - `5*6`
     - `8/2`
     - `2^3` (potência: 2 elevado a 3)
     - `9r2` (raiz quadrada de 9)

4. **Para encerrar:**
   - Digite `AC` ou `P` e pressione Enter.

### 2. Interface Web (nova)

1. **Instale as dependências do backend:**

   ```bash
   cd backend
   pip install flask flask-cors
   ```

2. **Execute o backend Flask:**

   ```bash
   python3 app.py
   ```

3. **Abra o arquivo `frontend/index.html` em seu navegador.**

4. **Digite sua expressão matemática na interface web e veja o resultado instantaneamente!**

   - O frontend envia a expressão para o backend via JSON.
   - O backend calcula e retorna o resultado para o frontend.

## Exemplo de Uso

### Terminal

```
==========================================================
==                 EIS A SUA CALCULADORA                ==
==========================================================
==                                                      ==
==                       REGRAS:                        ==
==  >>   Para encerrar a calculadora Digite: AC ou P    ==
==  >>   Insira os Valores de forma normal ex: 1+2      ==
==                                                      ==
==========================================================
==                                                      ==
==  : 2+2
==              4
==  : 9r2
==              3.0
==  : AC
```

### Web

- Interface intuitiva, basta digitar a expressão e clicar em "Enter".
- Suporte aos mesmos operadores da versão terminal.

## Estrutura do Projeto

- `main.py`: Interface principal do usuário (terminal).
- `calc.py`: Lógica das operações matemáticas (usada pelo terminal e pelo backend).
- `backend/app.py`: API Flask que recebe expressões e retorna resultados.
- `frontend/`: Interface web (HTML, CSS, JS).

## Requisitos

- Python 3.x
- Flask e Flask-CORS (para backend)
- Navegador web moderno (para frontend)

## Personalização

Você pode adicionar novas operações matemáticas facilmente editando o arquivo `calc.py`.  
O frontend pode ser customizado em `frontend/`.

## Licença

Este projeto está sob a licença MIT.

## Autor

<p>
   Feito por
  <a href="https://github.com/edineladelso" target="_blank">
    Edinel Mario Adelso
  </a>
 <a href="https://github.com/edineladelso/" target="_blank">
    <img align="center" src="https://img.shields.io/badge/-edineladelso-05122A?style=flat&logo=github" alt="github"/>
  </a>
</p>
