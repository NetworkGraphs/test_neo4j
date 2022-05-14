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

def json_to_cypher(json_graph):
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
