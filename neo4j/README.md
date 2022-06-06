# neo4j
* Cypher : Graph Query Language
* apoc : Awesome Procedures On Cypher
* gds : Graph Data Science

## run
- docker: simply run `./run.sh` which content is

then open in browser
http://localhost:7474/browser/
- note that as this repo is for test only, it is using a default user and password.

# references
install
- https://neo4j.com/developer/docker-run-neo4j/
- https://neo4j.com/labs/apoc/4.1/installation/#docker

list of plugins
- https://neo4j.com/docs/operations-manual/current/docker/operations/#docker-neo4jlabs-plugins

Browser Styling
- https://neo4j.com/docs/browser-manual/current/operations/browser-styling/
```cmd
:style
:style 'file:///style.grass'
```
## Cypher
refcard
- https://neo4j.com/docs/cypher-refcard/current/

manual
- https://neo4j.com/docs/cypher-manual/4.4/introduction/

apoc
- https://neo4j.com/labs/apoc/4.4/

## Graph Data Science
https://neo4j.com/docs/graph-data-science/current/

project params
- https://neo4j.com/docs/graph-data-science/current/graph-project/

FastRP and kNN example
- https://neo4j.com/docs/graph-data-science/current/end-to-end-examples/fastrp-knn-example/

## Python
- limitations (No Numeric utility, no Cypher on GDS on Python) https://neo4j.com/docs/graph-data-science/current/python-client/known-limitations/
- mapping Cypher / Python : https://neo4j.com/docs/graph-data-science/current/python-client/getting-started/#python-client-getting-started-mapping


## Bloom
- bloom on docker only for enterprise edition with license as docker param
- note that bloom does not connect to default (non-enterprise) neo4j docker
- https://neo4j.com/docs/bloom-user-guide/current/bloom-installation/advanced-installation/#bloom-docker
