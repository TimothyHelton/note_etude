// Get user instrument selection then create positions and notes menus
function instrDetails() {
  var sel = document.getElementById("instrDropDown");
  sel.classList.toggle("show");

}

// Close drop down menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropDown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};

// Toggle text of clickable drop down menu
function toggleText(buttonId, menuId) {
  var sel = document.getElementById(menuId);
  var text = document.getElementById(buttonId).firstChild;
  text.data = sel.getAttribute("data-picked");
}
