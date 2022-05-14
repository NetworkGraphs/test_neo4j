from graphdatascience import GraphDataScience

gds = GraphDataScience("bolt://localhost:7687", auth=("neo4j", "test"))

G, res = gds.graph.project(
    "purchase-proj",
    ["Person", "Product"],
    ["BUYS","CHILD_OF"]
)

G = gds.graph.get("purchase-proj")

n = G.node_count()
props = G.node_properties("Person")

