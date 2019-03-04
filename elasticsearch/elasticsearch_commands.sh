GET localhost:9200 # base url for elasticsearch

# LOAD DATA IN BULK
curl -H "Content_Type: application/json" -X POST 'localhost:9200/shakespeare/_bulk?pretty' --data-binary @shakespeare.json
curl -H 'Content-Type: application/json' -XPOST 'localhost:9200/bank/account/_bulk?pretty' --data-binary @accounts.json


POST localhost:9200/accounts/person/1 # automatically creates the accounts index
{
    "name" : "John",
    "lastname" : "Doe",
    "job_description" : "Systems administrator and Linux specialit"
}

GET localhost:9200/accounts/person/1 # get request for that specific id
GET localhost:9200/_search?q=john # query search API by any field containing "john"
GET localhost:9200/_search?q=j* # query search API ie. LIKE 'j%'
GET localhost:9200/_search?q=job_description:john # query for field "job description" containing "linux"

# within accounts index and person document use the query API 
GET localhost:9200/accounts/person/_search?q=job_description:linux 

DELETE localhost:9200/accounts/person/1 # DELETE record

POST localhost:9200/accounts/person/1/_update # UPDATE request by ID
{
      "doc":{
       "job_description" : "Systems administrator and Linux specialist"
     }
}


# grabs ALL documents in the sharespeare index
GET localhost:9200/shakespeare/_search
{
    "query": {
            "match_all": {}
    }
}

GET localhost:9200/shakespeare/_search # get all
{
    "query": {
            "match_all": {}
    }
}

# where play_name field = "Anthony"
POST localhost:9200/shakespeare/scene/_search/
{
    "query":{
        "match" : {
            "play_name" : "Antony"
        }
    }
}

# where play_name = "Anthony"
# speaker also equals = "Demetrius"
# in SQL: play_game = 'Antony' AND speaker = 'Demetrius'
POST localhost:9200/shakespeare/scene/_search/
{
    "query":{
        "bool": {
             "must" : [
                 {
                    "match" : {
                        "play_name" : "Antony"
                    }
                 },
                 {
                    "match" : {
                        "speaker" : "Demetrius"
                    }
                 }
             ]
        }
    }
}
