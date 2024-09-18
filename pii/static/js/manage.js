const UserBTN = document.querySelector(".button-56");
const SecondDiv = document.querySelector(".user-ids");


UserBTN.addEventListener("click", () => {
    SecondDiv.classList.toggle("display-none");

});

const opendbtn = document.querySelector(".button-52");
const Details = document.querySelector(".addhar-detail");
const closedbtn = document.querySelector(".close-2");

opendbtn.addEventListener("click", () => {
    Details.classList.toggle("display-none");
});

closedbtn.addEventListener("click", () => {
    Details.classList.toggle("display-none");
});