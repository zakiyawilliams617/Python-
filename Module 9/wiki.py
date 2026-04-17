"""
Retrieve Wikipedia Summary based on formatted query term.
"""
import wikipedia
import warnings

# This handles a warning message that can sometimes occur with wikipedia
warnings.filterwarnings('ignore')


def fetch_wikipedia_summary(query_term, file_name):
    # Search for article titles related to the query

    modified_term = query_term.replace(" ", "_")

    output_file = open(file_name, "a")

    results = wikipedia.search(modified_term)

    if len(results) == 0:
        output_file.write("No articles found for ' " +
                          modified_term + "'..." + "\n")
        output_file.close()
        return ""

    else:
        first_result = results[0]

        try:
            summary = wikipedia.summary(first_result)
            output_file.write("Searching Wikipedia for ''" +
                              modified_term + "''..." + "\n")
            output_file.write(
                "Summary of '" + first_result + "':" + summary + "\n")
            output_file.close()
            return summary

        except:
            output_file.write(
                "An issue occurred retrieving information for " + modified_term + "." + "\n")
            output_file.close()
            return ""
