import argparse
import os
from fetch_papers import fetch_papers
from filter_papers import filter_papers
from save_to_csv.save_to_csv import save_to_csv  # Corrected import

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("--query", required=True, help="Search query for PubMed")
    parser.add_argument("-o", "--outfile", default="results.csv", help="Output CSV filename")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print(f"\n🔹 Debug Mode ON")
        print(f"🔹 Query: {args.query}")
        print(f"🔹 Output file: {args.outfile}\n")

    print("📥 Fetching papers...")
    papers = fetch_papers(args.query)
    
    if not papers:
        print("⚠️ No papers found for the given query.")
        return

    print(f"✅ Fetched {len(papers)} papers.")
    print("🔍 Filtering papers...")
    filtered_papers = filter_papers(papers)

    if not filtered_papers:
        print("⚠️ No relevant papers after filtering.")
        return

    os.makedirs(os.path.dirname(os.path.abspath(args.outfile)), exist_ok=True)
    print(f"💾 Saving {len(filtered_papers)} papers to {args.outfile}...")

    try:
        save_to_csv(filtered_papers, args.outfile)
        print("✅ Done!")
    except Exception as e:
        print(f"❌ Error saving CSV: {e}")

if __name__ == "__main__":
    main()
