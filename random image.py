import requests

#random file form commons
def get_random_article_from_category(category): 
    url = "https://commons.wikimedia.org/wiki/api.php" 
    params = { 
        "action": "query", 
        "list": "random", 
        "rnnamespace": 0, 
        "rnlimit": 1, 
        "generator": "categorymembers", 
        "gcmtitle": f"Category:{category}",
    } 
 
    response = requests.get(url, params=params) 
    data = response.json() 
 
    if 'random' in data['query']: 
        return data['query']['random'][0]['title'] 
    else: 
        return None 
 
# Example usage 
random_article = get_random_article_from_category("Science") 
print(f"Random Article: {random_article}")
