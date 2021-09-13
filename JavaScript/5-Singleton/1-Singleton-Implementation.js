class Singleton
{
    constructor()
    {
        const instance = this.constructor.instance;
        if (instance)
        {
            return instance
        }

        this.constructor.instance = this
    }
}

let s1 = new Singleton()
let s2 = new Singleton()

console.log(`Are item identical? ${s1 === s2}`)