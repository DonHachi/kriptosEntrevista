from pymongo import MongoClient
from random import randint
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://hachi:1234abcd@cluster0-yh2mp.mongodb.net/test?retryWrites=true&w=majority")
#db=client.admin
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)
db=client.business
def test():
    fivestar = db.reviews.find_one({'rating': 5})
    print(fivestar)
test()
# #Step 2: Create sample data
# names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
# company_type = ['LLC','Inc','Company','Corporation']
# company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
# for x in range(1, 501):
#     business = {
#         'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
#         'rating' : randint(1, 5),
#         'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
#     }
#     #Step 3: Insert business object directly into MongoDB via isnert_one
#     result=db.reviews.insert_one(business)
#     #Step 4: Print to the console the ObjectID of the new document
#     print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
# #Step 5: Tell us that you are done
# print('finished creating 500 business reviews')

##find one
# fivestar = db.reviews.find_one({'rating': 5})
# print(fivestar)
#count all
# fivestarcount = db.reviews.find({'rating': 5}).count()
# print(fivestarcount)

#aggregation
# print('\nThe sum of each rating occurance across all data grouped by rating ')
# stargroup=db.reviews.aggregate(
# # The Aggregation Pipeline is defined as an array of different operations
# [
# # The first stage in this pipe is to group data
# { '$group':
#     { '_id': "$rating",
#      "count" : 
#                  { '$sum' :1 }
#     }
# },
# # The second stage in this pipe is to sort the data
# {"$sort":  { "_id":1}
# }
# # Close the array with the ] tag             
# ] )
# # Print the result
# for group in stargroup:
#     print(group)

#updating
# ASingleReview = db.reviews.find_one({})
# print('A sample document:')
# pprint(ASingleReview)
# result = db.reviews.update_one({'_id' : ASingleReview.get('_id') }, {'$inc': {'likes': 1}})
# print('Number of documents modified : ' + str(result.modified_count))
# UpdatedDocument = db.reviews.find_one({'_id':ASingleReview.get('_id')})
# print('The updated document:')
# pprint(UpdatedDocument)

#deleting
#result = db.restaurants.delete_many({“category”: “Bar Food“})