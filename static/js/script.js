document.addEventListener("DOMContentLoaded", function () {
    autoDismiss();

    const form = document.getElementById("registerForm");

    form?.addEventListener("submit", function (e) {
        let valid = true;

        form.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));

        function showError(input, message) {
            const feedback = document.createElement("div");
            feedback.className = "invalid-feedback";
            feedback.innerText = message;
            input.classList.add("is-invalid");
            if (!input.nextElementSibling || !input.nextElementSibling.classList.contains("invalid-feedback")) {
                input.parentNode.appendChild(feedback);
            }
            valid = false;
        }

        const username = form.querySelector("[name='username']");
        if (!username.value.trim()) {
            showError(username, "Username is required.");
        }

        const email = form.querySelector("[name='email']");
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!email.value.trim()) {
            showError(email, "Email is required.");
        } else if (!emailRegex.test(email.value.trim())) {
            showError(email, "Enter a valid email address.");
        }

        const password1 = form.querySelector("[name='password1']");
        if (!password1.value) {
            showError(password1, "Password is required.");
        }

        const password2 = form.querySelector("[name='password2']");
        if (!password2.value) {
            showError(password2, "Confirm your password.");
        } else if (password1.value !== password2.value) {
            showError(password2, "Passwords do not match.");
        }

        if (!valid) {
            e.preventDefault();
        }
    });
});

function autoDismiss() {
    setTimeout(() => {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        });
    }, 3000);
}
