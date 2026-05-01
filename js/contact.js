const form = document.getElementById('contact-form');
const submitButton = document.getElementById('submit-button');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    submitButton.disabled = true;
    submitButton.innerText = 'Sending...';
    errorMessage.classList.add('hidden');

    const formData = new FormData(form);

    try {
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        });

        if (response.ok) {
            window.location.href = 'thank-you.html';
        } else {
            throw new Error('Form submission failed');
        }
    } catch (error) {
        errorMessage.classList.remove('hidden');
        submitButton.disabled = false;
        submitButton.innerText = 'Send Message';
    }
});
