//get version
call dbms.components() yield name, versions, edition
unwind versions as version
return name, version, edition;

// list databases
show databases

//match all
MATCH (n)
RETURN n

//or simply
match(n) return n

