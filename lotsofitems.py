from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///categoryitems.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
user1 = User(name="Sun Flower", email="sun_flower@itemcatalog.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Items for Annuals
category1 = Category(name="Annual", description="An annual plant is a plant that completes its life cycle, from germination to the production of seeds, within one year, and then dies.")

session.add(category1)
session.commit()

categoryItem1 = CategoryItem(name="Begonia", description="The genus Begonia offers a wide selection of outstanding foliage as well as flowers.",
                     price="6.99", category=category1, user=user1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Cleome", description="An heirloom often seen in cottage gardens, Spider Flowers deserve a place in well-bred borders, too.",
                     price="5.50", category=category1, user=user1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Coleus", description="The endlessly colorful foliage of the genus Coleus is making a comeback as gardeners rediscover old varieties and breeders introduce new ones.",
                     price="7.99", category=category1, user=user1)

session.add(categoryItem3)
session.commit()


# Items for Perennials
category2 = Category(name="Perennial", description="A perennial plant or simply perennial is a plant that lives more than two years.")

session.add(category2)
session.commit()

categoryItem1 = CategoryItem(name="Cone Flower", description="Echinacea, a North American genus in the Daisy family, has big, bright flowers that appear from late June until frost.",
                     price="6.99", category=category2, user=user1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Black-Eyed Susan", description="Rudbeckia is a genus of highly decorative native American perennials that bloom from late summer until frost.",
                     price="5.50", category=category2, user=user1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Hosta", description="Hostas have many handsome leaf colorations and lavender or white Lily-like flowers on graceful stalks.",
                     price="3.99", category=category2, user=user1)

session.add(categoryItem3)
session.commit()


# Items for Shrubs
category3 = Category(name="Shrub", description="A shrub or bush is a small to medium-sized woody plant.")

session.add(category3)
session.commit()

categoryItem1 = CategoryItem(name="Rose", description="Roses offer colors, perfumes, forms, and habits to suit every garden situation.",
                     price="12.99", category=category3, user=user1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="Hygrangea", description="Hydrangea is a valuable genus of some 100 species of shrubs and vines grown for their large and very showy flower heads.",
                     price="25.50", category=category3, user=user1)

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(name="Azalea", description="Rhododendron is a genus of evergreen and deciduous shrubs, which includes Azaleas.",
                     price="13.99", category=category3, user=user1)

session.add(categoryItem3)
session.commit()


print "added category items!"