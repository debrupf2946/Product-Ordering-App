from fastapi import FastAPI
from redis_om import get_redis_connection,HashModel
from fastapi.middleware.cors import CORSMiddleware





redis= get_redis_connection(
    host='redis-10368.c212.ap-south-1-1.ec2.redns.redis-cloud.com',
    port=10368,
    password="YO3uvaQQzwtIGsB0KnPDxWow0ptm3PX9",
    decode_responses=True,
)

class Product(HashModel):
    name: str
    price: float
    quantity: int
    
    class  Meta:
        database=redis
    

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['https://127.0.0.1:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/products")
def all():
    return Product.all_pks()

@app.post("/products")
def create(product: Product):
    return product.save()
    
    


