let prevScrollpos = window.window.scrollY;

window.onscroll = function() {
  let currentScrollPos = window.window.scrollY;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navBarHorizontal").style.top = "0";
  } else {
    document.getElementById("navBarHorizontal").style.top = "-50px"; // Ajusta según la altura de tu barra de navegación
  }
  prevScrollpos = currentScrollPos;
};
