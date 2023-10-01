class Player {
    constructor(username, hp, mp, backPackItems){
        this.username = username;
        this.hp = hp;
        this.mp = mp;
        this.backPackItems = backPackItems;
    }
}

const Ronald = new Player('Ronnie5562', 98, 87, ['Sword', 'M16', 'TAQ-56', 'Granade', 'Fire Blaster']);
console.log(Ronald);

const Tina = new Player();
console.log(Tina);