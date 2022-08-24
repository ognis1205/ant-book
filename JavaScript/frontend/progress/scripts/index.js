document.addEventListener('DOMContentLoaded', () => {
  const bar = document.querySelector('#progress');

  window.fillByCSS = (duration) => {
    bar.style.transition = `${duration}s linear width`;
    bar.style.width = '100%';
  };

  window.fillByScript = (duration) => {
    let progress = 0;
    const interval = setInterval(() => {
      bar.style.width = `${++progress}%`;
      if (progress >= 100) clearInterval(interval);
    }, (duration * 1000) / 100);
  };

  window.reset = () => {
    bar.style.transition = '';
    bar.style.width = '0%';
  };
});
