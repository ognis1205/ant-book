document.addEventListener('DOMContentLoaded', () => {
  window.fill1 = (duration) => {
    const bar = document.querySelector('#progress-bar');
    bar.style.transition = `${duration}s linear width`;
    bar.style.width = '100%';
  };

  window.fill2 = (duration) => {
    const bar = document.querySelector('#progress-bar');
    let progress = 0;
    const interval = setInterval(() => {
      progress++;
      bar.style.width = `${progress}%`;
      if (progress >= 100) clearInterval(interval);
    }, (duration * 1000) / 100);
  };

  window.reset = () => {
    const bar = document.querySelector('#progress-bar');
    bar.style.transition = '';
    bar.style.width = '0%';
  };
});
