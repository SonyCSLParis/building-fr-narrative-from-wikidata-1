# Narrative Prototype Replication

This project is a second prototype on narrative building. In particular, the focus of the study is the creation of knowledge graphs (KGs) about the French Revolution, the Russo-Ukrainian War and the Peaceful Revolution. The idea is to explore events and participants throughout structured ([Wikidata](https://www.wikidata.org)) and unstructured ([Wikipedia](https://www.wikipedia.org)) data. Structured data can help better grasp the main entities, objects or events, while unstructured data, like text, can help make hypotheses on how events are linked. Additionally, the created narrative structures (in the form of KGs) can be evaluated on their quality with SPARQL queries and SHACL shapes.

---
## Set Up

If using https, run:
```python
git clone https://github.com/SonyCSLParis/building-fr-narrative-from-wikidata1.git 
cd building-fr-narrative-from-wikidata1
```

If using ssh, run:
```python
git clone git@github.com:SonyCSLParis/building-fr-narrative-from-wikidata1.git
cd building-fr-narrative-from-wikidata1
```

In the `settings` folder, create a `private.py` file and add the following paramters:
* ROOT_PATH: <root path to the project directory>
* AGENT: <your user agent which you can find on https://whatmyuseragent.com/>

Create a virtual environment and activate it:
```bash
conda create -n <yourenvname> python=3.9.4
conda activate <yourenvname>
```

```bash
pip install -r requirements.txt
```

```bash
python setup.py install
```

Finally, to run the streamlit app
```bash
cd app-demo && streamlit run app.py
```
---

## Start up

When you installed the system with the instructions in Set up, you can start the system again in your next visit by running the following:

Activate your virtual environment:
```bash
conda activate <yourenvname>
```
activate the streamlit app:
```bash
cd app-demo && streamlit run app.py
```

## Troubleshooting
Later when launching the app, you might encounter the following error:
```bash
ImportError: pycurl: libcurl link-time ssl backends (secure-transport, openssl) do not include compile-time ssl backend (none/other)
```

To prevent this error, and following [this link](https://stackoverflow.com/questions/21096436/ssl-backend-error-when-using-openssl), you can run the followings:
```bash
pip uninstall pycurl
export PYCURL_SSL_LIBRARY=openssl
pip install pycurl --no-cache-dir
```

---

## Quality Evaluation

To evaluate the quality of the replications with SHACL, each knowledge graph (KG) has to be evaluated separately.

For the French Revolution KG created in the replication phase, run:
'''bash
pyshacl -s quality_evaluations/SHACL/shape_graph.ttl -f table quality_evaluations/SHACL/data_graphs/FR1_data_graph.ttl -o quality_evaluations/SHACL/SHACL_output_files/FR1_output_file
'''

For the Russo-Ukrainian War KG created in the replication phase, run:
'''bash
pyshacl -s quality_evaluations/SHACL/shape_graph.ttl -f table quality_evaluations/SHACL/data_graphs/RU1_data_graph.ttl -o quality_evaluations/SHACL/SHACL_output_files/RU1_output_file
'''

For the Peaceful Revolution KG created in the replication phase, run:
'''bash
pyshacl -s quality_evaluations/SHACL/shape_graph.ttl -f table quality_evaluations/SHACL/data_graphs/PR1_data_graph.ttl -o quality_evaluations/SHACL/SHACL_output_files/PR1_output_file
'''

For the French Revolution KG created in the improvement phase, run:
'''bash
pyshacl -s quality_evaluations/SHACL/shape_graph.ttl -f table quality_evaluations/SHACL/data_graphs/FR2_data_graph.ttl -o quality_evaluations/SHACL/SHACL_output_files/FR2_output_file
'''

For the Russo-Ukrainian War KG created in the improvement phase, run:
'''bash
pyshacl -s quality_evaluations/SHACL/shape_graph.ttl -f table quality_evaluations/SHACL/data_graphs/RU2_data_graph.ttl -o quality_evaluations/SHACL/SHACL_output_files/RU2_output_file
'''

For the Peaceful Revolution KG created in the improvement phase, run:
'''bash
pyshacl -s quality_evaluations/SHACL/shape_graph.ttl -f table quality_evaluations/SHACL/data_graphs/PR2_data_graph.ttl -o quality_evaluations/SHACL/SHACL_output_files/PR2_output_file
'''

## Knowledge Graph Completion with Causal Links

To improve the original narrative builder, this section performs a knowledge graph completion task. 
The completion refers to the addition of causal links between events. The causal links are retrieved
from Wikipedia with the Chat GPT API. Note that you have to fill in your own API key first.

'''bash
cd quality_improvement && python causal_link_extraction.py
'''

## Structure

- [app-demo](./app-demo)

  Streamlit web application to collect data and build networks.

- [graph_building](./graph_building)

  Module to build networks using networkx or pyvis.

- [settings](./settings)

- [kb_sparql](./kb_sparql) 
  
  Using a SPARQL wrapper to query wikidata, as well as the knowledge graph created throughout the process.

- [wikipedia_narrative](./wikipedia_narrative)

    Used for the pilot: mapping Wikidata/Wikipedia, extracting infoboxes and text from Wikipedia
  
- [quality_evaluations](./quality_evaluations)

- [adding_causal_links](./adding_causal_links)

---
## References



<img align="left" width="70" height="50" src=./Flag_of_Europe.svg.png>

The work reported in this paper was funded by the [European MUHAI project](https://muhai.org) from the  Horizon 2020 research and innovation  programme under grant number 951846 and the Sony Computer Science Laboratories Paris.
<br/>
<br/>
This work is also the result of a joint collaboration between the following partners in the project: [Sony CSL Paris](https://csl.sony.fr/project/building-narratives-computationally-from-knowledge-graphs/) & [Vrije Universiteit Amsterdam](https://krr.cs.vu.nl)

Contact: [Laura Brongers](mailto:laura.brongers@gmail.com)

[Corresponding paper link](<to-be-completed-when-proceedings-out>)

---
## Citation
If using this work, please cite the following:

```<to-be-completed-when-proceedings-out>```
