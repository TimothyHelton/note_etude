// Show instrument drop down box
function showInstruments() {
    document.getElementById("instrDropDown").classList.toggle("show");
}

// Create fields for positions drop down box
// TODO how to call this in HTML
// function createPositions() {
//   var toAdd = document.createDocumentFragment();
//   for(var i=0; i < 8; i++){
//     var newDiv = document.createElement("div");
//     var id = "pickedPos" + i;
//     newDiv.id = id;
//     newDiv.data-picked = "i";
//     newDiv.onclick = "posDetails('" + id + "')";
//     toAdd.appendChild(newDiv);
//   }
//
//   document.appendChild(toAdd);
//}

// Show positions drop down box
function showPositions() {
    document.getElementById("posDropDown").classList.toggle("show");
}

// Rename instrument box and add note buttons
function instrDetails(menuId) {
    var instrPick = document.getElementById(menuId).getAttribute("data-picked");
    window.instrument = instrPick;
    toggleText("instrbtn", instrPick);
}

// Rename position box
function posDetails(menuId) {
    var posPick = document.getElementById(menuId).getAttribute("data-picked");
    window.fingerPosition = posPick;
    toggleText("posbtn", "Position: " + posPick);
    setQuizColor();
}

// Set quiz box color
function setQuizColor() {
    var sel = document.getElementById("quizBox");
    var quizColor;
    switch (window.fingerPosition) {
        case "1":
            quizColor = "yellow";
            break;
        case "2":
            quizColor = "pink";
            break;
        case "3":
            quizColor = "deepskyblue";
            break;
        case "4":
            quizColor = "lightgoldenrodyellow";
            break;
        case "5":
            quizColor = "lightgreen";
            break;
        case "6":
            quizColor = "orange";
            break;
        case "7":
            quizColor = "white";
            break;
    }
    sel.style.background = quizColor;
}

// Toggle text of clickable drop down menu
function toggleText(buttonId, newText) {
    var text = document.getElementById(buttonId).firstChild;
    text.data = newText;
}

// Close drop down menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropDown-content");
        var i;
        for (i =0; i<dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains("show")) {
                openDropdown.classList.remove("show");
            }
        }
    }
};
