''' Wikipedia texts used for causal link extraction in the quality improvement phase '''
import wikipedia

# pre-selected titles of wikipedia texts (5 per historical event)
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

FR_wiki_text = ""
for title in FR_wikipedia_texts:
    wiki_summary = wikipedia.summary(title)
    with open("FR_wikitext<version>.ttl", "a", encoding="utf-8") as file:
        file.write(wiki_summary)
    with open("FR_wikitext<version>.ttl", "a", encoding="utf-8") as file:
        file.write("\n\n")
    FR_wiki_text = FR_wiki_text + wiki_summary + "\n\n"

RU_wiki_text = ""
for title in RU_wikipedia_texts:
    wiki_summary = wikipedia.summary(title)
    with open("RU_wikitext<version>.ttl", "a", encoding="utf-8") as file:
        file.write(wiki_summary)
    with open("RU_wikitext<version>.ttl", "a", encoding="utf-8") as file:
        file.write("\n\n")
    RU_wiki_text = RU_wiki_text + wiki_summary + "\n\n"

PR_wiki_text = ""
for title in PR_wikipedia_texts:
    wiki_summary = wikipedia.summary(title)
    with open("PR_wikitext<version>.ttl", "a", encoding="utf-8") as file:
        file.write(wiki_summary)
    with open("PR_wikitext<version>.ttl", "a", encoding="utf-8") as file:
        file.write("\n\n")
    PR_wiki_text = PR_wiki_text + wiki_summary + "\n\n"