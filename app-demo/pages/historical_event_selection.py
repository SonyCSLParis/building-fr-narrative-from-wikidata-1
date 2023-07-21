# -*- coding: utf-8 -*-
"""
Streamlit page: historical event selection
"""

import os
import yaml
import streamlit as st
from pages.helpers import historical_event

def app():
    """ Main app function """
    st.title("Historical Event Selection")

    st.markdown(
        """
        The aim of this demo was to study the replication of the narrative builder with different historical events.
        The historical events used are the French Revolution, the Russo-Ukrainian War and the Peaceful Revolution.
        """)
    historical_event()
   

    st.markdown(f" You selected: {st.session_state['hist_event']}")
