let chave = "sua_chave_da_API_aqui";

function colocarNaTela(dados) {
  console.log(dados);
  document.querySelector(".cidade").innerHTML = "Tempo em " + dados.nome;
  document.querySelector(".temp").innerHTML = Math.floor(dados.main.temp) + "°C";
  document.querySelector(".descricao").innerHTML = dados.weather[0].description;
  document.querySelector(".icone").src = "https://openweathermap.org/img/wn/" + dados.weather[0].icon + ".png";
  document.querySelector(".umidade").innerHTML = "Umidade: " + dados.main.humidity + "%";
}

async function buscarCidade(cidade) {
  let resultado = await fetch("http://localhost:3000/buscarCidade", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ cidade: cidade }),
  });
  if (!resultado.ok) {
    return;
  }
  resultado = await resultado.json();
  if (resultado) {
    colocarNaTela(resultado);
  } else {
    console.error("Erro ao buscar a cidade:", resultado.error);
  }
}

function cliqueiNoBotao() {
  let cidade = document.querySelector(".input-cidade").value;
  buscarCidade(cidade);
}
