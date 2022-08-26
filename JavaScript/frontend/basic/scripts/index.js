document.addEventListener('DOMContentLoaded', () => {
  const reStyle = (index) => {
    console.log('before: ', document.styleSheets);
    noStyles();
    document.styleSheets[index].disabled = false;
    console.log('after: ', document.styleSheets);
  };

  const noStyles = () => {
    console.log('before: ', document.styleSheets);
    document.styleSheets[0].disabled = true;
    document.styleSheets[1].disabled = true;
    document.styleSheets[2].disabled = true;
    document.styleSheets[3].disabled = true;
    console.log('after: ', document.styleSheets);
  };

  window.reStyle = reStyle;
  window.noStyles = noStyles;
});
