# -*- coding: utf-8 -*-
"""
Main app script for the streamlit web interface:
Home: describing the project
1. Historical Event Selection: select which historical event to create a narrative network for
2. Event Collection: collect data from wikidata (events)
3. Wikidata Enrichment: extracting outoging nodes from Wikidata
4. Link Extraction: Extracting semi structured data from Wikipedia (infoboxes)
5. Build Network: Populate simple event model ontology
6. Display Network: Visualising the steps of network construction
"""

import streamlit as st
from pages import historical_event_selection, event_collection, home, infobox_extraction, \
    build_network, display_network, wikidata_retrieval

PAGES = {
    "Home": home,
    "1. Historical Event Selection": historical_event_selection,
    "2. Event Collection": event_collection,
    "3. Wikidata Enrichment": wikidata_retrieval,
    "4. Link Extraction": infobox_extraction,
    "5. Build Network": build_network,
    "6. Display Network": display_network
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
st.session_state["data_in_cache"] = True

page = PAGES[selection]
page.app()
