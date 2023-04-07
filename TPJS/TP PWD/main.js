// DOM ELEMENTS
const resultEL = document.getElementById('result');
const lengthEL = document.getElementById('length');
const uppercaseEL = document.getElementById('uppercase');
const lowercaseEL = document.getElementById('lowercase');
const numbersEL = document.getElementById('numbers');
const symbolsEL = document.getElementById('symbols');
const generateEL = document.getElementById('generate');
const clipboardEL = document.getElementById('clipboard');

generateEL.addEventListener('click', () => {
    const length = lengthEL.value;
    const characterTypes = {
        lowercase: lowercaseEL.checked,
        uppercase: uppercaseEL.checked,
        numbers: numbersEL.checked,
        symbols: symbolsEL.checked
    };
    const password = generatePassword(length, characterTypes);
    resultEL.innerText = password;
});

function generatePassword(length, characterTypes) {
    const characterSets = {
        lowercase: 'abcdefghijklmnopqrstuvwxyz',
        uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        numbers: '0123456789',
        symbols: '!@#$%^&*(){}[]=<>/,.'
    };
    const selectedCharacterSets = Object.entries(characterTypes)
        .filter(([key, value]) => value)
        .map(([key, value]) => characterSets[key])
        .join('');
    const selectedCharacterSetArray = Array.from(selectedCharacterSets);
    const passwordArray = Array.from({ length }, () => {
        const randomIndex = crypto.getRandomValues(new Uint32Array(1))[0] % selectedCharacterSetArray.length;
        return selectedCharacterSetArray[randomIndex];
    });
    return passwordArray.join('');
}