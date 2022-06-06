* Cypher : Graph Query Language
* apoc : Awesome Procedures On Cypher
* gds : Graph Data Science

# jupyter lab
should be run from the `python` folder as it is referencing file paths
```shell
$ cd python
$ source venv/bin/activate
python$ jupyter lab
```
then open the provided url with the tocken in the browser
http://localhost:8888/lab?token=9a94cxxxxxxxxxxxd85b002fxxxxxxxxxxxx


# install
- install VSCode plugin `Cypher Query Language`
- install VSCode plugin `JSON Lines`
- install python venv and dependencies

# issues
running jupyter lab on wsl result in following error which did not prevent further normal usage
`Start : This command cannot be run due to the error: The system cannot find the file specified.`
Fixing this error properly require a complex configuration

## Cypher
refcard
- https://neo4j.com/docs/cypher-refcard/current/

manual
- https://neo4j.com/docs/cypher-manual/4.4/introduction/

apoc
- https://neo4j.com/labs/apoc/4.4/
