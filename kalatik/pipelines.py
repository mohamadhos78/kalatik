# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter
from . import settings

class KalatikPipeline:
    # def __init__(self):
    #     with sqlite3.connect(settings.SQLITE_DB_NAME) as db:
    #         db.execute("""
    #             CREATE TABLE IF NOT EXISTS mobiles(
    #             title varchar(255) ,
    #             descrption varchar(255),
    #             color  varchar(63),
    #             price varchar(63),
    #             brand varchar(31)
    #         );""")
        
    def process_item(self, item, spider):
        values = (
            item['title'] , 
            item['description'] , 
            item['colors'] , 
            item['price'] , 
            item['brand']
        )
        with sqlite3.connect(settings.SQLITE_DB_NAME) as db:
            db.execute("""
                    CREATE TABLE IF NOT EXISTS mobiles(
                    title varchar(255) ,
                    descrption varchar(255),
                    color  varchar(63),
                    price varchar(63),
                    brand varchar(31)
                );""")
            db.execute(f"INSERT INTO mobiles VALUES{values};")  
            print("\n\n\tdata added!")          
        return "\n\n\tdata added!"