

// Initialize component ID counter
let componentId = 1;

// Get references to DOM elements
const addBtn = document.getElementById('addBtn');
const container = document.getElementById('container');

// Add event listener for 'Add New' button
addBtn.addEventListener('click', addComponent);


// Function to add a new component
function addComponent() {
    // Create the component div element
    const componentDiv = document.createElement('div');
    componentDiv.classList.add('component');
    componentDiv.id = 'component-' + componentId;
    
    
    // Create the header element
    const headerDiv = document.createElement('div')
    headerDiv.id = 'header'
    
    
    // Create the edit icon element
    const editIcon = document.createElement('i');
    editIcon.classList.add("bi", "bi-pencil-square");
    editIcon.setAttribute('aria-hidden', 'true');
    editIcon.addEventListener('click', toggleEditable);
    
    // Create the delete icon element
    const deleteIcon = document.createElement('i');
    deleteIcon.classList.add("bi", "bi-trash-fill");
    deleteIcon.setAttribute('aria-hidden', 'true');
    deleteIcon.addEventListener('click', deleteComponent);
    
    // Create the textarea element
    const textarea = document.createElement('textarea');
    textarea.disabled = true;
    
    // Add the edit and delete icons to the component div
    headerDiv.appendChild(deleteIcon);
    headerDiv.appendChild(editIcon);
    componentDiv.appendChild(headerDiv);
    
    // Add the textarea to the component div
    componentDiv.appendChild(textarea);
    
    // Add the component div to the container
    container.appendChild(componentDiv);
    
    // Increment the component ID counter
    componentId++;
}

// Function to toggle the editable state of a component's textarea
function toggleEditable(event) {
    const componentDiv = event.target.parentElement.parentElement;
    const textarea = componentDiv.querySelector('textarea');
    textarea.disabled = !textarea.disabled;
}

// function to change the hearer color


function changethecolor(){
    document.body.style.backgroundColor = 'salmon';

}
//Function to delete a component
function deleteComponent(event) {
    const componentDiv = event.target.parentElement.parentElement;
    container.removeChild(componentDiv);
}