import os
from Bio import Entrez, Medline

def search_pubmed(keyword):
    """
    Search articles in PubMed with the given keyword and return a list of dictionaries
    containing article details such as PMID, Title, Abstract, and MeSH terms.
    """
    Entrez.email = "your.email@example.com"  # Always provide your email
    handle = Entrez.esearch(db="pubmed", term=keyword, retmax=10)
    record = Entrez.read(handle)
    handle.close()

    id_list = record["IdList"]
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="text")
    records = Medline.parse(handle)

    articles = []
    for record in records:
        article = {
            "PMID": record.get("PMID", ""),
            "Title": record.get("TI", ""),
            "Abstract": record.get("AB", ""),
            "MeSH Terms": "; ".join(record.get("MH", []))
        }
        articles.append(article)

    return articles

def save_as_tsv(articles, filename="output.tsv"):
    """
    Save a list of article details to a TSV file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        # Write header
        file.write("PMID\tTitle\tAbstract\tMeSH Terms\n")

        # Write article data
        for article in articles:
            file.write(f"{article['PMID']}\t{article['Title']}\t{article['Abstract']}\t{article['MeSH Terms']}\n")

# Example usage
keyword = "diabetes"  # replace with your actual search term
articles = search_pubmed(keyword)
save_as_tsv(articles, "pubmed_articles.tsv")

