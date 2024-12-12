// Toggle navigation menu on mobile
document.getElementById("toggle-nav").addEventListener("click", function () {
  const navbar = document.getElementById("navbar");
  navbar.classList.toggle("active");
});

// Add your other interactivity code here

// Function to scroll to the top of the page
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}
