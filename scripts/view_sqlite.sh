docker run -it --rm \
    -p 8180:8080 \
    -v .:/data \
    -e SQLITE_DATABASE="db.sqlite3" \
    coleifer/sqlite-web