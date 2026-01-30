# Knowledge Graph–Based Learning Path Recommendation System

A web-based system that leverages a large-scale course knowledge graph and large language models to support course structure visualization, question answering, and personalized learning path recommendation.


## Overview

This project constructs a hierarchical course knowledge graph with prerequisite relationships and integrates it into an interactive web system.  
By combining graph-based reasoning with large language models (ChatGLM and KP-GLM), the system helps learners understand course structures and plan effective study paths.


## Project Structure

```bash
neo4j-knowledge-graph/   # Neo4j graph data and database files
frontend/               # Vue-based frontend (Element-Plus, D3.js)
backend/                # Backend APIs and graph query services
```
## Knowledge Graph Statistics
Entities: 35,533

Course (105), Chapter (944), Section (6,952), Subsection (27,525)

Relations: 50,929

Contains (49,726), Prerequisite (1,003)

## Key Features
Interactive visualization of course structures

Graph-based search and navigation

Learning path recommendation based on prerequisite reasoning

Question answering enhanced by large language models

## Tech Stack
Frontend: Vue, Element-Plus, Axios, D3.js

Backend: REST APIs, Neo4j

Models: ChatGLM, KP-GLM

## Frontend Preview
**Guide**
![Guide](frontend/screenshots/guide.png)

**Graph Visualization View**
![Graph View](frontend/screenshots/graph_view.png)

**Course Search Panel**
![Search Panel](frontend/screenshots/search_panel.png)

**Learning Path Recommendation**
![Learning Path](frontend/screenshots/path_recommendation.png)
![Learning Path](frontend/screenshots/path_recommendation2.png)
## License
For academic and research use.