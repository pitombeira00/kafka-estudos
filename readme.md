# Estudo de Integração Kafka e ksqlDB com Banco de Dados

## Descrição

Este projeto demonstra como integrar um tópico Kafka com um banco de dados utilizando o ksqlDB. O objetivo é mostrar, na prática, como dados publicados em um tópico Kafka podem ser processados e persistidos em um banco de dados não relacional, utilizando o poder do ksqlDB para transformar e consultar streams em tempo real.

## Arquitetura

- **Kafka**: Sistema de mensageria distribuído, responsável por receber e distribuir eventos.
- **ksqlDB**: Plataforma de streaming SQL para Apache Kafka, permitindo consultas e transformações em tempo real.
- **Banco de Dados**: Armazena os dados processados (MongoDB).

O fluxo básico é:
1. Um produtor publica mensagens em um tópico Kafka.
2. O ksqlDB lê e processa essas mensagens.
3. O resultado pode ser consultado via ksqlDB ou enviado para um banco de dados usando conectores Kafka Connect.

