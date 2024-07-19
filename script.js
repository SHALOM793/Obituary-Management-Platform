document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("obituary_form");
  form.addEventListener("submit_obituary", function(event) {
    event.preventDefault();
    const name = document.getElementById("name").value;
    const dateOfBirth = document.getElementById("date_of_birth").value;
    const dateOfDeath = document.getElementById("date_of_death").value;
    const content = document.getElementById("content").value;
    const author = document.getElementById("author").value;

    if (name && dateOfBirth && dateOfDeath && content && author) {
      form.submit();
    } else {
      alert("Please fill in all fields.");
    }
  });
});