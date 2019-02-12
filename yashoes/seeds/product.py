from yashoes.model.product import Product

CONST_PRODUCT_LIST = [
    {
        "id": 1,
        "name": "Neo",
        "description": "nice",
        "rate": 4,
        "brand_id": 2
    },
    {
        "id": 2,
        "name": "Ultra Boost",
        "description": "nice",
        "rate": 5,
        "brand_id": 2
    },
    {
        "id": 3,
        "name": "Supperstar",
        "description": "nice",
        "rate": 3,
        "brand_id": 2
    },
    {
        "id": 4,
        "name": "Stan Smith",
        "description": "nice",
        "rate": 5,
        "brand_id": 2
    },
    {
        "id": 5,
        "name": "Air Jordan 1",
        "description": "nice",
        "rate": 4,
        "brand_id": 1
    },
    {
        "id": 6,
        "name": "Dual Fusion Run 3",
        "description": "nice",
        "rate": 5,
        "brand_id": 1
    },
    {
        "id": 7,
        "name": "Pernix Mens Shoes Black",
        "description": "nice",
        "rate": 3,
        "brand_id": 1
    },
    {
        "id": 8,
        "name": "Air Zoom Pegasus",
        "description": "nice",
        "rate": 5,
        "brand_id": 1
    }
]


def create_product():
    for product in CONST_PRODUCT_LIST:
        try:
            obj = Product.objects.get(pk=product.get('id'))
            obj.name = product.get('name')
            obj.description = product.get('description')
            obj.rate = product.get('rate')
            obj.brand_id = product.get('brand_id')
            obj.save()
        except Product.DoesNotExist:
            Product.objects.create(**product)
