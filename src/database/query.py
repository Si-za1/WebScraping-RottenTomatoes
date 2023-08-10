def execute_query_from_file(conn, cur, query, data=None):
    if data:
        cur.execute(query, data)
    else:
        cur.execute(query)
  
    conn.commit()