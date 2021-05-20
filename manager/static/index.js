function deletePassword(passwordId) {
  fetch("/delete-password", {
    method: "POST",
    body: JSON.stringify({ passwordId: passwordId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
