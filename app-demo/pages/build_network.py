# -*- coding: utf-8 -*-
""" Build network Streamlit page """
from datetime import datetime

import pandas as pd
import streamlit as st

from graph_building.converter import WikipediaConverter, WikidataConverter, init_graph
from .helpers import get_session_state_val, check_session_state_value, \
    init_update_session_state

@st.cache(show_spinner=False)
def build_network(df_wp, df_wd):
    """ Build graph with rdf triples """
    graph = init_graph()
    converter_wp = WikipediaConverter()
    graph, counter = converter_wp(graph, df_wp)

    converter_wd = WikidataConverter()
    return converter_wd(graph, df_wd, counter)

def app():
    """ Main app page """
    st.title("Build the network")

    st.markdown("""
    Where would you like the knowledge graph to be downloaded? Please fill in the location as a path including:
    the name of the file and ending with '.ttl'. 
    For example: C:/Users/LauraBrongers/Documents/sony csl internship/knowledge_graph_FR.ttl
    """)
    
    selected_destination = st.text_area("Fill in location + file name + .ttl here", "C:/Users/example_path/example_knowledge_graph_name.ttl")
    
    st.markdown(f" You selected: {selected_destination}")
    
    st.markdown("""
    #
    Clicking the button below will have the narrative network constructed: 
    Extracted info from last steps will be converted to RDF triples.
    """)

    df_wp = get_session_state_val(var="wikipedia_for_graph")
    df_wd = get_session_state_val(var="wikidata_for_graph")

    if isinstance(df_wd, pd.DataFrame) and isinstance(df_wp, pd.DataFrame):

        st.write("##")
        if st.button("Build network"):

            # populating ontology by converting wikipedia semi-structured data
            # and wikidata triples
            build_start = datetime.now()
            graph, _ = build_network(df_wp=df_wp, df_wd=df_wd)
            # adjust destination path to your prefered location to save the knowledge graph
            graph.serialize(destination=selected_destination, format="turtle") 

            if check_session_state_value(var="data_in_cache", value=True):
                init_update_session_state(var="graph", value=graph)
            build_end = datetime.now()

            init_update_session_state(var="build_nt_time",
                                      value=build_end - build_start)
            st.markdown(f"_It took {st.session_state['build_nt_time']} s_")

            st.success("Building done!")
            st.balloons()
