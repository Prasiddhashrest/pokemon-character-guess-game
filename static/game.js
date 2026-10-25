// Put the cursor into the guessing box on each round.
// The game rules and score validation remain in Python on the server.
window.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('#guess');
  if (input && window.innerWidth > 800) input.focus({ preventScroll: true });
});
