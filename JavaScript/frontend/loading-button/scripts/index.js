document.addEventListener('DOMContentLoaded', () => {
  const button = document.querySelector('#search-button');
  const buttonContent = document.querySelector('#search-button div');

  button.addEventListener('click', () => {
    buttonContent.classList.toggle('loading');
  });
});
