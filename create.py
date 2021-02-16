from main.models import * 
import pandas as pd
import unidecode
import math

path = 'goods/final.csv'

def create_all():
    i = 0
    d = pd.read_csv(path)
    for index, item in d.iterrows():
        cat_name = item['category']
        sub_name = item['sub_name']
        sub_img = item['sub_img']
        name = item['p_name']
        price = item['p_price']
        imgsrc = item['p_image']
        desc = item['p_desc']
        code = item['p_code']
        features = item['p_features']
        sale_price = item['p_sale_price']
        sale_price = "{:.2f}".format(sale_price)
        print('sale price is: ', sale_price)
        if (sale_price == 'nan'):
            sale_price = None
        price = unidecode.unidecode(price)
        price = price.split(' ')[0].strip(',').replace(',', '.')
        price = float(price)
        price = "{:.2f}".format(price)


        if (Category.objects.filter(
            name = cat_name
        ).exists()):
            category = Category.objects.get(
                name = cat_name
            )
        else:
            category = Category.objects.get_or_create(
                name = cat_name,
                imgsrc = imgsrc
            )[0]

        if (Subcategory.objects.filter(
            category = category,
            name = sub_name
        ).exists()):
            subcategory = Subcategory.objects.get(
            category = category,
            name = sub_name
            )
        else:
            subcategory = Subcategory.objects.get_or_create(
            category = category,
            name = sub_name,
            imgsrc = imgsrc,
            )[0]

        print('try to assign product')
        product = Product(
            category = category,
            subcategory = subcategory,
            name = name,
            price = price,
            sale_price = sale_price,
            imgsrc = imgsrc,
            description = desc,
            code = code,
        )
        print('try to save product')
        product.save()

        features = eval(features)
        for key in features:
            attribute_name = key.strip()
            attributeitem_name = features[key].strip()
            attribute = Attribute.objects.get_or_create(
                name = attribute_name
            )[0]
            attributeitem = Attributeitem.objects.get_or_create(
                attribute = attribute,
                name = attributeitem_name
            )[0]
            product.attributeitem.add(attributeitem)
        i += 1
        print('created', i, 'products')


if __name__ == '__main__':
    delall()
    create_all()
