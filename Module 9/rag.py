from ollama import chat


class RAG:
    # constructor - stores the LLM model name
    def __init__(self, model):
        self.model = model

    def rag_response(self, prompt):
        # sends a prompt to the ollama LLM and returns the txt response
        response = chat(model=self.model, messages=[
                        {"role": "user", "content": prompt}])
        return response.message.content

    def generate_lookup_list(self, apod_info, file_name):
        # uses the LLM to generate a list of Wikipedia search terms
        # from the APOD photo explanation,
        # writes terms to file and returns them
        photo_explanation = apod_info["explanation"]

        lookup_prompt = ("Analyze the following and based on the information provided, create a list of terms to look up for more information. The list should be returned as a list of strings in python format. No other information should be returned. Information: " + photo_explanation)

        raw_string = self.rag_response(lookup_prompt)

        # convert the sinle stringreturned by LLM into a python list
        raw_string = raw_string.strip()

        if raw_string[0] == "[":
            raw_string = raw_string[1:]

        if raw_string[len(raw_string) - 1] == "]":
            raw_string = raw_string[:len(raw_string) - 1]

        raw_items = raw_string.split(",")

        terms = []
        i = 0
        while i < len(raw_items):
            item = raw_items[i].strip()
            if len(item) > 0 and (item[0] == "'" or item[0] == '"'):
                item = item[1:]
            if len(item) > 0 and (item[len(item) - 1] == "'" or item[len(item) - 1] == '"'):
                item = item[:len(item) - 1]
            if len(item) > 0:
                terms.append(item)
            i = i + 1

        # write terms to file
        output_file = open(file_name, "a")
        output_file.write("Additional Search Terms:\n")
        j = 0
        while j < len(terms):
            output_file.write("\u2022 '" + terms[j] + "'\n")
            j = j + 1
        output_file.close()

        return terms

    def generate_augmented_description(self, apod_info, wiki_summary):

        photo_title = apod_info["title"]
        photo_explanation = apod_info["explanation"]

        rag_prompt = (
            ' ""NASA APOD Title: ' + photo_title + "\n"
            "Explanation: " + photo_explanation + "\n"
            "Additional Context from Wikipedia:\n"
            + wiki_summary + "\n"
            "Write a more detailed and accessible description of the image using all of the above. \n"
            '"""'
        )

        result = self.rag_response(rag_prompt)
        return result
