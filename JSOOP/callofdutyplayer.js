class Player {
    constructor(username, hp, mp, backpackItems) {
        this.username = username;
        this.hp = hp;
        this.mp = mp;
        this.backpackItems = backpackItems;
    }

    attack(targetPlayer) {
        // Aution your 500 👊👊. Make you Eblaze en mouth.
        console.log(`${this.username} attacked ${targetPlayer.username} with ${this.hp} hp`);
    }

    heal(healthPoints) {
        console.log(`${this.username} is healing for ${healthPoints} hp...`);
        setTimeout(() => {
            this.hp += healthPoints;
            console.log(`${this.username} healed for ${healthPoints} hp. Current HP: ${this.hp}`);
        }, 2000); // Simulating a 2-second delay for healing
    }

    useMP(manaPoints) {
        if (this.mp >= manaPoints) {
            this.mp -= manaPoints;
            console.log(`${this.username} used ${manaPoints} MP. Current MP: ${this.mp}`);
        } else {
            console.log(`${this.username} does not have enough MP to perform this action.`);
        }
    }

    displayInfo() {
        console.log(`
            Username: ${this.username}
            HP: ${this.hp}
            MP: ${this.mp}
            Backpack Items: ${this.backpackItems.join(', ')}
        `);
    }
}

const Ronald = new Player('Ronnie5562', 98, 87, ['Laptop']);
const Tina = new Player('Tina', 95, 90, ['Health Potion', 'Magic Scroll']);
const StarBoy = new Player('StarBoy', 90, 56, ['Sword', 'M16', 'TAQ-56', 'Grenade', 'Fire Blaster']);

Ronald.attack(Tina);
Tina.heal(20); // Healing Tina for 20 HP
StarBoy.useMP(30); // StarBoy using 30 MP

Ronald.displayInfo();
Tina.displayInfo();
StarBoy.displayInfo();
