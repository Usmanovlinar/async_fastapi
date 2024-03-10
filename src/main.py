from fastapi import FastAPI


redis = aioredis.from_url("redis://localhost")

app = FastAPI()
app.debug = True

import children.router as children_rout
import parents.router as parents_rout

app.include_router(children_rout.router)
app.include_router(parents_rout.router)










