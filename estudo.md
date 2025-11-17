# Entrevista Técnica - Apache Kafka: Perguntas e Respostas Otimizadas

---

## 1. Administração e configuração de clusters Kafka

**Pontos positivos da resposta:**
- Brokers em número ímpar para garantir resiliência.
- Preocupação com consumidores, CPU e memória.
- Foco em alta disponibilidade.

**Resposta otimizada:**
> Diante de um cenário de alta demanda, como Black Friday, minha estratégia seria aumentar o número de brokers do cluster Kafka para um valor ímpar (5 ou 7), fortalecendo a tolerância a falhas. Revisaria o fator de replicação dos tópicos, faria o rebalanceamento das partições para otimizar o uso dos brokers e monitoraria métricas como lag dos consumidores, Under Replicated Partitions, CPU, memória e taxas de throughput. Testaria cenários de failover e revisaria configurações como min.insync.replicas, reforçando controles de acesso e auditoria para proteger os dados em períodos críticos.

---

## 2. Pipelines de alto throughput

**Pontos positivos da resposta:**
- Particionamento balanceado com brokers.
- Uso de "at least once" para entrega confiável.
- Estrutura distribuída por zonas para disponibilidade.

**Resposta otimizada:**
> Para garantir alto throughput em pipelines Kafka, defino o número de partições baseado no volume de eventos e paralelismo, podendo ultrapassar o número de brokers. Configuro produtores com batch.size, linger.ms e compression.type, adotando “at least once” para segurança. Mantenho brokers em zonas distintas, monitoro o lag dos consumidores e as taxas de eventos com Prometheus/Grafana. Realizo testes de stress, ajusto balanceamento e configuro parâmetros para garantir o throughput desejado.

---

## 3. Soluções de stream processing

**Pontos positivos da resposta:**
- Uso de chave de negócios para ordenação.
- Mecanismos de deduplicação.
- Windowing para métricas agregadas.
- Monitoramento por Prometheus/Grafana.

**Resposta otimizada:**
> Utilizo Kafka Streams para calcular métricas de engajamento em tempo real, aplicando chaves por campanha, windowing de 5 minutos, e deduplicação por UUID. Monitoro lag dos consumidores e a latência das janelas com Prometheus/Grafana, garantindo ordenação, integridade e alta disponibilidade dos dados processados.

---

## 4. Estratégias de resiliência, particionamento e replicação

**Pontos positivos da resposta:**
- Brokers distribuídos entre data centers.
- Uso de Zookeeper/KRaft para eleição de líder.
- Configuração inicial de tópicos alinhada.

**Resposta otimizada:**
> Distribuo brokers entre data centers distintos e utilizo Zookeeper ou KRaft para eleição automática de líder em caso de falhas. Crio tópicos com número de partições conforme a demanda, replication.factor igual ao número de brokers ou três para tolerância a falhas, e ajusto min.insync.replicas para garantir entrega consistente. Valido a resiliência com testes de failover, mantendo produção e consumo operacionais em caso de falhas.

---

## 5. Apoio aos squads de backend

**Pontos positivos da resposta:**
- Particionamento ajustado por contexto.
- Grupos consumidores bem definidos para isolamento.
- Segurança via SSL/ACL.

**Resposta otimizada:**
> Em ambientes com múltiplos squads, configuro particionamento conforme demanda e grupos consumidores por equipe para isolamento. Implemento SSL/TLS e ACLs por serviço/tópico, uso Schema Registry para governança dos contratos de dados, e monitoro produção/consumo por squad, garantindo rastreabilidade e compliance.

---

## 6. Monitoramento, observabilidade e segurança

**Pontos positivos da resposta:**
- SSL/TLS na comunicação.
- ACL por serviço/tópico.
- Prometheus/Grafana para rastreabilidade.

