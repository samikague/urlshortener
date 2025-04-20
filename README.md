[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7ddd267328ac4c82889770e0f3e42356)](https://app.codacy.com/gh/samikague/urlshortener/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
# UrlShortener - Yet another pet project.
I want to study alembic in more detail in conjunction with sqlalchemy and fastapi

Used in this project:
- SQLAlchemy
_ FastAPI
_ Alembic
- SQLite(with aiosqlite) / I was too lazy to do it on postgresql
- the list will be expanded btw

  
<b>Running</b>:

1. Default

```bash
python3 main.py
```

2. With docker

```bash
docker pull samikague/urlshortener | docker run -p 8000:8000 samikague/urlshortner
```

Build from sources

```bash
docker build -t samikague/urlshortener . | docker run -p 8000:8000 samikague/urlshortner
```



# Roadmap:

VERSION 1 - FINISHED
```
- Add more functionality (V1)
- Finish the project (V1)
```

VERSION 2

```
- Rewrite the project to the structure of several docker images under kubernetes management (V2)
```
