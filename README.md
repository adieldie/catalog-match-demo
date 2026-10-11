# Correspondência de catálogo — demonstração offline

**Estágio: experimental / em teste. Demonstração parcial sanitizada, não pronta para produção.**

## Objetivo
Um recorte de correspondência de produtos por nome, preço e categoria.

## Recursos
Mapeamento por nome e preço, aliases específicos, aproximação textual e desempate por categoria.

## Instalação
Python 3.10+; sem dependências externas. Baixe somente os arquivos desta demonstração para uma pasta local.

## Uso e testes
```sh
python demo.py
python -m unittest -v
```

## Estágio e limites
Demonstração parcial de lógica extraída e adaptada, não uma cópia integral do sistema original. Fixtures e entradas são inteiramente fictícias.

Não é um sincronizador completo. A busca aproximada e o desempate pelo primeiro candidato podem sugerir correspondências incorretas. Preços usam float e tolerância de 0,05 herdada do recorte; isso não é uma regra universal. Todo resultado precisa de revisão humana; a demo não grava em catálogo nem acessa rede.

## Dados e segurança
Não inclui configurações operacionais, contas, histórico de conversas, bancos de dados, capturas de rede, segredos ou endpoints de produção. Nenhum envio externo ocorre.

## Licença
Nenhuma licença de redistribuição é atribuída automaticamente. A definição de licença depende de revisão dos direitos aplicáveis antes da publicação.
