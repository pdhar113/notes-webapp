function deleteNote(noteID){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteID }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((_res) => {
        window.location.href = "/";
    })
}

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            alert.style.transition = "opacity 0.6s ease, transform 0.6s ease";
            alert.style.opacity = "0";
            alert.style.transform = "translateY(-10px)";
            setTimeout(() => alert.remove(), 600);
        });
    }, 1000);
});