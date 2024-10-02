const express = require('express');
const morgan = require('morgan');
const helmet = require('helmet');
const cors = require('cors');
const app = express();
const port = process.env.PORT || 3001; // Alterado para 3001

// Middleware
app.use(helmet());
app.use(cors());
app.use(morgan('combined'));
app.use(express.json());

// Rotas
app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get('/api', (req, res) => {
  res.json({ message: 'API funcionando!' });
});

// Tratamento de Erros
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Algo deu errado!');
});

const server = app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});

// Tratamento para encerrar o servidor corretamente
process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Processo encerrado');
  });
});

process.on('SIGINT', () => {
  server.close(() => {
    console.log('Processo interrompido');
  });
});

// Tratamento para lidar com erros de porta ocupada
server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') {
    console.error(`Porta ${port} já está em uso. Tentando outra porta...`);
    setTimeout(() => {
      server.close();
      server.listen(port + 1);
    }, 1000);
  } else {
    throw err;
  }
});
