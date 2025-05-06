document.addEventListener("DOMContentLoaded", async () => {
    const token = localStorage.getItem("access_token");

    // If no token at all, redirect to login
    if (!token) {
        redirectToLogin();
        return;
    }

    try {
        const res = await fetch("/api/v1/auth/me", {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        if (res.status !== 200) {
            throw new Error("Invalid or expired token");
        }

        const user = await res.json();
        console.log("Authenticated as:", user.username); // Optional: Use user info if needed
    } catch (err) {
        console.warn("Auth check failed:", err.message);
        localStorage.removeItem("access_token");
        redirectToLogin();
    }
});

function redirectToLogin() {
    window.location.href = "/login";
}
