function fullname(){
    return this.firstName + ' ' + this.lastName;
}

const person = {
    firstName: 'Pradeep',
    lastName: 'Kumar'
}
// Prints 'Pradeep Kumar'
console.log(fullname.apply(person));

function fullname_withArgs(city, country) {
    return this.firstName + ' ' + this.lastName + ' is from ' + city + ', ' + country;
}

const person1 = {
    firstName: 'Tippa',
    lastName: 'Kumar'
};


// the .apply() method takes arguments as array
console.log(fullname_withArgs.apply(person1, ['Hyderabad', 'India']));
// Prints 'Tippa Kumar is from Hyderabad, India'

// TODO: .apply with undefined. .apply(undefined, obj)