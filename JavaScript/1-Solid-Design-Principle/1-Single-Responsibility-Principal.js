// SRP SOC
// If we have a class if should have a primary responsibility
// It shouldn't take other responsibilities
const fs = require('fs');
class Journal
{
    constructor(){
        this.entries = {};
    }

    addEntry(text) {
        let c = ++Journal.count;
        let entry = `${c}: ${text}`
        this.entries[c] = entry;
        return c;
    }

    removeEntry(pos){
        return delete this.entries[pos];
    }

    toString(){
        return Object.values(this.entries).join('\n');
    }
    
    // Below methods are secondary responsibilities which
    // shouldn't be responsibility of Journal
    save(filename){

    }
    load(filename){

    }
    loadFromWeb(uri){

    }
}
Journal.count = 0;

// Instead we will have separate helper to help us with the same
class PersistanceManager{
    saveToFile(text, filename){
        fs.writeFileSync(filename, text);

    }
    loadFromFile(text, filename){

    }
}

j = new Journal();
j.addEntry("I smiled today");
j.addEntry('I ate an ice-cream today');
console.log(`Journal entries: \n${j.toString()}`);
file = './journal.txt';
persistanceManager = new PersistanceManager();
persistanceManager.saveToFile(j.toString(), file);