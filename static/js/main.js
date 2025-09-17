 document.addEventListener('DOMContentLoaded', function () {
      const form = document.getElementById('supportForm');
      const overlay = document.getElementById('spinnerOverlay');
      const submitBtn = document.getElementById('submitBtn');

      // Wenn die Seite geladen ist (auch nach POST), Spinner verstecken
      if (overlay) overlay.style.display = 'none';

      if (form) {
        form.addEventListener('submit', (e) => {
          // Overlay anzeigen
          if (overlay) overlay.style.display = 'flex';
          // Button deaktivieren um Doppel-Submits zu verhindern
          if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerText = 'Wird ausgeführt…';
            // if user cancel make a function stop the spinner
          }
          // Default-Submit passiert (kein e.preventDefault()), Seite lädt neu und Spinner bleibt sichtbar bis Response eintrifft.
        });
      }
    });