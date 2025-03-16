import requests
import xml.etree.ElementTree as ET

def fetch_papers(query):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    
    try:
        search_url = f"{base_url}esearch.fcgi?db=pubmed&term={query}&retmode=json"
        response = requests.get(search_url)
        response.raise_for_status()
        data = response.json()
        paper_ids = data.get("esearchresult", {}).get("idlist", [])
        
        if not paper_ids:
            print(f"⚠️ No papers found for query: {query}")
            return []

        fetch_url = f"{base_url}efetch.fcgi?db=pubmed&id={','.join(paper_ids)}&retmode=xml"
        response = requests.get(fetch_url)
        response.raise_for_status()
        
        root = ET.fromstring(response.text)
        papers = []

        for article in root.findall(".//PubmedArticle"):
            paper_id = article.findtext(".//PMID", "")
            title = article.findtext(".//ArticleTitle", "")
            source = article.findtext(".//Journal/Title", "")
            affiliation = article.findtext(".//AffiliationInfo/Affiliation", "").strip()
            publication_date = article.findtext(".//PubDate", "")
            
            email = ""
            for author in article.findall(".//Author"):
                email_text = author.findtext(".//AffiliationInfo/Affiliation", "")
                if "@" in email_text:
                    email = email_text
                    break  

            papers.append({
                "id": paper_id,
                "title": title,
                "publication_date": publication_date,
                "affiliation": affiliation,
                "corresponding_author_email": email
            })

        print(f"✅ Fetched {len(papers)} papers.")
        return papers

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching papers: {e}")
        return []
