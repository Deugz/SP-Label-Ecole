## Vince

<input type="password" id="password" placeholder="Mot de passe">
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