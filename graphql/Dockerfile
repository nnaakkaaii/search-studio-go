FROM golang:1.17-alpine

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY gqlgen.yml ./
COPY server.go ./
COPY graph ./graph
COPY models ./models

RUN go build -o /docker-graphql ./server.go

EXPOSE 8080

CMD [ "/docker-graphql" ]