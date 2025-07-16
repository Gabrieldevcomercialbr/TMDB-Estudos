"""
Aplicação Flask para consumir a API do TMDB (The Movie Database)
Este projeto permite buscar filmes, ver detalhes e explorar o catálogo do TMDB
"""

import os
import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configuração da API do TMDB
TMDB_API_KEY = os.getenv('TMDB_API_KEY', 'sua_chave_api_aqui')  # Substitua pela sua chave da API
TMDB_BASE_URL = 'https://api.themoviedb.org/3'
TMDB_IMAGE_BASE_URL = 'https://image.tmdb.org/t/p/w500'

# Configuração da aplicação
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-secreta-padrao')

class TMDBService:
    """
    Classe para gerenciar as chamadas à API do TMDB
    """
    
    def __init__(self, api_key):
        """
        Inicializa o serviço com a chave da API
        
        Args:
            api_key (str): Chave da API do TMDB
        """
        self.api_key = api_key
        self.base_url = TMDB_BASE_URL
        self.image_base_url = TMDB_IMAGE_BASE_URL
    
    def get_popular_movies(self, page=1):
        """
        Busca filmes populares
        
        Args:
            page (int): Número da página (padrão: 1)
            
        Returns:
            dict: Dados dos filmes populares
        """
        url = f"{self.base_url}/movie/popular"
        params = {
            'api_key': self.api_key,
            'language': 'pt-BR',
            'page': page
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao buscar filmes populares: {e}")
            return None
    
    def search_movies(self, query, page=1):
        """
        Busca filmes por termo de pesquisa
        
        Args:
            query (str): Termo de pesquisa
            page (int): Número da página (padrão: 1)
            
        Returns:
            dict: Resultados da busca
        """
        url = f"{self.base_url}/search/movie"
        params = {
            'api_key': self.api_key,
            'language': 'pt-BR',
            'query': query,
            'page': page
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao buscar filmes: {e}")
            return None
    
    def get_movie_details(self, movie_id):
        """
        Busca detalhes de um filme específico
        
        Args:
            movie_id (int): ID do filme
            
        Returns:
            dict: Detalhes do filme
        """
        url = f"{self.base_url}/movie/{movie_id}"
        params = {
            'api_key': self.api_key,
            'language': 'pt-BR',
            'append_to_response': 'credits,videos,images'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao buscar detalhes do filme: {e}")
            return None
    
    def get_top_rated_movies(self, page=1):
        """
        Busca filmes mais bem avaliados
        
        Args:
            page (int): Número da página (padrão: 1)
            
        Returns:
            dict: Dados dos filmes mais bem avaliados
        """
        url = f"{self.base_url}/movie/top_rated"
        params = {
            'api_key': self.api_key,
            'language': 'pt-BR',
            'page': page
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao buscar filmes mais bem avaliados: {e}")
            return None
    
    def get_now_playing_movies(self, page=1):
        """
        Busca filmes em cartaz
        
        Args:
            page (int): Número da página (padrão: 1)
            
        Returns:
            dict: Dados dos filmes em cartaz
        """
        url = f"{self.base_url}/movie/now_playing"
        params = {
            'api_key': self.api_key,
            'language': 'pt-BR',
            'page': page
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Erro ao buscar filmes em cartaz: {e}")
            return None

# Inicializa o serviço TMDB
tmdb_service = TMDBService(TMDB_API_KEY)

@app.route('/')
def index():
    """
    Página inicial - mostra filmes populares
    """
    page = request.args.get('page', 1, type=int)
    movies_data = tmdb_service.get_popular_movies(page)
    
    if movies_data:
        movies = movies_data.get('results', [])
        total_pages = movies_data.get('total_pages', 1)
        current_page = movies_data.get('page', 1)
    else:
        movies = []
        total_pages = 1
        current_page = 1
    
    # Cálculo dos limites de paginação
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)
    
    return render_template('index.html', 
                         movies=movies, 
                         current_page=current_page, 
                         total_pages=total_pages,
                         start_page=start_page,
                         end_page=end_page,
                         image_base_url=TMDB_IMAGE_BASE_URL)

@app.route('/search')
def search():
    """
    Página de busca de filmes
    """
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    
    if query:
        search_data = tmdb_service.search_movies(query, page)
        if search_data:
            movies = search_data.get('results', [])
            total_pages = search_data.get('total_pages', 1)
            current_page = search_data.get('page', 1)
            total_results = search_data.get('total_results', 0)
        else:
            movies = []
            total_pages = 1
            current_page = 1
            total_results = 0
    else:
        movies = []
        total_pages = 1
        current_page = 1
        total_results = 0
    
    # Cálculo dos limites de paginação
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)
    
    return render_template('search.html', 
                         movies=movies, 
                         query=query,
                         current_page=current_page, 
                         total_pages=total_pages,
                         total_results=total_results,
                         start_page=start_page,
                         end_page=end_page,
                         image_base_url=TMDB_IMAGE_BASE_URL)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    """
    Página de detalhes de um filme específico
    
    Args:
        movie_id (int): ID do filme
    """
    movie_data = tmdb_service.get_movie_details(movie_id)
    
    if movie_data:
        return render_template('movie_detail.html', 
                             movie=movie_data,
                             image_base_url=TMDB_IMAGE_BASE_URL)
    else:
        return render_template('error.html', message="Filme não encontrado"), 404

@app.route('/top-rated')
def top_rated():
    """
    Página de filmes mais bem avaliados
    """
    page = request.args.get('page', 1, type=int)
    movies_data = tmdb_service.get_top_rated_movies(page)
    
    if movies_data:
        movies = movies_data.get('results', [])
        total_pages = movies_data.get('total_pages', 1)
        current_page = movies_data.get('page', 1)
    else:
        movies = []
        total_pages = 1
        current_page = 1
    
    # Cálculo dos limites de paginação
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)
    
    return render_template('top_rated.html', 
                         movies=movies, 
                         current_page=current_page, 
                         total_pages=total_pages,
                         start_page=start_page,
                         end_page=end_page,
                         image_base_url=TMDB_IMAGE_BASE_URL)

@app.route('/now-playing')
def now_playing():
    """
    Página de filmes em cartaz
    """
    page = request.args.get('page', 1, type=int)
    movies_data = tmdb_service.get_now_playing_movies(page)
    
    if movies_data:
        movies = movies_data.get('results', [])
        total_pages = movies_data.get('total_pages', 1)
        current_page = movies_data.get('page', 1)
    else:
        movies = []
        total_pages = 1
        current_page = 1
    
    # Cálculo dos limites de paginação
    start_page = max(1, current_page - 2)
    end_page = min(total_pages, current_page + 2)
    
    return render_template('now_playing.html', 
                         movies=movies, 
                         current_page=current_page, 
                         total_pages=total_pages,
                         start_page=start_page,
                         end_page=end_page,
                         image_base_url=TMDB_IMAGE_BASE_URL)

@app.errorhandler(404)
def not_found(error):
    """
    Página de erro 404
    """
    return render_template('error.html', message="Página não encontrada"), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Página de erro 500
    """
    return render_template('error.html', message="Erro interno do servidor"), 500

if __name__ == '__main__':
    # Verifica se a chave da API está configurada
    if TMDB_API_KEY == 'sua_chave_api_aqui':
        print("⚠️  ATENÇÃO: Configure sua chave da API do TMDB no arquivo .env")
        print("   Obtenha sua chave em: https://www.themoviedb.org/settings/api")
    
    # Executa a aplicação em modo de desenvolvimento
    app.run(debug=True, host='0.0.0.0', port=5000) 