# WP_Blog_CommentAI

WP_Blog_CommentAI é um repositório que foi projetado para adicionar automaticamente um comentário gerado por AI à sua publicação do blog WordPress. Isso é feito por meio da API da OpenAI.

## Funcionalidades

Este projeto foi desenvolvido para gerar comentários com base no título de sua postagem do blog. Ao adicionar a URL do seu blog e a chave da API da OpenAI nos campos apropriados no arquivo `settings.py`, o programa irá automaticamente obter o título da postagem do blog e gerar um comentário relevante para a postagem.

## Configuração

### Pré-requisitos
- Python
- Selenium
- Chave da API da OpenAI

### Instalação

1. Clone o repositório
\`\`\`
git clone https://github.com/seu_usuario/WP_Blog_CommentAI.git
\`\`\`
2. Entre na pasta do repositório
\`\`\`
cd WP_Blog_CommentAI
\`\`\`
3. Instale as dependências
\`\`\`
pip install -r requirements.txt
\`\`\`

### Configurando o `settings.py`

No arquivo `settings.py`, você encontrará duas constantes: `MAIN_BLOG_URL` e `OPENAI_API_KEY`. 

- `MAIN_BLOG_URL`: Adicione a URL do seu blog WordPress entre as aspas.
- `OPENAI_API_KEY`: Adicione sua chave da API da OpenAI entre as aspas.

\`\`\`python
MAIN_BLOG_URL = "https://seublog.wordpress.com"
OPENAI_API_KEY = "sua-chave-openai"
\`\`\`

Depois de adicionar essas informações, você está pronto para começar a usar o WP_Blog_CommentAI.

## Uso

Após configurar as informações do `settings.py`, você pode executar o script principal para gerar e postar um comentário no seu blog WordPress.

\`\`\`python
python main.py
\`\`\`

## Nota

Esta é uma versão de debug e, portanto, usa o Selenium. Estou atualmente trabalhando em uma versão mais avançada e automatizada, então fique atento para atualizações futuras!

## Contribuição

Sinta-se à vontade para fazer um fork do repositório e propor alterações. Todos os contribuidores são bem-vindos!
