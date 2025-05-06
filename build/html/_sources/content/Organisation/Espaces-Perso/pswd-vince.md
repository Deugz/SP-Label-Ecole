# Vince

***

::::{grid} 2

:::{grid-item}
:columns: 6

```{note}

créer une div avec le mdp à droite et une toff à gauche

```

:::

:::{grid-item}
:columns: 6

<br>

<input type="password" id="password" placeholder="Mot de passe">

<br>

<button onclick="checkPassword()">Valider</button>
<p id="error" style="color: red;"></p>

<script>
    function checkPassword() {
      const password = document.getElementById("password").value;
      const correctPassword = "monmotdepasse";  // à changer

      if (password === correctPassword) {
        window.location.href = "Vince.html";  // redirection si bon mot de passe
      } else {
        document.getElementById("error").textContent = "Mot de passe incorrect.";
        document.getElementById("password").value = "";
      }
    }
</script>

:::

::::

## Un peu de contexte

- [Fiche de poste originale](Docs/EC_ETUD-Assistant.eProgramManager.pdf)

- [Docs passation Iris]()

- [Déroulé péda Ines]()


## Descriptif du Poste

En 2023, Label École souhaite développer son offre de formation en proposant des parcours en alternance. De plus, nous avons pour ambition d’ouvrir de nouveaux campus sur le territoire métropolitain. Afin d’accompagner notre Program Manager dans cette phase de croissance, nous recherchons un.e assistant.e en stage ou alternance. Sous la supervision d’une Program Manager de Label École, vos missions seront les suivantes : 

### Soutien à l’organisation et suivi des formations (30%) 

- Coordination de la production des différents supports de formation

- Suivi administratif des apprenant.es (inscription, rémunération)

- Suivi des formateur.rices

- Suivi des absences et retards

### Suivi des stagiaires de la formation (40%) 

- Accompagnement des apprenant.es sur leur projet de formation

- Préparation aux examens

- Reporting de l’avancement des projets apprenant.es

### Développement d’outils de communication (30%) 

- Gestion des réseaux sociaux de l'école

- Création de newsletter

- Rédaction d'articles de blog

## Profil recherché 

- Tu es étudiant.e en 3ᵉ, 4ᵉ ou 5ᵉ année d’une école de commerce, d’un IAE, d’un IEP, d’une école du web, en gestion des ressources humaines.

- Tu es polyvalent.e et flexible, tu aimes travailler sur différents sujets : un vrai couteau suisse, capable de s’adapter aussi bien à nos formateur.rices qu’à nos apprenant.es.

- Tu as un goût pour le rédactionnel et la pédagogie.

- Tu es curieux.se, humble et enthousiaste.

- Tu sais donner ton avis pour faire évoluer les pratiques dans un environnement en pleine croissance où tout reste à faire.

- Tu as un fort intérêt pour l'Économie Sociale et Solidaire.

- La maîtrise de la suite Adobe (Illustrator, Photoshop, InDesign) est un plus. 

