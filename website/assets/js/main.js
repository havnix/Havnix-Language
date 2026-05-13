/**
 * Havnix Website - Main JavaScript
 */

// ─── Navbar scroll effect ───
window.addEventListener('scroll', () => {
    const nav = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        nav.style.background = 'rgba(0, 0, 0, 0.95)';
    } else {
        nav.style.background = 'rgba(0, 0, 0, 0.85)';
    }
});

// ─── Smooth scroll for anchor links ───
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ─── Package search ───
const searchInput = document.getElementById('search-packages');
const filterSelect = document.getElementById('filter-category');

if (searchInput) {
    searchInput.addEventListener('input', filterPackages);
}
if (filterSelect) {
    filterSelect.addEventListener('change', filterPackages);
}

function filterPackages() {
    const query = (searchInput?.value || '').toLowerCase();
    const cards = document.querySelectorAll('.package-card');

    cards.forEach(card => {
        const name = card.querySelector('.package-name')?.textContent.toLowerCase() || '';
        const desc = card.querySelector('.package-desc')?.textContent.toLowerCase() || '';
        const matches = name.includes(query) || desc.includes(query);
        card.style.display = matches ? '' : 'none';
    });
}

// ─── Upload form ───
const uploadForm = document.getElementById('upload-form');
if (uploadForm) {
    uploadForm.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(this);
        const name = formData.get('name');
        const desc = formData.get('description');

        // Show success message (in production, send to PHP backend)
        const uploadArea = document.getElementById('upload-area');
        if (uploadArea) {
            const msg = document.createElement('div');
            msg.style.cssText = 'padding: 20px; background: rgba(16,185,129,0.15); border: 1px solid var(--success); border-radius: 10px; margin-top: 20px; text-align: center;';
            msg.innerHTML = `<p style="color: var(--success); font-weight: bold;">تم رفع "${name}" بنجاح!</p><p style="color: var(--text-muted); font-size: 14px; margin-top: 8px;">سيتم مراجعة المكتبة والموافقة عليها قريباً.</p>`;
            uploadArea.appendChild(msg);
            this.reset();

            setTimeout(() => msg.remove(), 5000);
        }
    });
}

// ─── OS Detection for download page ───
function detectOS() {
    const ua = navigator.userAgent.toLowerCase();
    if (ua.includes('win')) return 'windows';
    if (ua.includes('mac')) return 'macos';
    if (ua.includes('linux')) return 'linux';
    return 'unknown';
}

// Highlight recommended OS card
document.addEventListener('DOMContentLoaded', () => {
    const os = detectOS();
    const cards = document.querySelectorAll('.download-card');
    const osMap = { windows: 0, linux: 1, macos: 2 };

    if (cards.length && osMap[os] !== undefined) {
        const card = cards[osMap[os]];
        card.style.borderColor = 'var(--accent)';
        card.style.boxShadow = '0 0 20px rgba(96, 165, 250, 0.2)';

        const badge = document.createElement('div');
        badge.textContent = '⭐ موصى به لنظامك';
        badge.style.cssText = 'background: var(--accent); color: var(--bg-dark); padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: 600; margin-bottom: 12px; display: inline-block;';
        card.insertBefore(badge, card.firstChild);
    }

    // Close mobile nav on link click
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            document.querySelector('.nav-links')?.classList.remove('open');
        });
    });
});

// ─── Code copy button ───
document.querySelectorAll('.code-block').forEach(block => {
    block.style.position = 'relative';
    block.style.cursor = 'pointer';
    block.title = 'اضغط للنسخ';

    block.addEventListener('click', () => {
        const code = block.querySelector('pre')?.textContent || '';
        navigator.clipboard.writeText(code).then(() => {
            const toast = document.createElement('div');
            toast.textContent = 'تم النسخ!';
            toast.style.cssText = 'position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); background: var(--success); color: white; padding: 8px 20px; border-radius: 8px; font-size: 14px; z-index: 9999; animation: fadeIn 0.2s;';
            document.body.appendChild(toast);
            setTimeout(() => toast.remove(), 1500);
        });
    });
});
