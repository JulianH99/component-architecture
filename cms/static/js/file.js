window.addEventListener("DOMContentLoaded", (event) => {
    const fileInput = document.querySelector("#banner-background");
    fileInput.onchange = () => {
        if (fileInput.files.length > 0) {
            const fileName = document.querySelector(
                "#banner-background-file-name"
            );
            fileName.textContent = fileInput.files[0].name;
        }
    };
});
