Name: Zakiya Williams

Module Info: Module  Assignment 9: Generative Artificial Intelligence  Due on 03/29/2026

Approach:
Overall Structure - The solution was broken into five files (api.py, apod.py, wiki.py, rag.py, and main.py), each with a specific responsibility.

api.py
A base API class was created to handle the GET requests. It stores a base URL and optional API key as instance variables and has a get_response() method that sends a GET request and returns the JSON response. This class was designed to be reusable and extendable by any API.

apod.py
The APOD class extends the base API class using inheritance. Its constructor calls the parent constructor with the NASA APOD URL and API key. It adds two methods: fetch_apod() which builds the request parameters and retrieves the photo data for a specific date, and download_image() which downloads and saves the photo as a binary file.

wiki.py
A standalone function fetch_wikipedia_summary() was created that takes a query term and file name, replaces spaces with underscores in the query term, searches Wikipedia, retrieves the summary of the first result, writes the findings to the results file, and returns the summary string for use as part of the knowledge base.

rag.py
The RAG class handles all interaction with the Ollama LLM. It has three methods: rag_response() which sends any prompt to the LLM and returns the text response, generate_lookup_list() which uses the provided lookup_prompt to ask the LLM what terms to look up on Wikipedia and then parses the returned string into a real Python list, and generate_augmented_description() which uses the provided rag_prompt along with the original photo explanation and Wikipedia summaries to generate a betterr, more detailed description of the photo.

main.py
The run_rag() function connects everything together, it fetches the APOD data, writes the original explanation to the terminal and results file, generates the Wikipedia lookup terms via the RAG class, fetches Wikipedia summaries for each term and builds them into one knowledge base string, sends everything to the LLM to generate an augmented description, and finally saves the photo link and downloads the image. The default date is set to today using datetime but defaults to "2024-12-14".

Known Bugs: n/a
Citation: n/a
