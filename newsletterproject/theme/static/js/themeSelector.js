const storedTheme = localStorage.getItem('selectedTheme');
const themeSelector = document.getElementById('themeSelector');


if (storedTheme) {
  document.documentElement.setAttribute('data-theme', storedTheme);
  document.getElementById('themeSelector').checked = storedTheme !== 'lemonade';
}

themeSelector.addEventListener('change', handleThemeChange);

function handleThemeChange() {
  const selectedTheme = themeSelector.checked ? themeSelector.value : 'lemonade';
  document.documentElement.setAttribute('data-theme', selectedTheme);
  localStorage.setItem('selectedTheme', selectedTheme);
}