function bindShowButton() {
    const showing = document.getElementById('showing-button');
    const input = document.getElementById('search-input');

    if (showing && input) {
        showing.addEventListener('click', () => {
            input.value = '';
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    bindShowButton();
});

document.body.addEventListener('htmx:afterSwap', (e) => {
    if (e.target.id === 'tasks-container') {
        bindShowButton();
    }
});