**Resposta otimizada:**
> Implemento SSL/TLS para criptografia, ACLs rígidas para acesso controlado, e logs de auditoria para rastrear operações sensíveis. Usando Prometheus/Grafana, monitoro latência, throughput e alertas automáticos, integrando com SIEM se necessário, para garantir compliance e segurança dos dados.

---

## 7. Evolução da arquitetura distribuída

**Pontos positivos da resposta:**
- Clusters segmentados por contexto/artefato.
- Kafka em padrão saga ou async.
- Redução de latência com zona única.

**Resposta otimizada:**
> Crio clusters Kafka segmentados por contexto, utilizo Kafka como orquestrador de sagas e comunicação assíncrona entre microsserviços, mantenho infraestrutura na mesma região e distribuo brokers por zonas para baixa latência. Uso API Gateway e Load Balancer na borda, complementando com Schema Registry, tracing distribuído e automação CI/CD.

---

## 8. Integração: Kafka Connect, Schema Registry e Avro/Protobuf

**Pontos positivos da resposta:**
- Integração de APIs, bancos e logs via connectors.
- Governança de contratos de dados.
- Compactação e padronização com Avro/Protobuf.

**Resposta otimizada:**
> Utilizo Kafka Connect para integrar sistemas diversos, Schema Registry para padronizar e versionar os dados, e Avro/Protobuf para compactar, validar e otimizar o tráfego. Monitoro connectors via Confluent Control Center para garantir integridade e performance.

---

## 9. Desafio de alto volume e baixa latência

**Pontos positivos da resposta:**
- Monitoramento e alerta de lag.
- Diagnóstico pontual do broker.
- Rebalanceamento e escalabilidade de infraestrutura.

**Resposta otimizada:**
> Monitoro continuamente o lag dos consumidores com Prometheus/Alertmanager. Ao detectar lag elevado, analiso se é pontual ou sistêmico, rebalanceio partições e escalo brokers ou consumidores conforme necessário, utilizando automação via KEDA (Kubernetes) ou scripts, garantindo performance e disponibilidade nos picos.

---

## 10. Escolha de solução para analytics em tempo real com restrição de orçamento

**Pontos positivos da resposta:**
- Decisão orientada por volume, integração, custo e facilidade.
- Comparação entre Kafka Streams e ksqlDB.

**Resposta otimizada:**
> Com restrições orçamentárias, avalio o volume e complexidade: para processamento moderado, escolho Kafka Streams ou ksqlDB, que rodam embarcados nas aplicações e demandam pouca infraestrutura. Kafka Streams é ideal para lógica customizada, ksqlDB para operações em SQL. Escalo aplicações conforme a demanda e monitoro métricas críticas, priorizando estas soluções pela facilidade de operação, baixo custo e integração nativa ao Kafka.

---

## 11. Integração e enriquecimento de dados com Oracle

**Pontos positivos da resposta:**
- Uso de Kafka Connector para Oracle.
- Particionamento inicial cuidadoso.
- Monitoramento via Prometheus.

**Resposta otimizada:**
> Integro Oracle ao Kafka com Connector configurado para CDC, criando tópicos com 3 partições, 1 réplica e 3 brokers. Uso Schema Registry para governança dos dados, monitoro throughput e lag via Prometheus/Grafana e ajusto escala conforme demanda. Realizo testes de carga e automação para evitar gargalos e garantir alta performance na integração e enriquecimento dos dados.

---

## 12. Infraestrutura distribuída: Docker, Kubernetes, CI/CD

**Pontos positivos da resposta:**
- Containerização dos serviços.
- Migração para Kubernetes.
- Práticas CI/CD, automação e escalabilidade.

**Resposta otimizada:**
> Em ambientes Kubernetes, implanto brokers Kafka usando Helm Charts, configuro volumes persistentes para dados e uso StatefulSets para gerenciamento dos pods. Automatizo deploys com pipelines CI/CD, garantindo atualizações sem downtime. Implemento monitoramento, autoscaling e rollback seguro, promovendo escalabilidade e evolução da arquitetura distribuída.

---

_Fim do documento_