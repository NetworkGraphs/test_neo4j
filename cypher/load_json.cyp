CALL apoc.load.json("file:///person.json")
YIELD value
MERGE (p:Person {name: value.name})
SET p.age = value.age
WITH p, value
UNWIND value.children AS child
MERGE (c:Person {name: child})
MERGE (c)-[:CHILD_OF]->(p);
