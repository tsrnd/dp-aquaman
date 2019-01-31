from yashoes.model.brand import Brand

CONST_BRAND_LIST = [
    {
        "id": 1,
        "brand_name": "Nike"
    },
    {
        "id": 2,
        "brand_name": "Adidas"
    },
    {
        "id": 3,
        "brand_name": "Bitis"
    },
    {
        "id": 4,
        "brand_name": "Converse"
    }
]


def create_brand():
    for brand in CONST_BRAND_LIST:
        try:
            Brand.objects.get(pk=brand.get('id'))
        except Brand.DoesNotExist:
            Brand.objects.create(**brand)
