# TMDB Explorer

Uma aplicação web Flask que consome a API do TMDB (The Movie Database) para exibir informações sobre filmes, incluindo detalhes, elenco, trailers e imagens.

## 🎬 Funcionalidades

- **Filmes Populares**: Visualize os filmes mais populares do momento
- **Filmes Mais Avaliados**: Descubra os filmes com melhores avaliações
- **Filmes em Cartaz**: Veja os filmes atualmente em exibição
- **Busca de Filmes**: Pesquise filmes por título
- **Detalhes Completos**: Informações detalhadas de cada filme
- **Elenco**: Lista do elenco principal
- **Trailers**: Visualização de trailers do YouTube
- **Imagens**: Galeria de imagens dos filmes
- **Design Responsivo**: Interface moderna e adaptável a diferentes dispositivos

## 🚀 Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Ícones**: Font Awesome
- **API**: The Movie Database (TMDB)
- **Gerenciamento de Dependências**: pip

## 📋 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Chave de API do TMDB

## 🔧 Instalação

1. **Clone o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd TMDB
   ```

2. **Crie um ambiente virtual** (recomendado):
   ```bash
   python -m venv venv
   
   # No Windows:
   venv\Scripts\activate
   
   # No Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   - Copie o arquivo `env_example.txt` para `.env`
   - Edite o arquivo `.env` e adicione sua chave da API do TMDB

   ```bash
   # No Windows:
   copy env_example.txt .env
   
   # No Linux/Mac:
   cp env_example.txt .env
   ```

5. **Obtenha sua chave da API do TMDB**:
   - Acesse: https://www.themoviedb.org/settings/api
   - Crie uma conta gratuita
   - Solicite uma chave de API
   - Adicione a chave no arquivo `.env`:

   ```
   TMDB_API_KEY=sua_chave_api_aqui
   ```

## 🏃‍♂️ Como Executar

1. **Ative o ambiente virtual** (se estiver usando):
   ```bash
   # No Windows:
   venv\Scripts\activate
   
   # No Linux/Mac:
   source venv/bin/activate
   ```

2. **Execute a aplicação**:
   ```bash
   python app.py
   ```

3. **Acesse no navegador**:
   ```
   http://localhost:5000
   ```

## 📁 Estrutura do Projeto

```
TMDB/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── env_example.txt       # Exemplo de variáveis de ambiente
├── README.md             # Este arquivo
└── templates/            # Templates HTML
    ├── base.html         # Template base
    ├── index.html        # Página inicial (filmes populares)
    ├── search.html       # Página de busca
    ├── movie_detail.html # Página de detalhes do filme
    ├── top_rated.html    # Filmes mais bem avaliados
    ├── now_playing.html  # Filmes em cartaz
    └── error.html        # Página de erro
```

## 🔍 Como Usar

### Navegação Principal
- **Filmes Populares**: Página inicial com os filmes mais populares
- **Mais Avaliados**: Filmes com melhores avaliações
- **Em Cartaz**: Filmes atualmente em exibição
- **Busca**: Campo de pesquisa na barra de navegação

### Funcionalidades
1. **Visualizar Filmes**: Clique em qualquer filme para ver detalhes
2. **Buscar**: Use o campo de busca para encontrar filmes específicos
3. **Navegar**: Use a paginação para ver mais filmes
4. **Ver Detalhes**: Acesse informações completas, elenco, trailers e imagens

## 🎨 Características do Design

- **Interface Moderna**: Design limpo e profissional
- **Responsivo**: Adaptável a desktop, tablet e mobile
- **Animações**: Efeitos hover e transições suaves
- **Ícones**: Font Awesome para melhor experiência visual
- **Gradientes**: Background com gradiente moderno
- **Cards**: Layout em cards para melhor organização

## 🔧 Configuração Avançada

### Variáveis de Ambiente
- `TMDB_API_KEY`: Sua chave da API do TMDB (obrigatória)
- `SECRET_KEY`: Chave secreta do Flask (opcional)

### Personalização
Você pode personalizar:
- Cores e estilos no arquivo `templates/base.html`
- Número de filmes por página
- Tamanho das imagens
- Idioma dos dados (padrão: pt-BR)

## 🐛 Solução de Problemas

### Erro de API
- Verifique se a chave da API está correta
- Confirme se a chave tem permissões adequadas
- Verifique a conectividade com a internet

### Erro de Dependências
- Certifique-se de que o ambiente virtual está ativo
- Reinstale as dependências: `pip install -r requirements.txt`

### Erro de Porta
- Se a porta 5000 estiver ocupada, altere no arquivo `app.py`
- Ou use: `python app.py --port 8000`

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas:
1. Verifique a documentação da API do TMDB
2. Consulte os logs da aplicação
3. Abra uma issue no repositório

## 🔗 Links Úteis

- [The Movie Database (TMDB)](https://www.themoviedb.org/)
- [Documentação da API TMDB](https://developers.themoviedb.org/3)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)

---

**Desenvolvido com ❤️ usando Flask e TMDB API** 