// js/cart.js

// Konstanten
const CART_KEY = 'wandl_cart';

// Warenkorb initialisieren oder abrufen
function getCart() {
    const cart = localStorage.getItem(CART_KEY);
    return cart ? JSON.parse(cart) : [];
}

// Artikel in den Warenkorb legen
function addToCart(productName, quantity, price) {
    const cart = getCart();
    const existingProductIndex = cart.findIndex(item => item.name === productName);
    
    if (existingProductIndex >= 0) {
        cart[existingProductIndex].quantity += parseInt(quantity);
    } else {
        cart.push({
            name: productName,
            quantity: parseInt(quantity),
            price: parseFloat(price)
        });
    }
    
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartUI();
    
    // Visuelles Feedback
    showToast(`${quantity}x ${productName} zum Warenkorb hinzugefügt!`);
}

// Artikel aus dem Warenkorb entfernen
function removeFromCart(productName) {
    let cart = getCart();
    cart = cart.filter(item => item.name !== productName);
    localStorage.setItem(CART_KEY, JSON.stringify(cart));
    updateCartUI();
    
    showToast(`${productName} wurde aus dem Warenkorb entfernt.`);
}

// Warenkorb komplett leeren
function clearCart() {
    localStorage.removeItem(CART_KEY);
    updateCartUI();
}

// UI (Navigation Zähler) updaten
function updateCartUI() {
    const cart = getCart();
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    
    const cartButtons = document.querySelectorAll('.nav-cta');
    cartButtons.forEach(btn => {
        if (btn.textContent.includes('Warenkorb') || btn.textContent.includes('🛒')) {
            btn.innerHTML = `🛒 Warenkorb (${totalItems})`;
            // Change link to checkout if items exist
            if (totalItems > 0) {
                btn.style.backgroundColor = 'var(--color-olive-600)';
                btn.href = 'checkout.html';
            } else {
                btn.style.backgroundColor = 'var(--color-olive-500)';
                btn.href = '#';
            }
        }
    });
}

// Einfaches Toast-System für Feedback
function showToast(message) {
    let toastContainer = document.getElementById('toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'toast-container';
        toastContainer.style.position = 'fixed';
        toastContainer.style.bottom = '20px';
        toastContainer.style.right = '20px';
        toastContainer.style.zIndex = '9999';
        document.body.appendChild(toastContainer);
    }

    const toast = document.createElement('div');
    toast.textContent = message;
    toast.style.backgroundColor = 'var(--color-olive-600)';
    toast.style.color = 'white';
    toast.style.padding = '12px 24px';
    toast.style.borderRadius = '8px';
    toast.style.marginTop = '10px';
    toast.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
    toast.style.fontFamily = 'var(--font-body)';
    toast.style.fontWeight = '500';
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(20px)';
    toast.style.transition = 'all 0.3s ease';

    toastContainer.appendChild(toast);

    // Animieren
    requestAnimationFrame(() => {
        toast.style.opacity = '1';
        toast.style.transform = 'translateY(0)';
    });

    // Entfernen
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(20px)';
        setTimeout(() => {
            toast.remove();
        }, 300);
    }, 3000);
}

// Beim Laden der Seite UI aktualisieren
document.addEventListener('DOMContentLoaded', () => {
    updateCartUI();
});
