// navigation.js - Responsive navigation component for all devices

document.addEventListener('DOMContentLoaded', function () {
    // Create the navigation container with padding to prevent content overlap
    const navContainer = document.createElement('div');
    navContainer.className = 'nav-container fixed top-0 left-0 w-full z-50';

    // Create the navigation element
    const nav = document.createElement('nav');
    nav.className = 'bg-white shadow-lg';

    // Create the navigation content with mobile menu button
    nav.innerHTML = `
        <div class="max-w-7xl mx-auto px-4">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <span class="text-xl font-bold text-indigo-600">Options Analyzer</span>
                    <button id="mobile-menu-button" class="md:hidden ml-4 text-gray-500 hover:text-indigo-600 focus:outline-none">
                        <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                    </button>
                </div>
                <div id="nav-links" class="hidden md:flex items-center space-x-1">
                    <a href="/" class="nav-link" data-path="/">
                        <span>Strikes Analysis</span>
                    </a>
                    <a href="/nifty" class="nav-link" data-path="/nifty">
                        <span>Nifty Analysis</span>
                    </a>
                    <a href="/banknifty" class="nav-link" data-path="/banknifty">
                        <span>BankNifty Analysis</span>
                    </a>
                    <a href="/signals" class="nav-link" data-path="/signals">
                        <span>Signals</span>
                    </a>
                    </a>
                    <a href="/disclaimer" class="nav-link" data-path="/disclaimer">
                        <span>Disclaimer</span>
                    </a>
                    </a>
                    <a href="/ContactUs" class="nav-link" data-path="/ContactUs">
                        <span>ContactUs</span>
                    </a>
                </div>
            </div>
            <!-- Mobile menu (hidden by default) -->
            <div id="mobile-menu" class="md:hidden hidden">
                <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-gray-50">
                    <a href="/" class="nav-link block px-3 py-2 rounded-md" data-path="/">
                        <span>Strikes Analysis</span>
                    </a>
                    <a href="/nifty" class="nav-link block px-3 py-2 rounded-md" data-path="/nifty">
                        <span>Nifty Analysis</span>
                    </a>
                    <a href="/banknifty" class="nav-link block px-3 py-2 rounded-md" data-path="/banknifty">
                        <span>BankNifty Analysis</span>
                    </a>
                    <a href="/signals" class="nav-link block px-3 py-2 rounded-md" data-path="/signals">
                        <span>Signals</span>
                    </a>
                    <a href="/disclaimer" class="nav-link block px-3 py-2 rounded-md" data-path="/disclaimer">
                        <span>Disclaimer</span>
                    </a>
                    <a href="/ContactUs" class="nav-link block px-3 py-2 rounded-md" data-path="/ContactUs">
                        <span>ContactUs</span>
                    </a>
                </div>
            </div>
        </div>
    `;

    navContainer.appendChild(nav);

    // Insert the navigation at the top of the body
    document.body.insertBefore(navContainer, document.body.firstChild);

    // Add padding to body to prevent content overlap
    document.body.style.paddingTop = '4rem';

    // Add styles dynamically
    const style = document.createElement('style');
    style.textContent = `
        /* Base styles */
        .nav-container {
            transition: all 0.3s ease;
        }
        
        .nav-link {
            position: relative;
            padding: 0.5rem 1rem;
            color: #4b5563;
            font-weight: 500;
            text-decoration: none;
            transition: all 0.3s ease;
            border-radius: 0.375rem;
            overflow: hidden;
        }
        
        .nav-link span {
            position: relative;
            z-index: 1;
        }
        
        /* Desktop hover effect */
        .nav-link:before {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: #6366f1;
            transform: scaleX(0);
            transform-origin: right;
            transition: transform 0.3s ease;
        }
        
        .nav-link:hover {
            color: #6366f1;
        }
        
        .nav-link:hover:before {
            transform: scaleX(1);
            transform-origin: left;
        }
        
        .nav-link.active {
            color: #6366f1;
        }
        
        .nav-link.active:before {
            transform: scaleX(1);
        }
        
        /* Animation for active link */
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(99, 102, 241, 0); }
            100% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0); }
        }
        
        .nav-link.active {
            animation: pulse 1.5s infinite;
        }
        
        /* Mobile menu styles */
        @media (max-width: 767px) {
            #nav-links {
                display: none;
            }
            
            #mobile-menu {
                display: none;
                transition: all 0.3s ease;
            }
            
            #mobile-menu.show {
                display: block;
                animation: slideDown 0.3s ease-out;
            }
            
            @keyframes slideDown {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            .nav-link {
                display: block;
                padding: 0.75rem 1rem;
                margin: 0.25rem 0;
            }
            
            .nav-link:before {
                height: 100%;
                width: 3px;
                top: 0;
                left: 0;
                transform: scaleY(0);
                transform-origin: bottom;
            }
            
            .nav-link:hover:before,
            .nav-link.active:before {
                transform: scaleY(1);
                transform-origin: top;
            }
        }
        
        /* Ripple effect styles */
        .ripple {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 5px;
            height: 5px;
            background: rgba(99, 102, 241, 0.3);
            opacity: 1;
            border-radius: 50%;
            transform: scale(1, 1) translate(-50%, -50%);
            transform-origin: 50% 50%;
            animation: ripple 0.6s ease-out;
        }
        
        @keyframes ripple {
            0% {
                transform: scale(0, 0) translate(-50%, -50%);
                opacity: 1;
            }
            100% {
                transform: scale(20, 20) translate(-50%, -50%);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);

    // Mobile menu toggle functionality
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
            mobileMenu.classList.toggle('show');
        });
    }

    // Set active link based on current path
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        if (link.getAttribute('data-path') === currentPath) {
            link.classList.add('active');
        }

        // Add click effect
        link.addEventListener('click', function (e) {
            // Remove active class from all links
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));

            // Add active class to clicked link
            this.classList.add('active');

            // Add ripple effect
            const ripple = document.createElement('span');
            ripple.className = 'ripple';
            this.appendChild(ripple);

            setTimeout(() => {
                ripple.remove();
            }, 1000);

            // Close mobile menu if open
            if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('hidden');
                mobileMenu.classList.remove('show');
            }
        });
    });

    // Add scroll effect to navigation (only for desktop)
    let lastScroll = 0;
    window.addEventListener('scroll', function () {
        if (window.innerWidth > 767) { // Only for desktop
            const currentScroll = window.pageYOffset;

            if (currentScroll <= 0) {
                navContainer.style.transform = 'translateY(0)';
                return;
            }

            if (currentScroll > lastScroll) {
                // Scrolling down
                navContainer.style.transform = 'translateY(-100%)';
            } else {
                // Scrolling up
                navContainer.style.transform = 'translateY(0)';
            }

            lastScroll = currentScroll;
        }
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function (e) {
        if (!nav.contains(e.target) && !mobileMenuButton.contains(e.target)) {
            if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('hidden');
                mobileMenu.classList.remove('show');
            }
        }
    });
});