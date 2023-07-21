"""Knowledge Graph Completion (KGC) with causal link actraction using the OpenAI GPT API in one single prompt"""
import openai
import wikipedia

openai.api_key = "<YOUR OPENAI KEY HERE>"

def GPT_API(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

FR_wikipedia_texts = ["First White Terror (French Revolution)", "Coup of 9 Thermidor (French Revolution)",\
"Reveillon Riot (French Revolution)", "massacres of La Glacière (French Revolution)", \
"Storming of the Bastille (French Revolution)"]

RU_wikipedia_texts = ["Kerch Strait incident (Russo-Ukrainian War)", \
"2017 cyberattacks on Ukraine (Russo-Ukrainian War)", "Minsk agreements (Russo-Ukrainian War)", \
"blockade of the Azov Sea (Russo-Ukrainian War)", \
"annexation of Crimea by the Russian Federation (Russo-Ukrainian War)"]

PR_wikipedia_texts = ["Removal of Hungary's border fence (Peaceful Revolution)", \
"Fall of the inner German border (Peaceful Revolution)", \
"Monday demonstrations in East Germany (Peaceful Revolution)", \
"Fall of the Berlin Wall (Peaceful Revolution)", "40th anniversary of GDR (Peaceful Revolution)"]

historical_events = [FR_wikipedia_texts, RU_wikipedia_texts, PR_wikipedia_texts]  

for hist_event in historical_events:
    for text in hist_event:
        wiki_summary = wikipedia.summary(text)
        KGC_single_prompt = f"""
        Return the causal links between the events in the form of Resource Description Framework (RDF) triples from {wiki_summary}. 
        For each causal link return 3 triples. 
        First, return a triple including the unique identifier of the first event, the "has effect" predicate and the unique 
        identifier of the second event. E.g., ex:event_1 wd:P1542 ex:event_2. 
        Second, return a triple with the unique identifier of the first event, the “label” predicate and the name of the event in 
        string form. The unique identifier starts with the prefix "ex:event_" followed by a unique number that is used for only one 
        event. E.g., ex:event_1 rdfs:label “Battle of Neuburg".
        Third, return a triple with the unique identifier of the second event, the label predicate and the name of the second event 
        in string form. E.g., ex:event_2 rdfs:label "end of Austrian control over the River Danube”.

        Assign unique identifiers in the format "ex:event_X" to each event, where X represents a number starting from 1 and 
        incrementing for each new event. If a unique event occurs in more than one causal link, then return the triple with the 
        label for that event only once. E.g. these are two causal links that both use the same event:
        ex:event_13 wd:P1542 ex:event_14 .
        ex:event_13 rdfs:label "5 August 2019 Hong Kong anti-extradition bill protest" .
        ex:event_14 rdfs:label "10 August 2019 Hong Kong anti-extradition bill protest" .

        ex:event_14 wd:P1542 ex:event_15 .
        ex:event_15 rdfs:label "Global Anti-totalitarianism Protest" .

        Below are some more examples of causal links in RDF form:
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

        ex:event_18 wd:P1542 ex:event_19.
        ex:event_18 rdfs:label "2014 Russian invasion of Crimea".
        ex:event_19 rdfs:label "Crimean referendum, 2014".

        ex:event_18 wd:P1542 ex:event_20.
        ex:event_20 rdfs:label "declaration of Independence of the Republic of Crimea".

        ex:event_18 wd:P1542 ex:event_21.
        ex:event_21 rdfs:label "Treaty on the Adoption of the Republic of Crimea to Russia".

        Make sure to return the triple with the label of a unique event only once per event, even if the event occures in more 
        than one causal link. And each triple should get their own unique identifyer.
        """ 
        output_triples = GPT_API(KGC_single_prompt) 

        # store the final output in a new file
        if hist_event == FR_wikipedia_texts:
            with open("FR2_single_prompt_output.ttl", "a", encoding="utf-8") as file:
                file.write(output_triples)

        if hist_event == RU_wikipedia_texts:
            with open("RU2_single_prompt_output.ttl", "a", encoding="utf-8") as file:
                file.write(output_triples)

        if hist_event == PR_wikipedia_texts:
            with open("PR2_single_prompt_output.ttl", "a", encoding="utf-8") as file:
                file.write(output_triples)