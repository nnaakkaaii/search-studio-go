FROM golang:1.17-alpine

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY start.sh ./
COPY cmd ./cmd
COPY pkg ./pkg

RUN go build -o /docker-search-go ./cmd/main.go

EXPOSE 8001

CMD [ "/docker-search-go" ]