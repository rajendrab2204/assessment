# Use the official Golang image
FROM alpine:latest as builder

RUN apk add gdb go
# Set the working directory
WORKDIR /app

# Copy the Go source code and the necessary files
COPY golang/ .
COPY start.sh .
# Build the Go application
#RUN go build -o server server.go
RUN go build -gcflags="all=-N -l" -o server server.go && ls -l

# Final stage: create a small image for the application
FROM alpine:latest
RUN apk add go
# Set the working directory
WORKDIR /app

# Copy the server binary and necessary files from the builder
COPY --from=builder /app/server .
COPY --from=builder /app/file-dev.txt .
COPY --from=builder /app/file-prod.txt .
COPY --from=builder /app/start.sh .

RUN chmod +x /app/server
RUN chmod +x /app/start.sh
# Expose the port the app runs on
EXPOSE 8080

# Command to run the executable
CMD ["./start.sh"]
