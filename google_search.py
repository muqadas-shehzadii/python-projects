from googlesearch import search

query = input("Enter your search query: ")
for url in search(query):
    print(url)
