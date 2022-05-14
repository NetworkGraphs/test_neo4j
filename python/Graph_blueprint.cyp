CREATE 
 (lop:Program {name:'lop', lang:'java'}),
 (vadas:Person {name:'vadas', age:27}),
 (marko:Person {name:'marko', age:29}),
 (peter:Person {name:'peter', age:35}),
 (ripple:Program {name:'ripple', lang:'java'}),
 (josh:Person {name:'josh', age:32}),
 (josh)-[:created {weight:1}]->(ripple),
 (marko)-[:knows {weight:0.5}]->(vadas),
 (marko)-[:created {weight:0.4}]->(lop),
 (marko)-[:knows {weight:1}]->(josh),
 (josh)-[:created {weight:0.4}]->(lop),
 (peter)-[:created {weight:0.2}]->(lop);