const quizData = [
{
    question: "Which language runs in a web browser?",
    a: "Java",
    b: "C",
    c: "Python",
    d: "Javascript",
    correct: "d"
},

{
    question: "De quel référentiel faites-vous partie?",
    a: "Dev Data",
    b: "Dev Web",
    c: "Ref Dig",
    d: "Hckz",
    correct: "a"
},

{
    question: "What does the symbol ':-/' mean?",
    a: "Confused",
    b: "Skeptical",
    c: "Sad",
    d: "Angry",
    correct: "b"
},

{
    question: "What is the opposite of 'oui' in French?",
    a: "Ouin",
    b: "Noun",
    c: "Neuwon",
    d: "Non",
    correct: "d"
}
];

const quiz = document.getElementById('quiz');
const answerEls = document.querySelectorAll('.answer');
const questionEl = document.getElementById('question');
const a_text = document.getElementById('a_text');
const b_text = document.getElementById('b_text');
const c_text = document.getElementById('c_text');
const d_text = document.getElementById('d_text');
const submitBtn = document.getElementById('submit');

let currentQuiz = 0;
let score = 0;

loadQuiz();

function loadQuiz() {
deselectAnswers();

const currentQuizData = quizData[currentQuiz];

questionEl.innerText = currentQuizData.question;
a_text.innerText = currentQuizData.a;
b_text.innerText = currentQuizData.b;
c_text.innerText = currentQuizData.c;
d_text.innerText = currentQuizData.d;
}

function deselectAnswers() {
answerEls.forEach(answerEl => answerEl.checked = false);
}

function getSelected() {
let answer = undefined;

answerEls.forEach(answerEl => {
    if(answerEl.checked) {
    answer = answerEl.id;
    answerEls.forEach(otherEl => {
        if (otherEl !== answerEl) {
            answerEl.checked = false;
        };
    });
}});






return answer;
}

submitBtn.addEventListener('click', () => {
const answer = getSelected();

// console.log(answer === quizData[currentQuiz].correct)



if(answer) {
    if(answer ===  quizData[currentQuiz].correct) {
    score++;
    }

    currentQuiz++;

    if(currentQuiz < quizData.length) {
    loadQuiz();
    } 
    else if (currentQuiz === quizData.length) {
        quiz.innerHTML = `
            <h2>You answered ${score}/${quizData.length} questions correctly</h2>
            <button onclick="location.reload()">Reload</button>
            `;
//             //  block of code to be executed if the condition1 is false and condition2 is true    
}
}
});

