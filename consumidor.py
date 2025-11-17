from kafka import KafkaConsumer

# Configurações do Kafka
BROKER = 'localhost:9092'       # Altere para o endereço do seu broker Kafka
TOPICO = 'topico-estudo'       # Altere para o nome do seu tópico

def main():
    # Cria o consumidor
    consumer = KafkaConsumer(
        TOPICO,
        bootstrap_servers=[BROKER],
        auto_offset_reset='earliest',  # ou 'latest' para pegar apenas as novas mensagens
        enable_auto_commit=True,
        group_id='meu-grupo-consumidor',  # Nome do grupo de consumidores
        value_deserializer=lambda x: x.decode('utf-8')
    )

    print(f"Consumindo mensagens do tópico: {TOPICO}")
    for mensagem in consumer:
        print(f"Recebido: {mensagem.value}")

if __name__ == '__main__':
    main()