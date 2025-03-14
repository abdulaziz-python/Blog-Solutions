// Theme toggle functionality
document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle-btn');

    // Check if user has already set a preference
    const userPrefersDark = localStorage.getItem('theme') === 'dark' ||
                           (!('theme' in localStorage) &&
                            window.matchMedia('(prefers-color-scheme: dark)').matches);

    // Set initial theme
    if (userPrefersDark) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }

    // Toggle theme
    themeToggleBtn.addEventListener('click', () => {
        const isDark = document.documentElement.classList.toggle('dark');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });

    // Add fade-in effect to page content
    setTimeout(() => {
        document.querySelector('main').style.opacity = "1";
    }, 100);

    // Custom cursor
    const cursor = document.querySelector('.cursor');
    const cursorFollower = document.querySelector('.cursor-follower');

    if (cursor && cursorFollower) {
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';

            setTimeout(() => {
                cursorFollower.style.left = e.clientX + 'px';
                cursorFollower.style.top = e.clientY + 'px';
            }, 100);
        });

        // Hover effect on links and buttons
        const hoverElements = document.querySelectorAll('a, button, .tag, .card');

        hoverElements.forEach(element => {
            element.addEventListener('mouseenter', () => {
                cursor.style.width = '12px';
                cursor.style.height = '12px';
                cursorFollower.style.width = '40px';
                cursorFollower.style.height = '40px';
                cursorFollower.style.opacity = '0.2';
            });

            element.addEventListener('mouseleave', () => {
                cursor.style.width = '8px';
                cursor.style.height = '8px';
                cursorFollower.style.width = '30px';
                cursorFollower.style.height = '30px';
                cursorFollower.style.opacity = '0.4';
            });
        });

        // Hide cursor when mouse leaves window
        document.addEventListener('mouseout', () => {
            cursor.style.opacity = '0';
            cursorFollower.style.opacity = '0';
        });

        document.addEventListener('mouseover', () => {
            cursor.style.opacity = '1';
            cursorFollower.style.opacity = '0.4';
        });
    }

    // Disable custom cursor on mobile
    if (window.innerWidth <= 768) {
        document.body.classList.add('mobile');
    }

    // Magnetic effect for cards
    const magneticElements = document.querySelectorAll('.magnetic-effect');

    magneticElements.forEach(element => {
        element.addEventListener('mousemove', (e) => {
            const rect = element.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const moveX = (x - centerX) / 20;
            const moveY = (y - centerY) / 20;

            element.style.transform = `translate(${moveX}px, ${moveY}px) scale(1.02)`;
        });

        element.addEventListener('mouseleave', () => {
            element.style.transform = '';
        });
    });

    // Add split text animation to headings
    const splitTextElements = document.querySelectorAll('.split-text');

    splitTextElements.forEach(element => {
        element.style.opacity = '0';
        setTimeout(() => {
            element.style.opacity = '1';
            element.classList.add('animate');
        }, 300);
    });
});
