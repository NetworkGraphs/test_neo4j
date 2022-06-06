docker run \
    --name neo_explore \
    -p7474:7474 -p7687:7687 \
    -d \
    -v ${PWD}/docker/data:/data \
    -v ${PWD}/docker/logs:/logs \
    -v ${PWD}/docker/import:/var/lib/neo4j/import \
    -v ${PWD}/docker/plugins:/plugins \
    -e NEO4J_AUTH=neo4j/test \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4JLABS_PLUGINS=\[\"apoc\",\"graph-data-science\"\] \
    neo4j:latest
