# extractor
**uma ferramenta para baixar os curriculos lattes em XML, a partir do webservice do CNPq**

## Requisitos

* [Docker](https://docs.docker.com/get-docker)
* [Docker-compose](https://docs.docker.com/compose/install/)
* Acesso institucional ao [Lattes Extractor](http://memoria.cnpq.br/web/portal-lattes/extracoes-de-dados) do CNPq

## Entrada

* Arquivo de configurações conforme modelo abaixo
* Arquivo texto (idlattes.txt) com os ids que serão baixados (cada id em uma linha separada)

```
[DEFAULT]
xml_dir = xml/
idlattes_file = idlattes.txt
```

## Saída

* Arquivos XML relativos aos ids informados no arquivo de entrada

## Como executar

```
docker-compose run --rm extractor
```

## TODO
* Baixar as informações dos grupos de pesquisa

## Autor

* Prof. Rafael Perazzo Barbosa Mota ( rafael.mota (at) ufca.edu.br )
