from graphdatascience import GraphDataScience

# We follow the convention to name our `GraphDataScience` object `gds`
gds = GraphDataScience("bolt://localhost:7687", auth=("neo4j", "test"))

# Create a minimal example graph
gds.run_cypher(
  """
  CREATE
  (m: City {name: "Malmö"}),
  (l: City {name: "London"}),
  (s: City {name: "San Mateo"}),
  (m)-[:FLY_TO]->(l),
  (l)-[:FLY_TO]->(m),
  (l)-[:FLY_TO]->(s),
  (s)-[:FLY_TO]->(l)
  """
)

# Project the graph into the GDS Graph Catalog
# We call the object representing the projected graph `G_office`
G_office, _ = gds.graph.project("neo4j-offices", "City", "FLY_TO")

# Run the mutate mode of the PageRank algorithm
_ = gds.pageRank.mutate(G_office, tolerance=0.5, mutateProperty="rank")

# We can inspect the node properties of our projected graph directly
# via the graph object and see that indeed the new property exists
print(G_office.node_properties("City"))
