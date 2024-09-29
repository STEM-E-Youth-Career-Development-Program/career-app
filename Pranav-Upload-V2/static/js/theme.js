document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';

    // Set the theme based on the saved preference
    if (currentTheme === 'dark') {
        document.body.classList.add('dark-mode');
        themeToggle.src = '/static/images/theme_dark.png'; // path to dark theme image
    } else {
        document.body.classList.add('light-mode');
        themeToggle.src = '/static/images/theme_light.png'; // path to light theme image
    }

    // Toggle theme on click
    themeToggle.addEventListener('click', () => {
        if (document.body.classList.contains('light-mode')) {
            document.body.classList.replace('light-mode', 'dark-mode');
            themeToggle.src = '/static/images/theme_dark.png'; // path to dark theme image
            localStorage.setItem('theme', 'dark');
        } else {
            document.body.classList.replace('dark-mode', 'light-mode');
            themeToggle.src = '/static/images/theme_light.png'; // path to light theme image
            localStorage.setItem('theme', 'light');
        }
    });
});
