from yashoes.model.variant import Variant

CONST_VARIANT_LIST = [
    {
        "id": 1,
        "name": "3.0",
        "size": "40",
        "price": 400,
        "quantity": 10,
        "color": "red",
        "image_link": "https://kiza.vn/media/wysiwyg/products/adidas/KAD039/giay-adidas-namd-xr1-mau-den-2.jpg",
        "product_id": 1
    },
    {
        "id": 2,
        "name": "Black",
        "size": "40",
        "price": 300,
        "quantity": 10,
        "color": "black",
        "image_link": "http://anchuongshoes.com/image/cache/catalog/12-8/Giay%20Adidas%20Stanmith%20Den-800x800.jpg",
        "product_id": 2
    },
    {
        "id": 3,
        "name": "Black",
        "size": "40",
        "price": 500,
        "quantity": 10,
        "color": "black",
        "image_link": "https://vn-live-02.slatic.net/original/47f36d1004ad5a4fbad41345b7d2f87c.jpg",
        "product_id": 3
    },
    {
        "id": 4,
        "name": "Black",
        "size": "40",
        "price": 600,
        "quantity": 10,
        "color": "black",
        "image_link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLzo7GirVD6QZ-w2iJBF8Cs12Z_"
                      "TD4rClFxQPIs0K4VpgJ-g6n6g",
        "product_id": 4
    },
    {
        "id": 5,
        "name": "Racer +3",
        "size": "40",
        "price": 250,
        "quantity": 10,
        "color": "red",
        "image_link": "https://www.kingsport.vn/vnt_upload/product/giay_nike_nam/Untitled-1.jpg",
        "product_id": 5
    },
    {
        "id": 6,
        "name": "Jordan 1",
        "size": "40",
        "price": 480,
        "quantity": 10,
        "color": "white",
        "image_link": "https://kiza.vn/media/catalog/product/cache/1/image/650x/040ec09b1e35df139433887a97daa66f/g/i/"
                      "giay-nike-zoom-mau-den-005.jpg",
        "product_id": 6
    },
    {
        "id": 7,
        "name": "Run 3",
        "size": "40",
        "price": 150,
        "quantity": 10,
        "color": "blue",
        "image_link": "https://bizweb.dktcdn.net/100/266/606/files/giay-nike-air-zoom-pegasus-3411.jpg?v=1516242653597",
        "product_id": 7
    },
    {
        "id": 8,
        "name": "Black",
        "size": "40",
        "price": 230,
        "quantity": 10,
        "color": "red",
        "image_link": "https://www.kingsport.vn/vnt_upload/product/giay_nike_nu/0000199364273_nike-833662_010_"
                      "anp_05.jpg",
        "product_id": 8
    }
]


def create_variant():
    for variant in CONST_VARIANT_LIST:
        try:
            obj = Variant.objects.get(pk=variant.get('id'))
            obj.name = variant.get('name')
            obj.price = variant.get('price')
            obj.quantity = variant.get('quantity')
            obj.color = variant.get('color')
            obj.image_link = variant.get('image_link')
            obj.product_id = variant.get('product_id')
            obj.save()
        except Variant.DoesNotExist:
            Variant.objects.create(**variant)
