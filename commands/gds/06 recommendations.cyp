MATCH (:Person {name: "Annie"})-->(p1:Product)
WITH collect(p1) as products
MATCH (:Person {name: "Matt"})-->(p2:Product)
WHERE not p2 in products
RETURN p2.name as recommendation