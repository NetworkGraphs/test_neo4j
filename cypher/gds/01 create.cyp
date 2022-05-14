CREATE
 (dan:Person {name: 'Dan'}),
 (annie:Person {name: 'Annie'}),
 (matt:Person {name: 'Matt'}),
 (jeff:Person {name: 'Jeff'}),
 (brie:Person {name: 'Brie'}),
 (elsa:Person {name: 'Elsa'}),

 (cookies:Product {name: 'Cookies'}),
 (tomatoes:Product {name: 'Tomatoes'}),
 (cucumber:Product {name: 'Cucumber'}),
 (celery:Product {name: 'Celery'}),
 (kale:Product {name: 'Kale'}),
 (milk:Product {name: 'Milk'}),
 (chocolate:Product {name: 'Chocolate'}),

 (dan)-[:BUYS {amount: 1.2}]->(cookies),
 (dan)-[:BUYS {amount: 3.2}]->(milk),
 (dan)-[:BUYS {amount: 2.2}]->(chocolate),

 (annie)-[:BUYS {amount: 1.2}]->(cucumber),
 (annie)-[:BUYS {amount: 3.2}]->(milk),
 (annie)-[:BUYS {amount: 3.2}]->(tomatoes),

 (matt)-[:BUYS {amount: 3}]->(tomatoes),
 (matt)-[:BUYS {amount: 2}]->(kale),
 (matt)-[:BUYS {amount: 1}]->(cucumber),

 (jeff)-[:BUYS {amount: 3}]->(cookies),
 (jeff)-[:BUYS {amount: 2}]->(milk),

 (brie)-[:BUYS {amount: 1}]->(tomatoes),
 (brie)-[:BUYS {amount: 2}]->(milk),
 (brie)-[:BUYS {amount: 2}]->(kale),
 (brie)-[:BUYS {amount: 3}]->(cucumber),
 (brie)-[:BUYS {amount: 0.3}]->(celery),

 (elsa)-[:BUYS {amount: 3}]->(chocolate),
 (elsa)-[:BUYS {amount: 3}]->(milk);
 