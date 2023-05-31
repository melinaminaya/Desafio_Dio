#Desafio de Projeto de Github da Dio
Repositório criado para o Desafio de Projeto.

[Sintaxe Básica Markdown](https://www.markdownguide.org/basic-syntax)

# Docker HTML_Apache_Container

This document contains notes on Docker, including instructions on running containers, creating images, and using Docker Compose.

## Running Containers

To run a Docker container, use the following command:

```
docker run [OPTIONS] IMAGE [COMMAND]

```

Some useful options include:

- `d` to run the container in the background
- `p` to map a port on the host to a port inside the container
- `-name` to give the container a name
- `-volume` to mount a directory from the host inside the container

## Creating Images

To create a Docker image, create a Dockerfile containing the instructions for building the image. Then, use the `docker build` command to build the image.

For example, to build an image for a PHP application with Apache, you could use the following Dockerfile:

```
FROM php:7.4-apache
COPY website/ /var/www/html/

```

## Using Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. To use Docker Compose, create a YAML file describing the services you want to run, and then use the `docker-compose` command to start the services.

For example, to run an Apache container serving an HTML website, you could use the following YAML file:

```
version: '3.9'
services:
  apache:
    image: httpd:latest
    container_name: my-apache-app
    ports:
    - '80:80'
    volumes:
    - ./website:/usr/local/apache2/htdocs

```

## Conclusion

Docker is a powerful tool for managing and deploying applications in containers. With Docker, you can easily package your applications and their dependencies, and run them anywhere. These notes provide a starting point for working with Docker, but there is much more to learn.
