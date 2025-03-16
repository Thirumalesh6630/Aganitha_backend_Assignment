def is_non_academic(author_affiliation):
    if not author_affiliation:  
        return False  
    non_academic_keywords = [
        "inc", "ltd", "corp", "biotech", "pharma", "technologies", 
        "llc", "gmbh", "solutions", "systems", "research lab", "company"
    ]
    return any(keyword in author_affiliation.lower() for keyword in non_academic_keywords)

def filter_papers(papers):
    filtered_papers = []
    
    for paper in papers:
        affiliation = paper.get("affiliation", "").strip()
        is_non_academic_flag = is_non_academic(affiliation)
        
        print(f"📌 Paper ID: {paper.get('id', 'N/A')} | Affiliation: '{affiliation or 'N/A'}' | "
              f"{'✅ Non-Academic' if is_non_academic_flag else '❌ Academic'}")

        if is_non_academic_flag:
            filtered_papers.append(paper)

    return filtered_papers
