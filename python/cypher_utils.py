from neo4j import GraphDatabase

driver = None

def open(host,user,passwd):
    global driver
    driver = GraphDatabase.driver(host, auth=(user, passwd))
    return

def close():
    driver.close()
    return

def cypher(cmd):
    def transaction(tx,cypher_cmd):
        result = tx.run(cypher_cmd)
        ret = result.single()
        if(ret is None):
            return None
        else:
            return ret[0]
    with driver.session() as session:
        result = session.write_transaction(transaction, cmd)
        if(result is not None):
            return result

def run(driver,cypher_cmd):
    def transaction(tx,cypher_cmd):
        result = tx.run(cypher_cmd)
        ret = result.single()
        if(ret is None):
            return None
        else:
            return ret[0]
    with driver.session() as session:
        result = session.write_transaction(transaction, cypher_cmd)
        if(result is not None):
            return result

def json_nodes_edges_to_cypher(json_graph):
    uid = json_graph["edges_nodes_id"]
    cmd = "CREATE "
    for n in json_graph["nodes"]:
        props = ""
        prop_count = 0
        for key,value in n.items():
            if(key == "_label"):
                continue
            if(prop_count > 0):
                props += ", "
            if(type(n[key]) == str):
                props += f"{key}:'{n[key]}'"
            else:
                props += f"{key}:{n[key]}"
            prop_count += 1
        cmd += f"\n ({n[uid]}:{n['_label']} {{{props}}}),"

    for e in json_graph["edges"]:
        props = ""
        prop_count = 0
        for key,value in e.items():
            if(key in ["_label","_in","_out"]):
                continue
            if(prop_count > 0):
                props += ", "
            if(type(e[key]) == str):
                props += f"{key}:'{e[key]}'"
            else:
                props += f"{key}:{e[key]}"
            prop_count += 1
        cmd += f"\n ({e['_out']})-[:{e['_label']} {{{props}}}]->({e['_in']}),"
        
    cmd = cmd[:-1]+";"
    return cmd

def stringify_props(name,node,packed_json):
    props = f"name:'{name}'"
    for key,prop_val in node.items():
        if(key in packed_json):#This is a relationship not a property, so skip in node creation
            continue
        if(type(node[key]) == str):
            props += f", {key}:'{node[key]}'"
        else:
            props += f", {key}:{node[key]}"
    return props

def stringify_relations(name,node,packed_json):
    relations = ""
    for key,prop_val in node.items():
        if(key in packed_json):
            assert(isinstance(prop_val,list))
            for target in prop_val:
                relations += f"\n (`{name}`)-[:relatesto]->(`{target}`),"
    return relations
    

def json_packed_to_cypher(packed_json):
    cmd = "CREATE "
    #Nodes
    for Label,Labels_map in packed_json.items():
        for name,node in Labels_map.items():
            props = stringify_props(name,node,packed_json)
            cmd += f"\n (`{name}`:{Label} {{{props}}}),"
    #Relationships
    for Label,Labels_map in packed_json.items():
        for name,node in Labels_map.items():
            cmd += stringify_relations(name,node,packed_json)
    cmd = cmd[:-1]+";"
    return cmd
