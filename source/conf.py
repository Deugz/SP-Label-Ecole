# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Label Ecole V0'
copyright = '2024, Vincent Deguin'
author = 'Vincent Deguin'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

comments_config = {
   "utterances": {
      "repo": "https://github.com/Deugz/SP-Label-Ecole",
      "optional": "config",
   }
}

comments_config = {
   "hypothesis": True
}



extensions = [
  
  "myst_parser",
  "sphinx_design",
  "sphinx_comments",
  "sphinx_new_tab_link",
  "sphinx_book_theme",
  "sphinx_togglebutton",
  "sphinx_thebe",
]

myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2



templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = "_static/logos/Label-Ecole-Logo.png"
html_favicon = "_static/logos/Label-Ecole-Logo.png"
html_static_path = ['_static']

html_theme_options = {
    "external_links": [
        {
            "url": "https://deugz.github.io/SP-Label-Ecole/build/html/content/Organisation.html",
            "name": "&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 🔧 Organisation",
            "attributes": {"target": "_blank"},
        },
        {
            "url": "https://deugz.github.io/SP-Label-Ecole/build/html/content/Cours.html",
            "name": "&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 🎓 Cours",
            "attributes": {"target": "_blank"},
        },        
        {
            "url": "https://deugz.github.io/SP-Label-Ecole/build/html/content/Projet.html",
            "name": "&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp ✨ Le Projet",
            "attributes": {"target": "_blank"},
        },


    ],
    "header_links_before_dropdown": 10,    
    "icon_links": [
        {
            "name": "Discord",
            "url": "https://github.com/Deugz/Encyclopedia-Home",
            "icon": "fa-brands fa-discord",
        },
        {
            "name": "Drive",
            "url": "https://github.com/Deugz/Encyclopedia-Home",
            "icon": "fa-brands fa-google-drive",
        },
        {
            "name": "Calendrier",
            "url": "https://github.com/Deugz/Encyclopedia-Home",
            "icon": "fa-regular fa-calendar-days",
        },
        {
            "name": "Site web",
            "url": "https://www.disqutons.fr/",
            "icon": "fa-solid fa-globe",
        },        
        {
            "name": "GitHub",
            "url": "https://github.com/Deugz/Encyclopedia-Home",
            "icon": "fa-brands fa-github",
        },
    ],
    
    "logo": {
        "text": "&nbsp &nbsp Label Ecole",
        "image_dark": "_static/Logo/logo_SFTP.png",
        "alt_text": "",
    },
    
    
    "navbar_start": ["navbar-logo"],
    
}


html_css_files = ["css/custom_style.css", "css/slider.css", "css/flash-card.css",'https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Montserrat:wght@400;700&display=swap',]
html_js_files = ["_static/assets/scripts/slider-script.js"]

    
