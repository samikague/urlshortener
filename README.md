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

2. With docker(in project root-directory)

```bash
docker build -t urlshortener . | docker run -p 8000:8000 urlshortner
```



# Roadmap:

VERSION 1
```
- Add more functionality (in process) (V1)
- Finish the project (V1)
```

VERSION 2

```
- Rewrite the project to the structure of several docker images under kubernetes management (V2)
```
