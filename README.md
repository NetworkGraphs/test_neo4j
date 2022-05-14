# neo4j
* Cypher : Graph Query Language
* apoc : Awesome Procedures On Cypher
* gds : Graph Data Science
## note
Please refer to the official links for latest documentation, this repo is only a sort of cheat sheet and contains history of commands I tested
# install
```
./run.sh
```
then open in browser

http://localhost:7474/browser/

install VSCode plugin `Cypher Query Language`
# Links
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
manual
- https://neo4j.com/docs/cypher-manual/4.4/introduction/

Load Json
- https://neo4j.com/labs/apoc/4.4/overview/apoc.load/apoc.load.json/#usage-apoc.load.json

Match all nodes
- https://neo4j.com/docs/cypher-manual/4.4/clauses/match/#get-all-nodes
## Graph Data Science
https://neo4j.com/docs/graph-data-science/current/

project params
- https://neo4j.com/docs/graph-data-science/current/graph-project/

FastRP and kNN example
- https://neo4j.com/docs/graph-data-science/current/end-to-end-examples/fastrp-knn-example/

## Python
- limitations (No Numeric utility, no Cypher on GDS on Python) https://neo4j.com/docs/graph-data-science/current/python-client/known-limitations/
- mapping Cypher / Python : https://neo4j.com/docs/graph-data-science/current/python-client/getting-started/#python-client-getting-started-mapping

```shell
sudo apt install python3.8-venv
sudo apt install python3-pip
python3 -m venv venv
source venv/bin/activate
```
## Bloom
bloom on docker only for enterprise edition with license as docker param
- https://neo4j.com/docs/bloom-user-guide/current/bloom-installation/advanced-installation/#bloom-docker



