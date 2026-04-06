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
  // ------------------------------------------------

  // Verificar si el botón de descarga existe en la página actual
  if ($("#download-link").length > 0) {
    // $("#download-link") = selector jQuery que busca el elemento con id="download-link"
    // .length > 0 = verifica que el elemento fue encontrado (length es cuántos elementos coinciden)
    // Si length es 0, el elemento no existe en esta página y no ejecutamos el código

    // Agregar un escuchador de eventos al botón de descarga
    $("#download-link").on("click", function (event) {
      // .on("click", function) = escucha el evento "click" en el elemento seleccionado
      // event = objeto que contiene información sobre el evento ocurrido

      event.preventDefault();
      // event.preventDefault() = cancela la acción predeterminada del navegador.
      // En un enlace <a>, la acción predeterminada sería navegar a la URL o descargar el archivo.
      // Al cancelarla, podemos controlar exactamente qué sucede cuando se hace clic.

      // Mostrar el modal educativo de phishing
      // En lugar de un simple confirm(), usamos el modal de Bootstrap para mejor experiencia
      mostrarModalPhishing();
      // Llamada a la función definida más abajo en este archivo
    });
    // Fin del escuchador de eventos

  }
  // Fin del if de verificación

});
// Fin del $(document).ready()


// ------------------------------------------------
// FUNCIÓN: MOSTRAR MODAL EDUCATIVO DE PHISHING
// Esta función crea y muestra un modal de Bootstrap con la
// explicación educativa cuando el usuario hace clic en el botón de descarga.
// Un modal es una ventana emergente que se superpone a la página.
// ------------------------------------------------
function mostrarModalPhishing() {
  // function = palabra clave para definir una función
  // mostrarModalPhishing = nombre de la función (sin parámetros en este caso)

  // Verificar si ya existe un modal previo y eliminarlo para evitar duplicados
  if ($("#phishing-modal").length > 0) {
    // Si ya existe un modal con este id, lo eliminamos antes de crear uno nuevo
    $("#phishing-modal").remove();
    // .remove() = elimina el elemento del DOM (Document Object Model = estructura del HTML)
  }

  // Construir el HTML del modal usando una cadena de texto (template string)
  var modalHTML = `
    <div class="modal fade" id="phishing-modal" tabindex="-1" aria-labelledby="phishing-modal-label" aria-hidden="true">
      <!--
        modal = clase Bootstrap que define este div como un modal
        fade = animación de aparecer/desaparecer gradualmente
        id="phishing-modal" = identificador único del modal
        tabindex="-1" = excluye el elemento del orden de tabulación normal
        aria-labelledby = referencia al elemento que sirve como título (accesibilidad)
        aria-hidden = indica a lectores de pantalla que este elemento está oculto al inicio
      -->

      <div class="modal-dialog modal-dialog-centered">
        <!--
          modal-dialog = contenedor interno del modal Bootstrap
          modal-dialog-centered = centra el modal verticalmente en la pantalla
        -->

        <div class="modal-content">
          <!-- modal-content = el contenido visual del modal (la "caja") -->

          <!-- Encabezado del modal -->
          <div class="modal-header bg-warning">
            <!--
              modal-header = sección superior del modal Bootstrap
              bg-warning = fondo amarillo de Bootstrap
            -->

            <h5 class="modal-title fw-bold" id="phishing-modal-label">
              <!-- modal-title = clase Bootstrap para el título del modal -->
              ⚠️ You just experienced a Phishing Attempt!
            </h5>

            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
            </button>
            <!--
              btn-close = botón X de cierre de Bootstrap
              data-bs-dismiss="modal" = atributo de Bootstrap que cierra el modal al hacer clic
              aria-label="Close" = etiqueta para accesibilidad (lectores de pantalla)
            -->

          </div>
          <!-- Fin del modal-header -->

          <!-- Cuerpo del modal: la explicación educativa -->
          <div class="modal-body">
            <!-- modal-body = sección principal de contenido del modal -->

            <p class="mb-2">
              <strong>This was a simulated phishing page.</strong>
              The "NovaBank Security Tool" you were about to download does not exist.
            </p>

            <p class="mb-2">In a real attack, that file could have been:</p>

            <ul class="mb-3">
              <!-- ul = lista no ordenada en HTML -->
              <li>A <strong>keylogger</strong> — records everything you type</li>
              <li>A <strong>trojan</strong> — gives attackers remote access to your system</li>
              <li>A <strong>ransomware installer</strong> — encrypts your files for ransom</li>
            </ul>

            <div class="alert alert-info mb-0" role="alert">
              <!-- alert-info = alerta azul de Bootstrap (informativa) -->
              <!-- mb-0 = sin margin-bottom (es el último elemento) -->
              💡 <strong>Want to learn more?</strong>
              Visit our
              <a href="blog.html" class="alert-link">Awareness Page</a>
              to understand how phishing works and how to protect yourself.
              <!-- alert-link = clase Bootstrap para enlaces dentro de alertas -->
            </div>

          </div>
          <!-- Fin del modal-body -->

          <!-- Pie del modal: botones de acción -->
          <div class="modal-footer">
            <!-- modal-footer = sección inferior del modal Bootstrap -->

            <a href="blog.html" class="btn btn-primary">
              <!-- btn-primary = botón azul de Bootstrap -->
              📖 Learn More
            </a>

            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
              <!-- btn-secondary = botón gris de Bootstrap -->
              <!-- data-bs-dismiss="modal" = cierra el modal al hacer clic -->
              Close
            </button>

          </div>
          <!-- Fin del modal-footer -->

        </div>
        <!-- Fin del modal-content -->

      </div>
      <!-- Fin del modal-dialog -->

    </div>
  `;
  // Fin de la cadena de texto con el HTML del modal

  // Insertar el modal en el body del documento
  $("body").append(modalHTML);
  // $("body") = selecciona el elemento <body> con jQuery
  // .append() = agrega el HTML al final del body (sin reemplazar el contenido existente)

  // Crear la instancia del modal de Bootstrap y mostrarlo
  var modal = new bootstrap.Modal(document.getElementById("phishing-modal"));
  // new bootstrap.Modal() = crea una instancia del componente Modal de Bootstrap 5
  // document.getElementById("phishing-modal") = obtiene el elemento del DOM por su id
  // Bootstrap necesita la referencia al elemento DOM real, no al selector jQuery

  modal.show();
  // .show() = muestra el modal con la animación de fade definida en Bootstrap

}
// Fin de la función mostrarModalPhishing