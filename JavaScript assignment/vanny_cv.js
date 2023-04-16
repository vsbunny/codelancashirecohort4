//Adding events to the LHS of the document

//Styling the Progress Bars headings 
//For all for loops i,j,k are dummy variables

let celements = document.querySelectorAll(".centered-2"); // creating a nodelist of the elements with CSS class .centered-2

let hoverEventt = () => {
   var alpha = document.querySelectorAll('.centered-2');
   for (var k=0; k<alpha.length; k++) {
      alpha[k].style.color="rgb(223, 32, 191)";          // change color to pink when hovering
      alpha[k].style.fontWeight ="bold";
   }
}
celements.forEach((item) => {
   item.addEventListener('mouseover',hoverEventt)         //event on Mouseover for each item
});

//***********************************************************************//
let elements = document.querySelectorAll('.centered');   // creating a nodelist of the elements with CSS class .centered

let hoverEvent = () => {                                 // creating the 'event' to be passed on each item in the node
    var x = document.querySelectorAll('.centered');
    for (var i=0; i<x.length; i++) {                     // for loop that goes through all elements with class .centered
      x[i].style.color="rgb(177, 6, 148)";
    }
}
elements.forEach((item) => {
    item.addEventListener('mouseover', hoverEvent)       // for each element, this event will happen on Mouseover
});

let elements2 = document.querySelectorAll('.centered');  // creating another nodelist of the elements with CSS class .centered

let nohoverEvent = () => {                               // creating the 'event' to be passed on each item in the node
   var y = document.querySelectorAll('.centered');
   for (var j=0; j<y.length; j++) {                      // for loop that goes through all elements with class .centered
      y[j].style.color="black";                          // for each element, this event will happen on Mouseout
   }
}
elements2.forEach((item) => {
   item.addEventListener('mouseout',nohoverEvent)
});
//***********************************************************************//
//C ++ bar interactivity 
function movebar1() {
   var elem = document.getElementById("c-bar");   
   var width = 0;
   var id = setInterval(frame, 20);            //var for how fast the bar grows
   function frame() {
     if (width >= 75) {                        // going up to the desired percentage
       clearInterval(id);
     } else {
       width++; 
       elem.style.width = width + '%'; 
       elem.style.backgroundColor = "rgb(223, 32, 191)";
       elem.innerHTML = width * 1  + '%';      // % written in the bar
       elem.style.color = "white";
       elem.style.padding = "2px";
     }
   }
 }
//Python bar interactivity
function movebar2() {
   var elem2 = document.getElementById("python-bar");   
   var width2 = 0;
   var id2 = setInterval(frame2, 20);            //var for how fast the bar grows
   function frame2() {
     if (width2 >= 80) {                         // going up to the desired percentage
       clearInterval(id2);
     } else {
       width2++; 
       elem2.style.width = width2 + '%'; 
       elem2.style.backgroundColor = "rgb(223, 32, 191)";
       elem2.innerHTML = width2 * 1  + '%';      // % written in the bar
       elem2.style.color = "white";
       elem2.style.padding = "2px";
     }
   }
 }
//MATLAB bar interactivity
function movebar3() {
   var elem3 = document.getElementById("matlab-bar");   
   var width3 = 0;
   var id3 = setInterval(frame3, 20);            //var for how fast the bar grows
   function frame3() {
     if (width3 >= 60) {                         // going up to the desired percentage
       clearInterval(id3);
     } else {
       width3++; 
       elem3.style.width = width3 + '%'; 
       elem3.style.backgroundColor = "rgb(223, 32, 191)";
       elem3.innerHTML = width3 * 1  + '%';      // % written in the bar
       elem3.style.color = "white";
       elem3.style.padding = "2px";
     }
   }
 }
//HTML bar interactivity
function movebar4() {
   var elem4 = document.getElementById("html-bar");   
   var width4 = 0;
   var id4 = setInterval(frame4, 20);            //var for how fast the bar grows
   function frame4() {
     if (width4 >= 75) {                         // going up to the desired percentage
       clearInterval(id4);
     } else {
       width4++; 
       elem4.style.width = width4 + '%'; 
       elem4.style.backgroundColor = "rgb(223, 32, 191)";
       elem4.innerHTML = width4 * 1  + '%';       // % written in the bar
       elem4.style.color = "white";
       elem4.style.padding = "2px";
     }
   }
 }
//JavaScript bar interactivity
function movebar5() {
   var elem5 = document.getElementById("js-bar");   
   var width5 = 0;
   var id5 = setInterval(frame5, 20);               //var for how fast the bar grows
   function frame5() {
     if (width5 >= 65) {                            // going up to the desired percentage
       clearInterval(id5);
     } else {
       width5++; 
       elem5.style.width = width5 + '%'; 
       elem5.style.backgroundColor = "rgb(223, 32, 191)";
       elem5.innerHTML = width5 * 1  + '%';         // % written in the bar
       elem5.style.color = "white";
       elem5.style.padding = "2px";
     }
   }
 }
//***********************************************************************//
// Function for Mail to Button
function mailTo() {                                     // function to execute when the email icon is pressed (opens user's mail client)
   window.open('mailto:vannyaspasova@gmail.com');

}
// Function for Print CV Button
function printCV () {
   window.print();
}

function researchButton () {  
   var paragraph = document.getElementById("p-display-none");
   if (paragraph.style.display = "none") {             
      paragraph.style.display ="block";                // show paragraph with research projects when button is clicked 
   } 
}
const rButton = document.getElementById("ug-button");
rButton.addEventListener('click', () => {              // hide paragraph with research projects after a time lapse with an event handler function and the method timeOut
   setTimeout(() => {
   const paragraph2 = document.getElementById("p-display-none");
   paragraph2.style.display = "none";
   }, 3000);
});


