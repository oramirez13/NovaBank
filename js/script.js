// ================================================
// script.js — JavaScript compartido
// Proyecto: NovaBank (Simulación educativa de phishing)
// Curso: CLV-0062 | Universidad Fidélitas
// Autor: orami13
// ================================================


// ------------------------------------------------
// ESPERAR A QUE EL DOCUMENTO ESTÉ LISTO
// $(document).ready() es una función de jQuery que espera a que
// todo el HTML haya sido cargado antes de ejecutar el código.
// Esto evita errores al intentar acceder a elementos que aún no existen.
// ------------------------------------------------
$(document).ready(function () {
  // Todo el código dentro de esta función se ejecuta cuando la página termina de cargar.


  // ------------------------------------------------
  // FUNCIONALIDAD: BOTÓN DE DESCARGA EN INDEX.HTML
  // Esta sección solo afecta a index.html porque busca el elemento
  // con id="download-link", que solo existe en esa página.
  // Si el elemento no existe (ej: en blog.html), el if no se ejecuta.
  // ------------------------------------------------

  if ($("#download-link").length > 0) {
    // $("#download-link") = selector jQuery que busca el elemento con id="download-link"
    // .length > 0 = verifica que el elemento fue encontrado en esta página

    $("#download-link").on("click", function (event) {
      // .on("click", function) = escucha el evento "click" en el elemento seleccionado
      // event = objeto con información sobre el evento

      event.preventDefault();
      // event.preventDefault() = cancela la acción predeterminada del enlace.
      // Sin esto, el navegador intentaría descargar app.py inmediatamente.

      mostrarModalPhishing();
      // Llama a la función que muestra el modal educativo (definida abajo)
    });
    // Fin del escuchador de eventos

  }
  // Fin del if

});
// Fin del $(document).ready()


// ------------------------------------------------
// FUNCIÓN: MOSTRAR MODAL EDUCATIVO DE PHISHING
// Busca el modal que ya existe en el HTML de index.html
// (con id="phishing-modal") y lo muestra usando Bootstrap 5.
//
// IMPORTANTE: El modal NO se genera aquí con JavaScript.
// Vive en el HTML para evitar problemas al parsear HTML dentro de strings JS.
// El JS solo se encarga de mostrarlo y ocultarlo.
// ------------------------------------------------
function mostrarModalPhishing() {
  // function = palabra clave para definir una función reutilizable

  var elementoModal = document.getElementById("phishing-modal");
  // document.getElementById() = método nativo del navegador que busca
  // un elemento HTML por su atributo id.
  // Devuelve el elemento DOM si lo encuentra, o null si no existe.

  if (!elementoModal) {
    // Si el elemento no existe en la página, no hacemos nada
    // ! = operador lógico NOT (negación)
    // !elementoModal es verdadero cuando elementoModal es null
    console.warn("Modal #phishing-modal no encontrado en el HTML.");
    // console.warn() = muestra un mensaje de advertencia en la consola del navegador
    // Útil para depurar sin interrumpir al usuario
    return;
    // return = termina la función inmediatamente
  }

  var modal = new bootstrap.Modal(elementoModal);
  // new bootstrap.Modal(elemento) = crea una instancia del componente Modal de Bootstrap 5.
  // Recibe el elemento DOM real (no un selector jQuery) como argumento.
  // Esta instancia nos da acceso a los métodos .show() y .hide()

  modal.show();
  // .show() = muestra el modal con la animación "fade" definida en Bootstrap.
  // Bootstrap agrega automáticamente el fondo oscuro (backdrop) detrás del modal.

}
// Fin de la función mostrarModalPhishing
