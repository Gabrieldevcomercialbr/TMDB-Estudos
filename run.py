#!/usr/bin/env python3
"""
Script de inicialização para o TMDB Explorer
Este script facilita a execução da aplicação Flask
"""

import os
import sys
from app import app

def main():
    """
    Função principal que executa a aplicação Flask
    """
    print("🎬 TMDB Explorer - Iniciando...")
    print("=" * 50)
    
    # Verifica se a chave da API está configurada
    api_key = os.getenv('TMDB_API_KEY')
    if not api_key or api_key == 'sua_chave_api_aqui':
        print("⚠️  ATENÇÃO: Chave da API do TMDB não configurada!")
        print("📝 Para configurar:")
        print("   1. Copie o arquivo 'env_example.txt' para '.env'")
        print("   2. Edite o arquivo '.env' e adicione sua chave da API")
        print("   3. Obtenha sua chave em: https://www.themoviedb.org/settings/api")
        print()
        print("🚀 A aplicação será iniciada em modo de demonstração...")
        print()
    
    # Configurações da aplicação
    host = '0.0.0.0'
    port = 5000
    debug = True
    
    print(f"🌐 Servidor iniciado em: http://localhost:{port}")
    print(f"🔧 Modo debug: {'Ativado' if debug else 'Desativado'}")
    print("=" * 50)
    print("📱 Pressione Ctrl+C para parar o servidor")
    print()
    
    try:
        # Executa a aplicação Flask
        app.run(host=host, port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n👋 Servidor parado pelo usuário")
    except Exception as e:
        print(f"❌ Erro ao iniciar o servidor: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 