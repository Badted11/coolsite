document.addEventListener("DOMContentLoaded", function() {
    console.log("Страница загружена!");

    let button = document.querySelector("button");
    button.addEventListener("click", function() {
        console.log("Кнопка нажата!");
    });
});
