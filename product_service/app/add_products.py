from models import db, Product
import setup

app = setup.create_app()

items = [
    {
        'name': 'Product 1',
        'slug': 'product-1',
        'image': 'ps5.png',
        'price': 1
    },
    {
        'name': 'Product 2',
        'slug': 'product-2',
        'image': 'joy.png',
        'price': 2
    },
    {
        'name': 'Product 3',
        'slug': 'product-3',
        'image': 'xbox.png',
        'price': 3
    },
    {
        'name': 'Product 4',
        'slug': 'product-4',
        'image': 'drones.png',
        'price': 4
    },
    {
        'name': 'Product 5',
        'slug': 'product-5',
        'image': 'vector.png',
        'price': 1
    },
    {
        'name': 'Product 6',
        'slug': 'product-6',
        'image': '3D.png',
        'price': 3
    },
]



# def add_products_to_db():
#     for item in items:
    
#         record = Product.query.filter_by(slug=item['slug']).first()

#         if record is None:

#             print("Adding product " + item['slug'] + "\n")

#             record = Product()
#             record.name = item['name']
#             record.slug = item['slug']
#             record.image = item['image']
#             record.price = item['price']

#             db.session.add(record)
#             db.session.commit()
#         else:
#             print("product " + item['slug'] + " has already been added ...... Skipping \n")
for item in items:
    
    record = Product.query.filter_by(slug=item['slug']).first()

    if record is None:

        print("Adding product " + item['slug'] + "\n")

        record = Product()
        record.name = item['name']
        record.slug = item['slug']
        record.image = item['image']
        record.price = item['price']

        db.session.add(record)
        db.session.commit()
    else:
        print("product " + item['slug'] + " has already been added ...... Skipping \n")