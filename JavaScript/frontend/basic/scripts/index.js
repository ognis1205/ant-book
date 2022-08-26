document.addEventListener('DOMContentLoaded', () => {
  const menu = Array.from(document.querySelector('#menulist').children);

  const styles = Array.from(document.styleSheets);

  const reStyle = (index) => {
    noStyles();
    menu
      .filter((style, i) => i === index)
      .map((child) => child.classList.add('selected'));
    styles
      .filter((style, i) => i !== 0)
      .filter((style, i) => i === index)
      .map((style) => style.disabled = false);
  };

  const noStyles = () => {
    menu
      .map((child) => child.classList.remove('selected'));
    styles
      .filter((style, i) => i !== 0)
      .map((style) => style.disabled = true);
  };

  window.reStyle = reStyle;
  window.noStyles = noStyles;
  reStyle(0);
});
