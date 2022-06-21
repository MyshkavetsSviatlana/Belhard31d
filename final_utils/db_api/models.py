from sqlalchemy import Column, SmallInteger, VARCHAR, ForeignKey, INTEGER
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'
    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    parent_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'))


class Product(Base):
    __tablename__: str = "products"
    id = Column(INTEGER, primary_key=True)
    category_id = Column(SmallInteger, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    name = Column(VARCHAR(50), nullable=False)
    page = Column(SmallInteger, nullable=False)
    position = Column(SmallInteger, nullable=False)
    descr = Column(VARCHAR(50), nullable=False)
#
# 'products': [{"id":2725118,
#  "key":"mbpro16sg",
#  "name":"Macbook Pro 16\" M1 Pro 2021 MK183",
#  "full_name":"Apple Macbook Pro 16\" M1 Pro 2021 MK183",
#  "name_prefix":"Ноутбук",
#  "extended_name":"Ноутбук Apple Macbook Pro 16\" M1 Pro 2021 MK183",
#  "status":"active",
#  "images":
#      {"header":"\/\/content2.onliner.by\/catalog\/device\/header\/625fa73d5895f8e29a2048b4006eeffc.jpeg",
#       "icon":null},
# "image_size":[],
# "description":"16.2&quot; 3456 x 2234 IPS, 120 Гц, несенсорный, Apple M1 Pro (10 ядер), 16 ГБ, SSD 512 ГБ,
# видеокарта встроенная, Mac OS, цвет крышки серый",
# "micro_description":"3456 x 2234 IPS, несенсорный, Apple M1 Pro (10 ядер), 16 ГБ, SSD 512 ГБ, встроенная,
# Mac OS, цвет крышки серый",
# "html_url":"https:\/\/catalog.onliner.by\/notebook\/apple\/mbpro16sg",
# "reviews":
#         {"rating":50,
#         "count":2,
#         "html_url":"https:\/\/catalog.onliner.by\/notebook\/apple\/mbpro16sg\/reviews",
#         "url":"https:\/\/catalog.api.onliner.by\/products\/mbpro16sg\/reviews"},
#         "review_url":null,
# "color_code":"808080",
# "prices":
#         {"min":null,
#          "price_min":
#              {"amount":"7560.00",
#               "currency":"BYN",
#               "converted":{"BYN":{"amount":"7560.00","currency":"BYN"},"BYR":{"amount":"","currency":"BYR"}}},
#          "max":null,
#          "price_max":{"amount":"25360.80","currency":"BYN","converted":{"BYN":{"amount":"25360.80","currency":"BYN"},"BYR":{"amount":"","currency":"BYR"}}},
#          "currency_sign":null,
#          "offers":{"count":22},
#          "html_url":"https:\/\/catalog.onliner.by\/notebook\/apple\/mbpro16sg\/prices",
#          "url":"https:\/\/shop.api.onliner.by\/products\/mbpro16sg\/positions"},
# "max_installment_terms":{"all":{"term":4,"label":"Рассрочка до 4 месяцев"}},
# "max_cobrand_cashback":{"percentage":5,"label":"5% на «Клевер»"},
# "sale":{"is_on_sale":false,"discount":0,"min_prices_median":{"amount":"7900.00","currency":"BYN"}},
# "second":{"offers_count":1,"min_price":{"amount":"6850.00","currency":"BYN"}},
# "forum":{"topic_id":24957611,
#          "topic_url":"https:\/\/forum.onliner.by\/viewtopic.php?t=24957611",
#          "post_url":"https:\/\/forum.onliner.by\/posting.php?mode=newtopic&f=65&device=mbpro16sg",
#          "replies_count":89},
# "url":"https:\/\/catalog.api.onliner.by\/products\/mbpro16sg",
# "advertise":null,
# "stickers":[{"type":"recommended","label":"Onlíner рекомендует","text":"","color":"0b6fd3","bg_color":"dfebff",
# "html_url":null}],
# "prime_info":{"available":false}}]
