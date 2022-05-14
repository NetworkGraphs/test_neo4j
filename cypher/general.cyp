//get version
call dbms.components() yield name, versions, edition
unwind versions as version
return name, version, edition;

// list databases
show databases

//match all
MATCH (n)
RETURN n

//delete all
MATCH (n)
DETACH DELETE n

//or simply
match(n) return n

//meta gaph
call apoc.meta.graph

//gds
RETURN gds.version()

CALL gds.list()
CALL gds.graph.list()
