<h1 align="center">
  <br>
  <br>
  Bull-Alert
  <br>
</h1>

<h4 align="center">FastAPI meets blockchain sandbox project</h4>

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is a sandbox for me to experience FastAPI framework while also 
interacting with blockchain data from different entry points such as Etherscan API.

While implementing some features I might come up with I'll try to utilize best 
practices that I've learned from working on different Django Rest Framework projects.

## API URLs
* [/api/v1/openapi docs](http://0.0.0.0:8000/docs#/)
	
## Technologies
#### Project environment:
* Docker: 20.10.7
* docker-compose: 1.29.2
* Poetry: 1.0.5
* make

#### Project backend service:
* Python: 3.9.2
* FastAPI: 0.70.0

## Requirements:
* Docker: ^20.10.7
* docker-compose: ^1.29.2
* [optional] make
	
## Setup
To run this project locally cd into the project and:

```
$ make dev
# Builds and starts docker containers
$ make exec-backend
# enters backend container shell via bash
```
