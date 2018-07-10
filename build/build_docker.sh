HASH="${HASH:-local}"
docker build -t commands-base:$HASH .
