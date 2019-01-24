from django.db import models
from yashoes.model.brand import Brand


class HomePageResponse(object):

    def __init__(self, id, brand_name, products):
        self.id = id
        self.brand_name = brand_name
        self.products = products
