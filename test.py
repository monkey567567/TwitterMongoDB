import json
import pymongo
import sys

def load_json_to_mongodb(json_file, mongo_port):
    # Connect to MongoDB server
    client = pymongo.MongoClient(f"mongodb://localhost:{mongo_port}/")
    
    # Create or get the 291db database
    db = client['291db']

    # Drop existing 'tweets' collection if it exists
    if 'tweets' in db.list_collection_names():
        db.drop_collection('tweets')

    # Create a new 'tweets' collection
    tweets_collection = db['tweets']

    # Read JSON file and insert data in batches
    batch_size = 10000  # Adjust as needed
    with open(json_file, 'r') as f:
        data = json.load(f)
        tweet_batches = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

        for batch in tweet_batches:
            tweets_collection.insert_many(batch)

    print(f"Collection 'tweets' created successfully with data from {json_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python load-json.py <json_file> <mongo_port>")
        sys.exit(1)

    json_file = sys.argv[1]
    mongo_port = int(sys.argv[2])

    load_json_to_mongodb(json_file, mongo_port)
