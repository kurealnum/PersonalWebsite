// general file for stuff like scrolling to the top

const button = document.getElementById('topButton');

function scrollTopTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
  }