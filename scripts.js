const express = require('express');
const app = express();
const port = 3000;

let cidades = [
  { id: 1, nome: 'Rio de Janeiro', temperatura: 28, descricao: 'Nuvens Dispersas', umidade: 70 },
  { id: 2, nome: 'São Paulo', temperatura: 25, descricao: 'Ensolarado', umidade: 60 },
  { id: 3, nome: 'Belo Horizonte', temperatura: 30, descricao: 'Chuva', umidade: 80 }
];

app.use(express.json());

// Operação GET para obter todas as cidades
app.get('/cidades', (req, res) => {
  res.json(cidades);
});

// Operação GET para obter uma cidade específica
app.get('/cidades/:id', (req, res) => {
  const cidade = cidades.find(c => c.id === parseInt(req.params.id));
  if (!cidade) return res.status(404).send('Cidade não encontrada');
  res.json(cidade);
});

// Operação POST para adicionar uma nova cidade
