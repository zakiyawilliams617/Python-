import datetime
from apod import APOD
from rag import RAG
from wiki import fetch_wikipedia_summary

NASA_API_KEY = "diCSULnkIMl3tUySGpWvo2tVfMihSass0xVpntp6"
RESULTS_FILE = "results.txt"
IMAGE_FILE = "nasa_apod_image.jpg"
MODEL = "llama3.2"


def run_rag(date=None):
    """
    Orchestrates the full RAG pipeline:
    1. Fetch NASA APOD data for the given data
    2. Print and save original explanation
    3. Use RAG/LLM to generate Wikipedia search terms
    4. Fetch Wikipedia summaries for each term
    5. Use RAG/LLM to generate augmented description
    6. Save photo link and download image
    """

    if date is None:
        date = str(datetime.date.today())

    # 1. Fetch APOD data
    apod_obj = APOD(NASA_API_KEY)
    apod_info = apod_obj.fetch_apod(date)

    # 2. Write original explanation to results.txt and terminal
    # Open in write mode first to reset the file for thus run
    results = open(RESULTS_FILE, "w")
    results.write("Original APOD Image Information:\n")
    results.write("\n")
    results.write(apod_info["explanation"])
    results.write("\n")
    results.close()

    print("Original APOD Image Information:")
    print(apod_info["explanation"])

    # 3. Generate lookup list, this writes to file inside method
    rag_obj = RAG(MODEL)
    terms = rag_obj.generate_lookup_list(apod_info, RESULTS_FILE)

    # 4. Build Wikipedia knowledge base
    wiki_summary = ""
    i = 0
    while i < len(terms):
        term = terms[i]
        summary = fetch_wikipedia_summary(term, RESULTS_FILE)
        wiki_summary = wiki_summary + term + " " + summary + " "
        i = i + 1

    # 5. Generate and save augmented description
    augmented = rag_obj.generate_augmented_description(apod_info, wiki_summary)

    results = open(RESULTS_FILE, "a")
    results.write("\n")
    results.write("RAG Generated Description:\n")
    results.write("\n")
    results.write(augmented)
    results.write("\n")
    results.close()

    print("\nRAG Generated Description:")
    print(augmented)

    # 6. Save photo link and download image
    results = open(RESULTS_FILE, "a")
    results.write("\n")
    results.write("Link to this photo: \n")

    if "hdurl" in apod_info and apod_info["hdurl"] is not None:
        photo_url = apod_info["hdurl"]
    else:
        photo_url = apod_info["url"]

    results.write(photo_url)
    results.write("\n")
    results.close()

    apod_obj.download_image(photo_url, IMAGE_FILE)


if __name__ == "__main__":
    run_rag("2024-12-14")
