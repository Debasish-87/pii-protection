const file = document.querySelector("#file");
const fileName = document.querySelector(".file-name");
const image = document.querySelector(".photo-preview")
const previewBTN = document.querySelector(".preview");
const modal = document.querySelector(".modal");
const closeBTN = document.querySelector(".close");
// const UserBTN = document.querySelector(".btn-user");
// const SecondDiv = document.querySelector(".second-sec");

file.addEventListener("change", () => {
    fileName.innerHTML = file.files[0].name;
    const fileURL = URL.createObjectURL(file.files[0]);
    image.src = fileURL;
    previewBTN.classList.remove("inactive");
});

previewBTN.addEventListener("click", () => {
    modal.classList.toggle("display-none");
});

closeBTN.addEventListener("click", () => {
    modal.classList.toggle("display-none")
})

// UserBTN.addEventListener("click", () => {
//     SecondDiv.classList.toggle("display-none");

// });


