const d = document;
const cicleGif = "../assets/Y-icon-cicle.gif";
const staticGif = "../assets/Y-icon-static.png";

d.addEventListener("click", (e) => {
    if (e.target.matches(".div-tablero div")) {
        e.target.innerHTML = `<img src="${cicleGif}">`;

        setTimeout(() => {
            e.target.innerHTML = `<img src="${staticGif}">`;
        }, 450);
    }
});