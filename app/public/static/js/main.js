function onSendRequest() {

  const name = document.getElementById("name").value;
  const apiUrl = document.getElementById("apiUrl").value;

  if(name && apiUrl) {
    (async () => {
      const request = await fetch(url = apiUrl, {
        method: "POST",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({name})
      })
      if(request.status === 200) {
        const response = await request.json();
        alert("Nome salvo com sucesso!")
      }else {
        alert("Ocorreu um erro!")
      }
    })();
  }else {
    alert("Nome nao pode ficar em branco!")
  }
};


function onSendLogin() {
  const user = document.getElementById("user").value;
  const password = document.getElementById("password").value;
  
}

function onRandomPeople() {
  const people = JSON.parse(document.getElementById("people").value);
  const random = Math.floor(Math.random() * people.length);
  const person = people[random];
  if(person) {
    const personNameElement = document.getElementById("person-name");
    personNameElement.innerHTML = person.name;
  }
  console.log(random, person);
}