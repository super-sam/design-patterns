class CEO
{
    get name(){ return CEO._name; }
    set name(value){ CEO._name = value; }

    get age(){ return CEO._age; }
    set age(value){ CEO._age = value; }

    toString()
    {
        return `${this.name} is ${this.age} years old`
    }
}
CEO._age = null;
CEO._name = null;

let ceo = new CEO();
ceo.name = 'Supratim Samantray';
ceo.age = 29

let ceo2 = new CEO();
ceo2.name = 'Sapna Nimkar';
ceo2.age = 28

console.log(ceo.toString())
console.log(ceo2.toString())
