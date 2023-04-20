// Lorsque l'utilisateur fait défiler la page, exécutez myFunction
window.onscroll = function() {myFunction()};

// Obtenir la barre de navigation
let navbar = document.getElementById("navbar");

// Obtenir la position de décalage de la barre de navigation
let sticky = navbar.offsetTop;

// Ajoutez la classe collante à la barre de navigation lorsque vous atteignez sa position de défilement. Supprimer "collant" lorsque vous quittez la position de défilement
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

