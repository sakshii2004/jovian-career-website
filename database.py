from sqlalchemy import create_engine, text
import os

connection_info = os.environ['connection_info']

engine = create_engine(connection_info, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"}
})

def jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._asdict()))
    return jobs

'''with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    row = result.all()[0]
    dict_ = dict(row._asdict())
    print(type(dict_))'''