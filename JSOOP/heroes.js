const populate = async () => {
    const requestUrl = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json";

    const request = new Request(requestUrl); 

    const response = await fetch(request);
    const superHeroes = await response.json();

    console.log(superHeroes);
}

populate();