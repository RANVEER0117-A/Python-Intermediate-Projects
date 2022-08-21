import requests     
 
def NewsFromBBC():

    query_params = {

# Api and all information of bbc news

      "source": "bbc-news",

      "sortBy": "top",

      "apiKey": "4dbc17e007ab436fb66416009dfb59a8"

    }

    main_url = " https://newsapi.org/v1/articles"
 

# Fetching data in json format

    res = requests.get(main_url, params=query_params)

    open_bbc_page = res.json()
 

# Getting all articles in a string article

    article = open_bbc_page["articles"]
 

    # Making an empty List Which Will Contain all trending news
    results = []

     

    for ar in article:

        results.append(ar["title"])

         

    for i in range(len(results)):

# printing all trending news

        print('>>',i + 1, results[i])

 #Driver Code

if __name__ == '__main__':

# Calling the function

    NewsFromBBC()