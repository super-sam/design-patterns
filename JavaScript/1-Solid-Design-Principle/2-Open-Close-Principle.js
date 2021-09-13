let Color = Object.freeze({
    RED: 'red',
    GREEN: 'green',
    BLUE: 'blue'
});

let Size = Object.freeze({
    SMALL: 'small',
    MEDIUM: 'medium',
    LARGE: 'large'
});

class Product{
    constructor(name, color, size){
        this.name = name
        this.color = color
        this.size = size
    }
}
/*
Adding new filters when the requirement comes violets Open Close Principle (OCP)
This, added new filters(funtions) when requirements comes cause

"State space explosion"
 */
//OCP = Open for extension, Closed for modification

class ProductFilter{
    filterByColor(products, color){
        return products.filter(p => p.color === color);
    }

    filterBySize(products, size){
        return products.filter(p => p.size === size);
    }

    filterBySizeAndColor(products, size, color){
        return products.filter(p => (p.color === color && p.size === size))
    }
    
}

//  Specification Pattern
class ColorSpecification
{
    constructor(color)
    {
        this.color = color;
    }
    isSatisfied(item)
    {
        return this.color === item.color;
    }
}

class SizeSpecification
{
    constructor(size)
    {
        this.size = size;
    }
    isSatisfied(item)
    {
        return this.size === item.size;
    }
}

class NewProductFilter
{
    filter(items, spec){
        return items.filter(p => spec.isSatisfied(p))
    }
}

class AndSpecification
{
    constructor(...specs)
    {
        this.specs = specs
    }

    isSatisfied(item)
    {
        return this.specs.every(x => x.isSatisfied(item))
    }
}

apple = new Product('Apple', Color.GREEN, Size.SMALL);
tree = new Product('Tree', Color.GREEN, Size.LARGE);
house = new Product('House', Color.BLUE, Size.LARGE);

let products = [apple, tree, house];

let pf = new ProductFilter();
console.log('Green Products (old) : ');
for (p of pf.filterByColor(products, Color.GREEN)){
    console.log(` * ${p.name} is green`);
}

console.log('Large Products (old) : ');
for (p of pf.filterBySize(products, Size.LARGE)){
    console.log(` * ${p.name} is large`);
}

console.log('Green Products (new) : ');
let npf = new NewProductFilter()
let greenSpecification = new ColorSpecification(Color.GREEN);
for (p of npf.filter(products, greenSpecification)){
    console.log(` * ${p.name} is green`);
}
console.log('Large Products (new) : ');
let largSpec = new SizeSpecification(Size.LARGE);
for (p of npf.filter(products, largSpec)){
    console.log(` * ${p.name} is large`);
}

console.log('Large and Green Products (new) : ');
let largeAndGreenSpec = new AndSpecification(
    new ColorSpecification(Color.GREEN),
    new SizeSpecification(Size.LARGE)
)
for (p of npf.filter(products, largeAndGreenSpec)){
    console.log(` * ${p.name} is large and green`);
}

