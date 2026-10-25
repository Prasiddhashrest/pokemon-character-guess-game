// Front-end enhancement. Python/Flask still handles scores, clues and guesses.
window.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('#guess');
  if (input && window.innerWidth > 800) input.focus({ preventScroll: true });

  // Image hosts sometimes fail or visitors may play offline; keep the UI usable.
  document.querySelectorAll('.artwork-stage img').forEach((img) => {
    const showFallback = () => img.closest('.artwork-stage')?.classList.add('image-missing');
    img.addEventListener('error', showFallback);
    if (img.complete && img.naturalWidth === 0) showFallback();
  });
});
