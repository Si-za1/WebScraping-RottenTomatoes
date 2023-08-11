def execute_query_from_file(conn, cur, query, data=None):
    if data:
        breakpoint()
        cur.execute(query, data)
    else:
        cur.execute(query)
  
    conn.commit()