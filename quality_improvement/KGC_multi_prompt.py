"""Knowledge Graph Completion (KGC) with causal link actraction using the OpenAI GPT API with multiple prompts"""
import openai
import wikipedia
from get_wikipedia_texts import FR_wiki_text, RU_wiki_text, PR_wiki_text

openai.api_key = "<YOUR OPENAI KEY HERE>"

def GPT_API(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

trip_ex = f'''
ex:event_1 wd:P1542 ex:event_2. 
ex:event_1 rdfs:label "coup of 18 Brumaire".
ex:event_2 rdfs:label "French Consulate".

ex:event_3 wd:P1542 ex:event_4.
ex:event_3 rdfs:label "2022 referendums in Russian-occupied Ukraine".
ex:event_4 rdfs:label "Russian annexation of Donetsk, Kherson, Luhansk and Zaporizhzhia oblasts".

ex:event_5 wd:P1542 ex:event_6.
ex:event_5 rdfs:label "annexation of Crimea by the Russian Federation".
ex:event_6 rdfs:label "international reactions to the annexation of Crimea by the Russian Federation".

ex:event_7 wd:P1542 ex:event_8.
ex:event_7 rdfs:label "prelude to the Russian invasion of Ukraine".
ex:event_8 rdfs:label "reactions to 2021–2022 Russo-Ukrainian crisis".

ex:event_9 wd:P1542 ex:event_10.
ex:event_9 rdfs:label "First Opium War".
ex:event_10 rdfs:label "Treaty of Nanjing".

ex:event_11 wd:P1542 ex:event_12.
ex:event_11 rdfs:label "murder of George Floyd".
ex:event_12 rdfs:label "George Floyd protests".

ex:event_13 wd:P1542 ex:event_14.
ex:event_13 rdfs:label "12 June 2019 Hong Kong protest".
ex:event_14 rdfs:label "Second reading debate on the extradition bill postponed".

ex:event_15 wd:P1542 ex:event_16.
ex:event_15 rdfs:label "October 2013 protests".
ex:event_16 rdfs:label "Founding of March Against Myths About Modification (MAMyths)".
'''
ex1 = f'''
ex:event_9 wd:P1542 ex:event_10.
ex:event_9 rdfs:label "First Opium War".
ex:event_10 rdfs:label "Treaty of Nanjing".
'''

ex2 = f'''
ex:event_9 wd:P1542 ex:event_10.
event_9 a sem:Event.
ex:event_9 rdfs:label "First Opium War".
event_10 a sem:Event.
ex:event_10 rdfs:label "Treaty of Nanjing". 
'''


historical_events = [FR_wiki_text, RU_wiki_text, PR_wiki_text]

for hist_event in historical_events:
    KGC_multiple_prompt1 = f"""
    {hist_event} is a text from Wikipedia about historical events. Return the causal 
    relationships between the events in the text. Return one sentence per causal relationship 
    """ 
    output1 = GPT_API(KGC_multiple_prompt1)
    #print("output 1:\n", output1, "\n")

    KGC_multiple_prompt2 = f"""
    Use the causal relationships from {output1} and rewrite them in the form of triples: 
    <first event, causal relation, second event>. Make sure to give the events a concise name
    """
    output2 = GPT_API(KGC_multiple_prompt2)
    #print("output 2:\n", output2, "\n")

    KGC_multiple_prompt3 = f"""
    Return the causal relationships in {output2} in the form of Resource Description Framework 
    (RDF) triples. For each causal link return 3 triples:
    First, return a triple including the unique identifier of the first event, the "has effect" 
    predicate and the unique identifier of the second event. E.g., ex:event_1 wd:P1542 ex:event_2. 
    Second, return a triple with the unique identifier of the first event, the “label” predicate 
    and the name of the event in string form. The unique identifier starts with the prefix 
    "ex:event_" followed by a unique number that is used for only one event. 
    E.g., ex:event_1 rdfs:label “Battle of Neuburg".
    Third, return a triple with the unique identifier of the second event, the label predicate 
    and the name of the second event in string form. E.g., ex:event_2 rdfs:label "end of 
    Austrian control over the River Danube”
    {trip_ex} contains more examples. Do not add a disclaimer or any text other then the triples
    """
    output3 = GPT_API(KGC_multiple_prompt3)
    #print("output 3:\n", output3, "\n")

    KGC_multiple_prompt4 = f"""
    {output3} is a list of triples in RDF form. For each line with a rdfs:label in it, 
    add the following text above that line: 
    ex:event_X a sem:Event.
    In this example the X stands for unique identifier of the event.
    E.g. {ex1} becomes {ex2}. Return the updated triples list
    """
    output_triples = GPT_API(KGC_multiple_prompt4)
    #print("final output :\n", output_triples, "\n")

    # append the final output to the original knowledge graph
    if hist_event == FR_wiki_text:
        with open("../quality_evaluations/SHACL/data_graphs/FR3_data_graph.ttl", "a") as file:
            file.write(output_triples)

    if hist_event == RU_wiki_text:
        with open("../quality_evaluations/SHACL/data_graphs/RU3_data_graph.ttl", "a") as file:
            file.write(output_triples)

    if hist_event == PR_wiki_text:
        with open("../quality_evaluations/SHACL/data_graphs/PR3_data_graph.ttl", "a") as file:
            file.write(output_triples)