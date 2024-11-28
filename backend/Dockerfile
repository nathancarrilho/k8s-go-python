FROM golang:1.20
WORKDIR /app
COPY main.go .
RUN go mod init backend && go mod tidy
RUN go build -o main .
CMD ["./main"]
