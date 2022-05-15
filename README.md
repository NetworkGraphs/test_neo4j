# neo4j
* Cypher : Graph Query Language
* apoc : Awesome Procedures On Cypher
* gds : Graph Data Science
## note
Please refer to the official links for latest documentation, this repo is only a sort of cheat sheet and contains history of commands I tested
# run
- docker: simply run `./run.sh` which content is
```shell
docker run \
    --name neo_explore \
    -p7474:7474 -p7687:7687 \
    -d \
    -v ${PWD}/neo4j/data:/data \
    -v ${PWD}/neo4j/logs:/logs \
    -v ${PWD}/neo4j/import:/var/lib/neo4j/import \
    -v ${PWD}/neo4j/plugins:/plugins \
    -e NEO4J_AUTH=neo4j/test \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4JLABS_PLUGINS=\[\"apoc\",\"graph-data-science\"\] \
    neo4j:latest
```
then open in browser
http://localhost:7474/browser/
- note that as this repo is for test only, it is using a default user and password.

- jupyter lab : should be run from the `python` folder as it is referencing file paths
```shell
$ source venv/bin/activate
$ cd python
python$ jupyter lab
```
then open the provided url with the tocken in the browser
http://localhost:8888/lab?token=9a94cxxxxxxxxxxxd85b002fxxxxxxxxxxxx


# install
- install VSCode plugin `Cypher Query Language`
- install VSCode plugin `JSON Lines`
- install python environment
```shell
sudo apt install python3.8-venv
sudo apt install python3-pip
python3 -m venv venv
source venv/bin/activate
pip install jupyterlab
```

# issues
running jupyter lab on wsl result in following error which did not prevent further normal usage
`Start : This command cannot be run due to the error: The system cannot find the file specified.`
Fixing this error properly require a complex configuration
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
bloom on docker only for enterprise edition with license as docker param
- https://neo4j.com/docs/bloom-user-guide/current/bloom-installation/advanced-installation/#bloom-docker

